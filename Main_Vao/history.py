# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'history.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateTimeEdit, QHeaderView, QLabel,
    QMainWindow, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_HistoryWindow(object):
    def setupUi(self, HistoryWindow):
        if not HistoryWindow.objectName():
            HistoryWindow.setObjectName(u"HistoryWindow")
        HistoryWindow.resize(1270, 768)
        self.centralwidget = QWidget(HistoryWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Label_Anh_1 = QLabel(self.centralwidget)
        self.Label_Anh_1.setObjectName(u"Label_Anh_1")
        self.Label_Anh_1.setGeometry(QRect(10, 270, 691, 431))
        self.Label_Anh_1.setTabletTracking(False)
        self.Label_Anh_1.setStyleSheet(u"border: 2px solid red;\n"
"border-radius: 5px; \n"
"")
        self.Label_Anh_1.setScaledContents(False)
        self.Label_Anh_1.setWordWrap(False)
        self.Label_Anh_1.setOpenExternalLinks(False)
        self.Label_Bienso = QLabel(self.centralwidget)
        self.Label_Bienso.setObjectName(u"Label_Bienso")
        self.Label_Bienso.setGeometry(QRect(440, 10, 251, 41))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(20)
        self.Label_Bienso.setFont(font)
        self.Label_Bienso.setStyleSheet(u"border: 2px solid red;\n"
"border-radius: 5px; \n"
"")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(340, 10, 101, 41))
        self.label_3.setFont(font)
        self.Label_Anh_2 = QLabel(self.centralwidget)
        self.Label_Anh_2.setObjectName(u"Label_Anh_2")
        self.Label_Anh_2.setGeometry(QRect(10, 10, 321, 241))
        self.Label_Anh_2.setTabletTracking(False)
        self.Label_Anh_2.setStyleSheet(u"border: 2px solid red;\n"
"border-radius: 5px; \n"
"")
        self.Label_Anh_2.setScaledContents(False)
        self.Label_Anh_2.setWordWrap(False)
        self.Label_Anh_2.setOpenExternalLinks(False)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(340, 70, 101, 41))
        self.label_4.setFont(font)
        self.Label_ThoigianVao = QLabel(self.centralwidget)
        self.Label_ThoigianVao.setObjectName(u"Label_ThoigianVao")
        self.Label_ThoigianVao.setGeometry(QRect(440, 70, 251, 41))
        self.Label_ThoigianVao.setFont(font)
        self.Label_ThoigianVao.setStyleSheet(u"border: 2px solid red;\n"
"border-radius: 5px; \n"
"")
        self.Button_Search = QPushButton(self.centralwidget)
        self.Button_Search.setObjectName(u"Button_Search")
        self.Button_Search.setGeometry(QRect(1130, 90, 131, 41))
        self.Button_Search.setFont(font)
        self.Button_F5 = QPushButton(self.centralwidget)
        self.Button_F5.setObjectName(u"Button_F5")
        self.Button_F5.setGeometry(QRect(630, 190, 61, 41))
        self.Button_F5.setFont(font)
        self.TW = QTableWidget(self.centralwidget)
        self.TW.setObjectName(u"TW")
        self.TW.setGeometry(QRect(750, 140, 511, 561))
        self.Label_ThoiGianRa = QLabel(self.centralwidget)
        self.Label_ThoiGianRa.setObjectName(u"Label_ThoiGianRa")
        self.Label_ThoiGianRa.setGeometry(QRect(440, 130, 251, 41))
        self.Label_ThoiGianRa.setFont(font)
        self.Label_ThoiGianRa.setStyleSheet(u"border: 2px solid red;\n"
"border-radius: 5px; \n"
"")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(340, 130, 101, 41))
        self.label_5.setFont(font)
        self.DTE_Start_2 = QDateTimeEdit(self.centralwidget)
        self.DTE_Start_2.setObjectName(u"DTE_Start_2")
        self.DTE_Start_2.setGeometry(QRect(1030, 50, 231, 31))
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(14)
        self.DTE_Start_2.setFont(font1)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(860, 0, 171, 41))
        self.label_6.setFont(font)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(960, 40, 51, 41))
        self.label_7.setFont(font)
        self.DTE_Start = QDateTimeEdit(self.centralwidget)
        self.DTE_Start.setObjectName(u"DTE_Start")
        self.DTE_Start.setGeometry(QRect(1030, 10, 231, 31))
        self.DTE_Start.setFont(font1)
        self.RB_Ra = QRadioButton(self.centralwidget)
        self.RB_Ra.setObjectName(u"RB_Ra")
        self.RB_Ra.setGeometry(QRect(1030, 100, 61, 20))
        self.RB_Ra.setFont(font)
        self.RB_Vao = QRadioButton(self.centralwidget)
        self.RB_Vao.setObjectName(u"RB_Vao")
        self.RB_Vao.setGeometry(QRect(950, 100, 71, 20))
        self.RB_Vao.setFont(font)
        self.RB_Vao_2 = QRadioButton(self.centralwidget)
        self.RB_Vao_2.setObjectName(u"RB_Vao_2")
        self.RB_Vao_2.setGeometry(QRect(370, 220, 71, 20))
        self.RB_Vao_2.setFont(font)
        self.RB_Ra_2 = QRadioButton(self.centralwidget)
        self.RB_Ra_2.setObjectName(u"RB_Ra_2")
        self.RB_Ra_2.setGeometry(QRect(450, 220, 71, 20))
        self.RB_Ra_2.setFont(font)
        HistoryWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(HistoryWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1270, 33))
        HistoryWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(HistoryWindow)
        self.statusbar.setObjectName(u"statusbar")
        HistoryWindow.setStatusBar(self.statusbar)

        self.retranslateUi(HistoryWindow)

        QMetaObject.connectSlotsByName(HistoryWindow)
    # setupUi

    def retranslateUi(self, HistoryWindow):
        HistoryWindow.setWindowTitle(QCoreApplication.translate("HistoryWindow", u"L\u1ecbch s\u1eed", None))
        self.Label_Anh_1.setText(QCoreApplication.translate("HistoryWindow", u"ANH", None))
        self.Label_Bienso.setText("")
        self.label_3.setText(QCoreApplication.translate("HistoryWindow", u"Bi\u1ec3n s\u1ed1:", None))
        self.Label_Anh_2.setText(QCoreApplication.translate("HistoryWindow", u"ANH", None))
        self.label_4.setText(QCoreApplication.translate("HistoryWindow", u"Gi\u1edd v\u00e0o:", None))
        self.Label_ThoigianVao.setText("")
        self.Button_Search.setText(QCoreApplication.translate("HistoryWindow", u"T\u00ecm ki\u1ebfm", None))
        self.Button_F5.setText(QCoreApplication.translate("HistoryWindow", u"F5", None))
        self.Label_ThoiGianRa.setText("")
        self.label_5.setText(QCoreApplication.translate("HistoryWindow", u"Gi\u1edd ra:", None))
        self.label_6.setText(QCoreApplication.translate("HistoryWindow", u"Trong kho\u1ea3ng:", None))
        self.label_7.setText(QCoreApplication.translate("HistoryWindow", u"\u0110\u1ebfn:", None))
        self.RB_Ra.setText(QCoreApplication.translate("HistoryWindow", u"Ra", None))
        self.RB_Vao.setText(QCoreApplication.translate("HistoryWindow", u"V\u00e0o", None))
        self.RB_Vao_2.setText(QCoreApplication.translate("HistoryWindow", u"V\u00e0o", None))
        self.RB_Ra_2.setText(QCoreApplication.translate("HistoryWindow", u"Ra", None))
    # retranslateUi

