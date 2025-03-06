import sys
import cv2
import threading
import easyocr
import pyodbc
import re
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ultralytics import YOLO
from Main_Vao.UI import Ui_mainWindow
from datetime import datetime

DB_CONNECTION_STRING = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=192.168.1.96,1433;DATABASE=HTNDBSX1;UID=sa;PWD=Trang16091998"

class LicensePlateRecognition(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

        self.camera_index = 1
        self.model = YOLO("D://Project//Python//test_pyqt5//runs//detect//train11//weights//best.pt")
        self.reader = easyocr.Reader(['en'])
        self.current_frame = None

        self.ui.pushButton.clicked.connect(self.detect_license_plate)
        self.ui.pushButton_2.clicked.connect(self.clear_picture)
        self.ui.Button_Save.clicked.connect(self.on_save_button_clicked)

        self.running = True
        self.camera_thread = threading.Thread(target=self.show_webcam_stream, daemon=True)
        self.camera_thread.start()

    def show_webcam_stream(self):
        cap = cv2.VideoCapture(self.camera_index)
        while self.running:
            ret, frame = cap.read()
            if ret:
                self.current_frame = frame.copy()
                self.display_image(frame, self.ui.Label_RSTP)
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
                if x2 - x1 <= 0 or y2 - y1 <= 0:
                    continue
                plate_roi = self.current_frame[y1:y2, x1:x2]
                if plate_roi is None or plate_roi.size == 0:
                    continue

                gray_plate = self.preprocess_plate(plate_roi)
                detected_texts = self.reader.readtext(gray_plate, detail=1)
                raw_text = " ".join([text[1] for text in detected_texts])
                license_plate_text = "".join(re.findall(r'[A-Za-z0-9]', raw_text))

                cv2.rectangle(self.current_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.imwrite("captured_plate.jpg", self.current_frame)
                cv2.imwrite("anh_bien_so.jpg", gray_plate)

        now = datetime.now()
        formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
        self.ui.Label_Bienso.setText(license_plate_text)
        self.ui.Label_Time.setText(formatted_time)
        self.display_image(self.current_frame, self.ui.Label_Picture)

        if gray_plate is not None and gray_plate.size > 0:
            self.display_image(gray_plate, self.ui.Label_Picture_2)
            cv2.imwrite("anh_bien_so.jpg", gray_plate)

    def preprocess_plate(self, plate_roi):
        gray = cv2.cvtColor(plate_roi, cv2.COLOR_BGR2GRAY)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        gray = clahe.apply(gray)
        gray = cv2.GaussianBlur(gray, (5, 5), 0)
        binary = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
        return binary
    def clear_picture(self):
        self.ui.Label_Picture.clear()
        self.ui.Label_Bienso.clear()
        self.ui.Label_Picture_2.clear()
        self.ui.Label_Time.clear()

    def display_image(self, frame, label):
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
        Time = self.ui.Label_Time.text()

        if plate_text and image_path_1 and image_path_2:
            success = self.save_to_sql(plate_text, image_path_1, image_path_2, Time)
            if success:
                QMessageBox.information(self, "Thành công", "Lưu vào SQL Server thành công!")
            else:
                QMessageBox.critical(self, "Lỗi", "Lưu vào SQL Server thất bại!")
        else:
            QMessageBox.warning(self, "Cảnh báo", "Chưa có biển số hoặc ảnh để lưu!")

    def save_to_sql(self, plate_text, image_path_1, image_path_2, Time):
        try:
            img1 = cv2.imread(image_path_1)
            img2 = cv2.imread(image_path_2)
            _, img1_encoded = cv2.imencode('.jpg', img1)
            _, img2_encoded = cv2.imencode('.jpg', img2)
            img1_bytes = img1_encoded.tobytes()
            img2_bytes = img2_encoded.tobytes()

            conn = pyodbc.connect(DB_CONNECTION_STRING)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Xe (BienSo, Anh1, Anh2, Thoigian) VALUES (?, ?, ?, ?)", plate_text, img1_bytes, img2_bytes, Time)
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except Exception as e:
            print(f"Lỗi khi lưu vào SQL Server: {e}")
            return False

    def closeEvent(self, event):
        self.running = False
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LicensePlateRecognition()
    window.show()
    sys.exit(app.exec())
