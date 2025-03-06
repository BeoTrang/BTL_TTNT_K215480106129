import sys
import cv2
import threading
import pyodbc
import numpy as np
import time
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QHeaderView)
from PySide6.QtCore import Qt, QDateTime, QRect
from pyzbar.pyzbar import decode
from ra import Ui_MainWindow
from setting import Ui_SettingWindow as Ui_Settings
from history import Ui_HistoryWindow
import io
from PIL import Image

class SettingsWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Settings()
        self.ui.setupUi(self)
        self.setWindowTitle("Settings")

        if hasattr(self.parent(), 'rtsp_url'):
            self.ui.TE_LinkRSTP.setText(self.parent().rtsp_url)
            self.ui.TE_IP.setText(self.parent().db_server)
            self.ui.TE_Port.setText(self.parent().db_port)
            self.ui.TE_TK.setText(self.parent().db_username)
            self.ui.TE_MK.setText(self.parent().db_password)
            self.ui.TE_Database.setText(self.parent().db_database)

        self.ui.BT_Save.clicked.connect(self.save_settings)

    def save_settings(self):
        rtsp_url = self.ui.TE_LinkRSTP.toPlainText()
        server_ip = self.ui.TE_IP.toPlainText()
        port = self.ui.TE_Port.toPlainText()
        username = self.ui.TE_TK.toPlainText()
        password = self.ui.TE_MK.toPlainText()
        database = self.ui.TE_Database.toPlainText()

        config = {
            "RTSP_URL": rtsp_url,
            "DB_SERVER": server_ip,
            "DB_PORT": port,
            "DB_USERNAME": username,
            "DB_PASSWORD": password,
            "DB_DATABASE": database
        }
        self.save_config_to_file(config)

        if hasattr(self.parent(), 'update_settings'):
            self.parent().update_settings(rtsp_url, server_ip, port, username, password, database)

        self.close()

    def save_config_to_file(self, config):
        with open("config.txt", "w", encoding="utf-8") as f:
            for key, value in config.items():
                f.write(f"{key}={value}\n")

class HistoryWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_HistoryWindow()
        self.ui.setupUi(self)

        current_datetime = QDateTime.currentDateTime()
        self.ui.DTE_Start.setDateTime(current_datetime)
        self.ui.DTE_Start_2.setDateTime(current_datetime)

        self.ui.Button_Search.clicked.connect(self.search_history)
        self.ui.Button_F5.clicked.connect(self.load_history)
        self.ui.TW.itemClicked.connect(self.show_selected_record)
        self.ui.RB_Vao_2.toggled.connect(self.update_image_display)
        self.ui.RB_Ra_2.toggled.connect(self.update_image_display)

        self.ui.RB_Vao.setChecked(True)
        self.ui.RB_Vao_2.setChecked(True)

        self.ui.TW.setRowCount(0)
        self.ui.TW.setColumnCount(7)
        self.ui.TW.setHorizontalHeaderLabels(
            ["ID", "Biển số", "Thời gian vào", "Thời gian ra", "Anh1 (ẩn)", "Anh2 (ẩn)", "Anh3 (ẩn)"])
        self.ui.TW.setColumnHidden(4, True)
        self.ui.TW.setColumnHidden(5, True)
        self.ui.TW.setColumnHidden(6, True)
        self.ui.TW.setGeometry(QRect(750, 140, 511, 561))
        self.ui.TW.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.current_row = None

    def load_history(self):
        self.ui.TW.setRowCount(0)
        self.ui.Label_Bienso.clear()
        self.ui.Label_ThoigianVao.clear()
        self.ui.Label_ThoiGianRa.clear()
        self.ui.Label_Anh_1.clear()
        self.ui.Label_Anh_2.clear()
        self.current_row = None

    def search_history(self):
        start_datetime = self.ui.DTE_Start.dateTime().toString("yyyy-MM-dd HH:mm:ss")
        end_datetime = self.ui.DTE_Start_2.dateTime().toString("yyyy-MM-dd HH:mm:ss")

        try:
            conn = pyodbc.connect(self.parent().DB_CONNECTION_STRING)
            cursor = conn.cursor()
            if self.ui.RB_Vao.isChecked():
                query = "SELECT ID, BienSo, ThoigianVao, ThoigianRa, Anh1, Anh2, Anh3 FROM Xe WHERE ThoigianVao BETWEEN ? AND ? ORDER BY ThoigianVao DESC"
            else:
                query = "SELECT ID, BienSo, ThoigianVao, ThoigianRa, Anh1, Anh2, Anh3 FROM Xe WHERE ThoigianRa BETWEEN ? AND ? ORDER BY ThoigianRa DESC"

            cursor.execute(query, (start_datetime, end_datetime))
            rows = cursor.fetchall()
            self.ui.TW.setRowCount(len(rows))
            self.ui.TW.setColumnCount(7)
            self.ui.TW.setHorizontalHeaderLabels(
                ["ID", "Biển số", "Thời gian vào", "Thời gian ra", "Anh1 (ẩn)", "Anh2 (ẩn)", "Anh3 (ẩn)"])
            for i, row in enumerate(rows):
                self.ui.TW.setItem(i, 0, QTableWidgetItem(str(row[0])))
                self.ui.TW.setItem(i, 1, QTableWidgetItem(row[1]))
                self.ui.TW.setItem(i, 2, QTableWidgetItem(str(row[2])))
                self.ui.TW.setItem(i, 3, QTableWidgetItem(str(row[3]) if row[3] else ""))
                anh1_item = QTableWidgetItem()
                anh1_item.setData(Qt.UserRole, row[4])
                self.ui.TW.setItem(i, 4, anh1_item)
                anh2_item = QTableWidgetItem()
                anh2_item.setData(Qt.UserRole, row[5])
                self.ui.TW.setItem(i, 5, anh2_item)
                anh3_item = QTableWidgetItem()
                anh3_item.setData(Qt.UserRole, row[6])
                self.ui.TW.setItem(i, 6, anh3_item)
            self.ui.TW.setColumnHidden(4, True)
            self.ui.TW.setColumnHidden(5, True)
            self.ui.TW.setColumnHidden(6, True)
            cursor.close()
            conn.close()
        except Exception as e:
            print(f"Không thể tìm kiếm: {e}")

    def show_selected_record(self, item):
        self.current_row = item.row()
        bien_so = self.ui.TW.item(self.current_row, 1).text()
        thoigian_vao = self.ui.TW.item(self.current_row, 2).text()
        thoigian_ra = self.ui.TW.item(self.current_row, 3).text() if self.ui.TW.item(self.current_row, 3) else ""

        self.ui.Label_Bienso.setText(bien_so)
        self.ui.Label_ThoigianVao.setText(thoigian_vao)
        self.ui.Label_ThoiGianRa.setText(thoigian_ra)

        img2_item = self.ui.TW.item(self.current_row, 5)
        if img2_item:
            img2_data = img2_item.data(Qt.UserRole)
            if img2_data:
                try:
                    img2 = Image.open(io.BytesIO(img2_data))
                    if img2.mode != 'RGB':
                        img2 = img2.convert('RGB')
                    qimg2 = QImage(img2.tobytes(), img2.width, img2.height, img2.width * 3, QImage.Format_RGB888)
                    if not qimg2.isNull():
                        pixmap2 = QPixmap.fromImage(qimg2).scaled(self.ui.Label_Anh_2.size(), Qt.KeepAspectRatio)
                        self.ui.Label_Anh_2.setPixmap(pixmap2)
                    else:
                        self.ui.Label_Anh_2.setText("Ảnh 2 không hợp lệ")
                except Exception as e:
                    self.ui.Label_Anh_2.setText(f"Lỗi hiển thị Ảnh 2: {e}")
            else:
                self.ui.Label_Anh_2.setText("Không có Ảnh 2")
        else:
            self.ui.Label_Anh_2.setText("Không có dữ liệu Ảnh 2")

        self.update_image_display()

    def update_image_display(self):
        if self.current_row is None or self.current_row < 0:
            self.ui.Label_Anh_1.clear()
            return

        if self.ui.RB_Vao_2.isChecked():
            img_item = self.ui.TW.item(self.current_row, 4)  # Anh1
            label_text = "Không có Ảnh 1"
        else:
            img_item = self.ui.TW.item(self.current_row, 6)  # Anh3
            label_text = "Không có Ảnh 3"

        if img_item:
            img_data = img_item.data(Qt.UserRole)
            if img_data:
                try:
                    img = Image.open(io.BytesIO(img_data))
                    if img.mode != 'RGB':
                        img = img.convert('RGB')
                    qimg = QImage(img.tobytes(), img.width, img.height, img.width * 3, QImage.Format_RGB888)
                    if not qimg.isNull():
                        pixmap = QPixmap.fromImage(qimg).scaled(self.ui.Label_Anh_1.size(), Qt.KeepAspectRatio)
                        self.ui.Label_Anh_1.setPixmap(pixmap)
                    else:
                        self.ui.Label_Anh_1.setText("Ảnh không hợp lệ")
                except Exception as e:
                    self.ui.Label_Anh_1.setText(f"Lỗi hiển thị ảnh: {e}")
            else:
                self.ui.Label_Anh_1.setText(label_text)
        else:
            self.ui.Label_Anh_1.setText(label_text)

class ExitVehicleApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.load_config_from_file()

        self.current_frame_rtsp = None
        self.current_frame_webcam = None
        self.running = True
        self.last_qr_data = None
        self.current_id = None

        self.rtsp_thread = threading.Thread(target=self.show_rtsp_stream, daemon=True)
        self.rtsp_thread.start()

        self.webcam_thread = threading.Thread(target=self.show_webcam_stream, daemon=True)
        self.webcam_thread.start()

        self.ui.Button_Save.clicked.connect(self.confirm_vehicle_exit)
        self.ui.Menu_Setting.triggered.connect(self.open_settings)
        self.ui.Menu_History.triggered.connect(self.open_history)

    def load_config_from_file(self):
        self.rtsp_url = "rtsp://admin:ONYTPY@nekotrang.duckdns.org:554/onvif1"
        self.db_server = "nekotrang.duckdns.org"
        self.db_port = "1433"
        self.db_username = "sa"
        self.db_password = "NekoTrang16091998"
        self.db_database = "HTNDBSX1"

        try:
            with open("config.txt", "r", encoding="utf-8") as f:
                for line in f:
                    if "=" in line:
                        key, value = line.strip().split("=", 1)
                        if key == "RTSP_URL":
                            self.rtsp_url = value
                        elif key == "DB_SERVER":
                            self.db_server = value
                        elif key == "DB_PORT":
                            self.db_port = value
                        elif key == "DB_USERNAME":
                            self.db_username = value
                        elif key == "DB_PASSWORD":
                            self.db_password = value
                        elif key == "DB_DATABASE":
                            self.db_database = value
        except FileNotFoundError:
            print("Không tìm thấy file config.txt, sử dụng giá trị mặc định.")
            self.save_config_to_file({
                "RTSP_URL": self.rtsp_url,
                "DB_SERVER": self.db_server,
                "DB_PORT": self.db_port,
                "DB_USERNAME": self.db_username,
                "DB_PASSWORD": self.db_password,
                "DB_DATABASE": self.db_database
            })

        self.update_db_connection_string()

    def save_config_to_file(self, config):
        with open("config.txt", "w", encoding="utf-8") as f:
            for key, value in config.items():
                f.write(f"{key}={value}\n")

    def update_db_connection_string(self):
        self.DB_CONNECTION_STRING = (
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={self.db_server},{self.db_port};"
            f"DATABASE={self.db_database};"
            f"UID={self.db_username};"
            f"PWD={self.db_password}"
        )

    def update_settings(self, rtsp_url, server_ip, port, username, password, database):
        self.db_server = server_ip
        self.db_port = port
        self.db_username = username
        self.db_password = password
        self.db_database = database
        self.update_db_connection_string()

        if rtsp_url != self.rtsp_url:
            self.rtsp_url = rtsp_url
            self.restart_rtsp_stream()

    def restart_rtsp_stream(self):
        self.running = False
        if self.rtsp_thread.is_alive():
            self.rtsp_thread.join()
        self.running = True
        self.rtsp_thread = threading.Thread(target=self.show_rtsp_stream, daemon=True)
        self.rtsp_thread.start()
        print("Luồng RTSP đã được khởi động lại bởi người dùng.")

    def open_settings(self):
        self.settings_window = SettingsWindow(self)
        self.settings_window.show()

    def open_history(self):
        self.history_window = HistoryWindow(self)
        self.history_window.show()

    def show_rtsp_stream(self):
        while self.running:
            cap = cv2.VideoCapture(self.rtsp_url)
            if not cap.isOpened():
                print(f"Không thể kết nối đến RTSP URL: {self.rtsp_url}. Đang thử lại sau 5 giây...")
                time.sleep(5)  # Chờ 5 giây trước khi thử lại
                continue

            while self.running:
                ret, frame = cap.read()
                if ret:
                    self.current_frame_rtsp = frame.copy()
                    self.display_image(frame, self.ui.Label_RSTP)
                else:
                    print(f"Luồng RTSP bị ngắt: {self.rtsp_url}. Đang tự động khởi động lại sau 5 giây...")
                    cap.release()
                    time.sleep(5)  # Chờ 5 giây trước khi thử kết nối lại
                    break
            cap.release()

    def show_webcam_stream(self):
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Không thể mở webcam!")
            return
        while self.running:
            ret, frame = cap.read()
            if ret:
                self.current_frame_webcam = frame.copy()
                self.display_image(frame, self.ui.Label_QR)

                decoded_objects = decode(self.current_frame_webcam)
                if decoded_objects:
                    qr_data = decoded_objects[0].data.decode("utf-8")
                    if qr_data != self.last_qr_data:
                        print(f"Đã quét được mã QR: {qr_data}")
                        self.last_qr_data = qr_data
                        self.current_id = qr_data
                        self.fetch_vehicle_info(qr_data)
                time.sleep(0.1)
            else:
                print("Không thể đọc từ webcam!")
                break
        cap.release()

    def display_image(self, frame, label):
        if len(frame.shape) == 2:
            frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)
        else:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = frame.shape
        bytes_per_line = ch * w
        qimg = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
        label.setPixmap(QPixmap.fromImage(qimg))
        label.setScaledContents(True)

    def fetch_vehicle_info(self, qr_data):
        self.ui.Label_ID.setText(qr_data)

        try:
            conn = pyodbc.connect(self.DB_CONNECTION_STRING)
            cursor = conn.cursor()
            query = "SELECT BienSo, ThoigianVao, Anh1, Anh2 FROM Xe WHERE ID = ?"
            cursor.execute(query, (qr_data,))
            row = cursor.fetchone()

            if row:
                bien_so, thoigian_vao, anh1_data, anh2_data = row
                self.ui.Label_Bienso.setText(bien_so)
                self.ui.Label_TimeIn.setText(str(thoigian_vao))

                if anh1_data:
                    try:
                        img1 = Image.open(io.BytesIO(anh1_data))
                        if img1.mode != 'RGB':
                            img1 = img1.convert('RGB')
                        qimg1 = QImage(img1.tobytes(), img1.width, img1.height, img1.width * 3, QImage.Format_RGB888)
                        if not qimg1.isNull():
                            pixmap1 = QPixmap.fromImage(qimg1).scaled(self.ui.Label_Anh1.size(), Qt.KeepAspectRatio)
                            self.ui.Label_Anh1.setPixmap(pixmap1)
                        else:
                            self.ui.Label_Anh1.setText("Ảnh 1 không hợp lệ")
                    except Exception as e:
                        self.ui.Label_Anh1.setText(f"Lỗi hiển thị Ảnh 1: {e}")
                else:
                    self.ui.Label_Anh1.setText("Không có Ảnh 1")

                if anh2_data:
                    try:
                        img2 = Image.open(io.BytesIO(anh2_data))
                        if img2.mode != 'RGB':
                            img2 = img2.convert('RGB')
                        qimg2 = QImage(img2.tobytes(), img2.width, img2.height, img2.width * 3, QImage.Format_RGB888)
                        if not qimg2.isNull():
                            pixmap2 = QPixmap.fromImage(qimg2).scaled(self.ui.Label_Anh2.size(), Qt.KeepAspectRatio)
                            self.ui.Label_Anh2.setPixmap(pixmap2)
                        else:
                            self.ui.Label_Anh2.setText("Ảnh 2 không hợp lệ")
                    except Exception as e:
                        self.ui.Label_Anh2.setText(f"Lỗi hiển thị Ảnh 2: {e}")
                else:
                    self.ui.Label_Anh2.setText("Không có Ảnh 2")
            else:
                print(f"Không tìm thấy xe với ID: {qr_data}")
            cursor.close()
            conn.close()
        except Exception as e:
            print(f"Không thể truy vấn cơ sở dữ liệu: {e}")

    def confirm_vehicle_exit(self):
        if not self.current_id:
            print("Chưa quét được mã QR để xác nhận xe ra!")
            return

        if self.current_frame_rtsp is None:
            print("Không có hình ảnh từ RTSP để lưu vào Anh3!")
            return

        _, img_encoded = cv2.imencode('.jpg', self.current_frame_rtsp)
        anh3_bytes = img_encoded.tobytes()

        try:
            conn = pyodbc.connect(self.DB_CONNECTION_STRING)
            cursor = conn.cursor()
            thoigian_ra = time.strftime("%Y-%m-%d %H:%M:%S")
            query = "UPDATE Xe SET ThoigianRa = ?, Anh3 = ? WHERE ID = ?"
            cursor.execute(query, (thoigian_ra, anh3_bytes, self.current_id))
            conn.commit()
            cursor.close()
            conn.close()
            print(f"Đã cập nhật ThoigianRa và Anh3 cho xe với ID: {self.current_id} - {thoigian_ra}")

            self.ui.Label_ID.clear()
            self.ui.Label_Bienso.clear()
            self.ui.Label_TimeIn.clear()
            self.ui.Label_Anh1.clear()
            self.ui.Label_Anh2.clear()
            self.current_id = None
            self.last_qr_data = None
        except Exception as e:
            print(f"Không thể cập nhật ThoigianRa và Anh3: {e}")

    def closeEvent(self, event):
        self.running = False
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExitVehicleApp()
    window.show()
    sys.exit(app.exec())