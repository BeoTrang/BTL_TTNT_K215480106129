import sys
import cv2
import threading
import easyocr
import pyodbc
import re
import time
import numpy as np
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QHeaderView)
from PySide6.QtCore import Qt, QDateTime, QRect
from ultralytics import YOLO
from Main_Vao.UI import Ui_mainWindow
from Main_Ra.setting import Ui_SettingWindow as Ui_Settings
from history import Ui_HistoryWindow
from datetime import datetime
import io
from PIL import Image
import qrcode


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

        QMessageBox.information(self, "Thành công", "Đã lưu và áp dụng cài đặt mới!")
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
        self.ui.RB_Vao_2.toggled.connect(self.update_image_display)  # Kết nối RB_Vao_2
        self.ui.RB_Ra_2.toggled.connect(self.update_image_display)  # Kết nối RB_Ra_2

        self.ui.RB_Vao.setChecked(True)
        self.ui.RB_Vao_2.setChecked(True)  # Mặc định chọn RB_Vao_2 (hiển thị Anh1)

        self.ui.TW.setRowCount(0)
        self.ui.TW.setColumnCount(7)  # Thêm cột cho Anh3
        self.ui.TW.setHorizontalHeaderLabels(
            ["ID", "Biển số", "Thời gian vào", "Thời gian ra", "Anh1 (ẩn)", "Anh2 (ẩn)", "Anh3 (ẩn)"])
        self.ui.TW.setColumnHidden(4, True)
        self.ui.TW.setColumnHidden(5, True)
        self.ui.TW.setColumnHidden(6, True)
        self.ui.TW.setGeometry(QRect(750, 140, 511, 561))
        self.ui.TW.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.current_row = None  # Khởi tạo self.current_row trong __init__

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
            QMessageBox.critical(self, "Lỗi", f"Không thể tìm kiếm: {e}")

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


