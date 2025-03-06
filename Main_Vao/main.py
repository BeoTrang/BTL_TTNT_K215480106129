import sys
import cv2
import threading
import easyocr
import pyodbc
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ultralytics import YOLO
from Main_Vao.UI import Ui_mainWindow

DB_CONNECTION_STRING = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=nekotrang.duckdns.org,1433;DATABASE=HTNDBSX;UID=sa;PWD=Trang16091998"

class LicensePlateRecognition(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)


        self.rtsp_url = "rtsp://admin:Trang16091998@192.168.1.64:554/onvif2"


        # self.model = YOLO("D://Project//Python//TGM//Bienso_v2//training_v1//runs//detect//train5//weights//best.pt")
        self.model = YOLO("D://Project//Python//test_pyqt5//runs//detect//train6//weights//best.pt")
        self.reader = easyocr.Reader(['en', 'vi'])

        # Biến lưu frame mới nhất
        self.current_frame = None


        self.ui.pushButton.clicked.connect(self.detect_license_plate)
        self.ui.pushButton_2.clicked.connect(self.clear_picture)
        self.ui.Button_Save.clicked.connect(self.on_save_button_clicked)


        self.running = True
        self.rtsp_thread = threading.Thread(target=self.show_rtsp_stream, daemon=True)
        self.rtsp_thread.start()

    def show_rtsp_stream(self):
        cap = cv2.VideoCapture(self.rtsp_url)
        while self.running:
            ret, frame = cap.read()
            if ret:
                self.current_frame = frame.copy()
                self.display_image(frame, self.ui.Label_RSTP)
        cap.release()

    def detect_license_plate(self):
        if self.current_frame is None:
            return


        results = self.model(self.current_frame)[0]
        license_plate_text = ""


        for box in results.boxes.xyxy:
            x1, y1, x2, y2 = map(int, box[:4])
            plate_roi = self.current_frame[y1:y2, x1:x2]

            gray_plate = cv2.cvtColor(plate_roi, cv2.COLOR_BGR2GRAY)
            gray_plate = cv2.GaussianBlur(gray_plate, (3, 3), 0)


            detected_texts = self.reader.readtext(gray_plate, detail=1)


            detected_texts = sorted(detected_texts, key=lambda x: x[0][0][1])


            license_plate_text = " ".join([text[1] for text in detected_texts])


            cv2.rectangle(self.current_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)


        self.display_image(self.current_frame, self.ui.Label_Picture)


        self.ui.Label_Bienso.setText(license_plate_text)


        cv2.imwrite("captured_plate.jpg", self.current_frame)

    def clear_picture(self):
        self.ui.Label_Picture.clear()
        self.ui.Label_Bienso.clear()

    def display_image(self, frame, label):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = frame.shape
        bytes_per_line = ch * w
        qimg = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
        label.setPixmap(QPixmap.fromImage(qimg))
        label.setScaledContents(True)

    def on_save_button_clicked(self):
        plate_text = self.ui.Label_Bienso.text()
        image_path = "captured_plate.jpg"

        if plate_text and image_path:
            success = self.save_to_sql(plate_text, image_path)
            if success:
                QMessageBox.information(self, "Thành công", "Lưu vào SQL Server thành công!")
            else:
                QMessageBox.critical(self, "Lỗi", "Lưu vào SQL Server thất bại!")
        else:
            QMessageBox.warning(self, "Cảnh báo", "Chưa có biển số hoặc ảnh để lưu!")

    def save_to_sql(self, plate_text, image_path):
        try:
            # Đọc ảnh và chuyển đổi sang bytes
            img = cv2.imread(image_path)
            _, img_encoded = cv2.imencode('.jpg', img)
            img_bytes = img_encoded.tobytes()

            # Kết nối SQL Server
            conn = pyodbc.connect(DB_CONNECTION_STRING)
            cursor = conn.cursor()

            # Lưu vào database
            cursor.execute("INSERT INTO LicensePlates (PlateNumber, Image) VALUES (?, ?)", plate_text, img_bytes)
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
