# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(1746, 967)
        self.Q_Setting = QAction(mainWindow)
        self.Q_Setting.setObjectName(u"Q_Setting")
        self.Q_History = QAction(mainWindow)
        self.Q_History.setObjectName(u"Q_History")
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(250, 0, 261, 41))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(20)
        self.label.setFont(font)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(760, 40, 161, 51))
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(14)
        self.pushButton.setFont(font1)
        self.Label_RSTP = QLabel(self.centralwidget)
        self.Label_RSTP.setObjectName(u"Label_RSTP")
        self.Label_RSTP.setGeometry(QRect(20, 40, 721, 401))
        self.Label_RSTP.setTabletTracking(False)
        self.Label_RSTP.setStyleSheet(u"border: 2px solid red;\n"
"border-radius: 5px; \n"
"")
        self.Label_RSTP.setScaledContents(False)
        self.Label_RSTP.setWordWrap(False)
        self.Label_RSTP.setOpenExternalLinks(False)
        self.Label_Picture = QLabel(self.centralwidget)
        self.Label_Picture.setObjectName(u"Label_Picture")
        self.Label_Picture.setGeometry(QRect(20, 490, 721, 401))
        self.Label_Picture.setTabletTracking(False)
        self.Label_Picture.setStyleSheet(u"border: 2px solid red;\n"
"border-radius: 5px; /* Bo g\u00f3c 5px */\n"
"")
        self.Label_Picture.setScaledContents(False)
        self.Label_Picture.setWordWrap(False)
        self.Label_Picture.setOpenExternalLinks(False)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(240, 450, 321, 41))
        self.label_2.setFont(font)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(760, 110, 101, 41))
        self.label_3.setFont(font)
        self.Label_Bienso = QLabel(self.centralwidget)
        self.Label_Bienso.setObjectName(u"Label_Bienso")
        self.Label_Bienso.setGeometry(QRect(860, 110, 261, 41))
        self.Label_Bienso.setFont(font)
        self.Label_Bienso.setStyleSheet(u"border: 2px solid red;\n"
"border-radius: 5px; \n"
"")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(960, 40, 161, 51))
        self.pushButton_2.setFont(font1)
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(1400, 590, 161, 51))
        self.pushButton_3.setFont(font1)
        self.Button_Save = QPushButton(self.centralwidget)
        self.Button_Save.setObjectName(u"Button_Save")
        self.Button_Save.setGeometry(QRect(760, 210, 161, 51))
        self.Button_Save.setFont(font1)
        self.Label_Picture_2 = QLabel(self.centralwidget)
        self.Label_Picture_2.setObjectName(u"Label_Picture_2")
        self.Label_Picture_2.setGeometry(QRect(770, 490, 501, 401))
        self.Label_Picture_2.setTabletTracking(False)
        self.Label_Picture_2.setStyleSheet(u"border: 2px solid red;\n"
"border-radius: 5px; /* Bo g\u00f3c 5px */\n"
"")
        self.Label_Picture_2.setScaledContents(False)
        self.Label_Picture_2.setWordWrap(False)
        self.Label_Picture_2.setOpenExternalLinks(False)
        self.Label_Time = QLabel(self.centralwidget)
        self.Label_Time.setObjectName(u"Label_Time")
        self.Label_Time.setGeometry(QRect(860, 160, 261, 41))
        self.Label_Time.setFont(font)
        self.Label_Time.setStyleSheet(u"border: 2px solid red;\n"
"border-radius: 5px; \n"
"")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(760, 160, 101, 41))
        self.label_4.setFont(font)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(1150, 40, 131, 41))
        self.label_5.setFont(font)
        self.Label_Bienso_4 = QLabel(self.centralwidget)
        self.Label_Bienso_4.setObjectName(u"Label_Bienso_4")
        self.Label_Bienso_4.setGeometry(QRect(1140, 40, 131, 281))
        self.Label_Bienso_4.setFont(font)
        self.Label_Bienso_4.setStyleSheet(u"border: 2px solid red;\n"
"border-radius: 5px; \n"
"")
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(1150, 100, 111, 91))
        self.pushButton_4.setFont(font1)
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(1150, 210, 111, 91))
        self.pushButton_5.setFont(font1)
        self.Button_Restart = QPushButton(self.centralwidget)
        self.Button_Restart.setObjectName(u"Button_Restart")
        self.Button_Restart.setGeometry(QRect(690, 400, 51, 41))
        self.Button_Restart.setFont(font1)
        self.Label_QR = QLabel(self.centralwidget)
        self.Label_QR.setObjectName(u"Label_QR")
        self.Label_QR.setGeometry(QRect(1310, 150, 421, 421))
        self.Label_QR.setTabletTracking(False)
        self.Label_QR.setStyleSheet(u"border: 2px solid red;\n"
"border-radius: 5px; /* Bo g\u00f3c 5px */\n"
"")
        self.Label_QR.setScaledContents(False)
        self.Label_QR.setWordWrap(False)
        self.Label_QR.setOpenExternalLinks(False)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(1480, 110, 91, 41))
        self.label_6.setFont(font)
        self.Label_Time_2 = QLabel(self.centralwidget)
        self.Label_Time_2.setObjectName(u"Label_Time_2")
        self.Label_Time_2.setGeometry(QRect(1470, 60, 261, 41))
        self.Label_Time_2.setFont(font)
        self.Label_Time_2.setStyleSheet(u"border: 2px solid red;\n"
"border-radius: 5px; \n"
"")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(1420, 60, 41, 41))
        self.label_7.setFont(font)
        self.BT_QR = QPushButton(self.centralwidget)
        self.BT_QR.setObjectName(u"BT_QR")
        self.BT_QR.setGeometry(QRect(1570, 590, 161, 51))
        self.BT_QR.setFont(font1)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1746, 33))
        self.menuC_i_t = QMenu(self.menubar)
        self.menuC_i_t.setObjectName(u"menuC_i_t")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(mainWindow)
        self.statusbar.setObjectName(u"statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuC_i_t.menuAction())
        self.menuC_i_t.addAction(self.Q_Setting)
        self.menuC_i_t.addAction(self.Q_History)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"H\u1ec7 th\u1ed1ng nh\u1eadn di\u1ec7n bi\u1ec3n s\u1ed1 xe v\u00e0 in v\u00e9", None))
        self.Q_Setting.setText(QCoreApplication.translate("mainWindow", u"C\u00e0i \u0111\u1eb7t", None))
        self.Q_History.setText(QCoreApplication.translate("mainWindow", u"L\u1ecbch s\u1eed", None))
        self.label.setText(QCoreApplication.translate("mainWindow", u"CAMERA TR\u1ef0C TI\u1ebeP", None))
        self.pushButton.setText(QCoreApplication.translate("mainWindow", u"Ki\u1ec3m tra xe v\u00e0o", None))
        self.Label_RSTP.setText(QCoreApplication.translate("mainWindow", u"RSTP", None))
        self.Label_Picture.setText(QCoreApplication.translate("mainWindow", u"Picture", None))
        self.label_2.setText(QCoreApplication.translate("mainWindow", u"NH\u1eacN DI\u1ec6N BI\u1ec2N S\u1ed0 XE", None))
        self.label_3.setText(QCoreApplication.translate("mainWindow", u"Bi\u1ec3n s\u1ed1:", None))
        self.Label_Bienso.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("mainWindow", u"Hu\u1ef7 b\u1ecf", None))
        self.pushButton_3.setText(QCoreApplication.translate("mainWindow", u"In v\u00e9", None))
        self.Button_Save.setText(QCoreApplication.translate("mainWindow", u"L\u01b0u ", None))
        self.Label_Picture_2.setText(QCoreApplication.translate("mainWindow", u"Picture", None))
        self.Label_Time.setText("")
        self.label_4.setText(QCoreApplication.translate("mainWindow", u"Gi\u1edd v\u00e0o:", None))
        self.label_5.setText(QCoreApplication.translate("mainWindow", u"BARRIER", None))
        self.Label_Bienso_4.setText("")
        self.pushButton_4.setText(QCoreApplication.translate("mainWindow", u"M\u1ede", None))
        self.pushButton_5.setText(QCoreApplication.translate("mainWindow", u"\u0110\u00d3NG", None))
        self.Button_Restart.setText(QCoreApplication.translate("mainWindow", u"F5", None))
        self.Label_QR.setText(QCoreApplication.translate("mainWindow", u"QR", None))
        self.label_6.setText(QCoreApplication.translate("mainWindow", u"M\u00c3 QR", None))
        self.Label_Time_2.setText("")
        self.label_7.setText(QCoreApplication.translate("mainWindow", u"ID:", None))
        self.BT_QR.setText(QCoreApplication.translate("mainWindow", u"L\u1ea5y QR", None))
        self.menuC_i_t.setTitle(QCoreApplication.translate("mainWindow", u"Menu", None))
    # retranslateUi