class LicensePlateRecognition(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

        self.load_config_from_file()

        self.model = YOLO("D://Project//Python//test_pyqt5//runs//detect//train16//weights//best.pt")
        self.reader = easyocr.Reader(['en'])
        self.current_frame = None
        self.ui.pushButton.clicked.connect(self.detect_license_plate)
        self.ui.pushButton_2.clicked.connect(self.clear_picture)
        self.ui.Button_Save.clicked.connect(self.on_save_button_clicked)
        self.ui.Q_Setting.triggered.connect(self.open_settings)
        self.ui.Q_History.triggered.connect(self.open_history)
        self.ui.Button_Restart.clicked.connect(self.restart_rtsp_stream)
        self.ui.BT_QR.clicked.connect(self.generate_qr_code)

        self.running = True
        self.rtsp_thread = threading.Thread(target=self.show_rtsp_stream, daemon=True)
        self.rtsp_thread.start()

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
                time.sleep(5)
                continue

            while self.running:
                ret, frame = cap.read()
                if ret:
                    self.current_frame = frame.copy()
                    self.display_image(frame, self.ui.Label_RSTP)
                else:
                    print(f"Luồng RTSP bị ngắt: {self.rtsp_url}. Đang khởi động lại sau 5 giây...")
                    cap.release()
                    time.sleep(5)
                    break
            cap.release()

    def detect_license_plate(self):
        self.ui.Label_Picture.clear()
        self.ui.Label_Bienso.clear()
        self.ui.Label_Picture_2.clear()
        self.ui.Label_Time.clear()
        if self.current_frame is None:
            return

        results = self.model(self.current_frame)[0]
        license_plate_text = ""
        gray_plate = None

        for box, cls in zip(results.boxes.xyxy, results.boxes.cls):
            if int(cls) == 0:
                x1, y1, x2, y2 = map(int, box[:4])
                x1, y1, x2, y2 = max(x1 - 10, 0), max(y1 - 10, 0), min(x2 + 10, self.current_frame.shape[1]), min(
                    y2 + 10, self.current_frame.shape[0])
                if x2 - x1 <= 0 or y2 - y1 <= 0:
                    continue
                plate_roi = self.current_frame[y1:y2, x1:x2]
                if plate_roi is None or plate_roi.size == 0:
                    continue

                plate_roi_corrected, angle = self.correct_skew(plate_roi)
                gray_plate = self.preprocess_plate(plate_roi_corrected)
                gray_plate_resized = cv2.resize(gray_plate, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
                ocr_thread = threading.Thread(target=self.run_ocr, args=(gray_plate_resized,))
                ocr_thread.start()
                ocr_thread.join()
                license_plate_text = self.license_plate_text

                cv2.rectangle(self.current_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.imwrite("captured_plate.jpg", self.current_frame)
                cv2.imwrite("anh_bien_so.jpg", gray_plate)
                break

        now = datetime.now()
        formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
        self.ui.Label_Bienso.setText(license_plate_text)
        self.ui.Label_Time.setText(formatted_time)
        self.display_image(self.current_frame, self.ui.Label_Picture)
        if gray_plate is not None and gray_plate.size > 0:
            self.display_image(gray_plate, self.ui.Label_Picture_2)
            cv2.imwrite("anh_bien_so.jpg", gray_plate)

    def run_ocr(self, gray_plate):
        detected_texts = self.reader.readtext(gray_plate, detail=1, contrast_ths=1, adjust_contrast=.5,
                                              text_threshold=.9, low_text=0.5, beamWidth=1, batch_size=1)
        raw_text = " ".join([text[1] for text in detected_texts])
        license_plate_text = "".join(re.findall(r'[A-Za-z0-9]', raw_text))
        self.license_plate_text = license_plate_text.upper()

    def clear_picture(self):
        self.ui.Label_Picture.clear()
        self.ui.Label_Bienso.clear()
        self.ui.Label_Picture_2.clear()
        self.ui.Label_Time.clear()

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

    def on_save_button_clicked(self):
        plate_text = self.ui.Label_Bienso.text()
        image_path_1 = "captured_plate.jpg"
        image_path_2 = "anh_bien_so.jpg"
        thoigian_vao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        thoigian_ra = None

        if plate_text and image_path_1 and image_path_2:
            success = self.save_to_sql(plate_text, image_path_1, image_path_2, thoigian_vao, thoigian_ra)
            if success:
                QMessageBox.information(self, "Thành công", "Lưu vào SQL Server thành công!")
            else:
                QMessageBox.critical(self, "Lỗi", "Lưu vào SQL Server thất bại!")
        else:
            QMessageBox.warning(self, "Cảnh báo", "Chưa có biển số hoặc ảnh để lưu!")

    def save_to_sql(self, plate_text, image_path_1, image_path_2, thoigian_vao, thoigian_ra):
        try:
            img1 = cv2.imread(image_path_1)
            img2 = cv2.imread(image_path_2)
            _, img1_encoded = cv2.imencode('.jpg', img1)
            _, img2_encoded = cv2.imencode('.jpg', img2)
            img1_bytes = img1_encoded.tobytes()
            img2_bytes = img2_encoded.tobytes()
            conn = pyodbc.connect(self.DB_CONNECTION_STRING)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Xe (BienSo, Anh1, Anh2, ThoigianVao, ThoigianRa) VALUES (?, ?, ?, ?, ?)",
                           plate_text, img1_bytes, img2_bytes, thoigian_vao, thoigian_ra)
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except Exception as e:
            print(f"Lỗi khi lưu vào SQL Server: {e}")
            return False

    def generate_qr_code(self):
        try:
            conn = pyodbc.connect(self.DB_CONNECTION_STRING)
            cursor = conn.cursor()
            cursor.execute("SELECT TOP 1 ID FROM Xe ORDER BY ID DESC")
            row = cursor.fetchone()
            if row:
                latest_id = str(row[0])
                self.ui.Label_Time_2.setText(latest_id)
            else:
                latest_id = "No ID found"
                self.ui.Label_Time_2.setText(latest_id)
                QMessageBox.warning(self, "Cảnh báo", "Không tìm thấy ID nào trong cơ sở dữ liệu!")
                return
            cursor.close()
            conn.close()

            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(latest_id)
            qr.make(fit=True)

            qr_img = qr.make_image(fill_color="black", back_color="white")
            qr_img = qr_img.convert("RGB")

            qr_buffer = io.BytesIO()
            qr_img.save(qr_buffer, format="PNG")
            qr_data = qr_buffer.getvalue()
            qimg = QImage.fromData(qr_data)
            pixmap = QPixmap.fromImage(qimg).scaled(self.ui.Label_QR.size(), Qt.KeepAspectRatio)
            self.ui.Label_QR.setPixmap(pixmap)

            print(f"Mã QR đã được tạo cho ID: {latest_id}")
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Không thể tạo mã QR: {e}")

    def correct_skew(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        edges = cv2.Canny(blurred, 50, 150)
        lines = cv2.HoughLines(edges, 1, np.pi / 180, 100)
        if lines is not None:
            angles = []
            for line in lines:
                rho, theta = line[0]
                angle = theta * 180 / np.pi
                if 45 <= angle <= 135:
                    angles.append(angle - 90)
            if angles:
                median_angle = np.median(angles)
                (h, w) = image.shape[:2]
                center = (w // 2, h // 2)
                M = cv2.getRotationMatrix2D(center, median_angle, 1.0)
                rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
                return rotated, median_angle
        return image, 0

    def preprocess_plate(self, plate_roi):
        gray = cv2.cvtColor(plate_roi, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (5, 5), 0)
        gray = cv2.equalizeHist(gray)
        _, binary = cv2.threshold(gray, 255, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        return binary

    def closeEvent(self, event):
        self.running = False
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LicensePlateRecognition()
    window.show()
    sys.exit(app.exec())