# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ra.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1366, 931)
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(14)
        MainWindow.setFont(font)
        self.Menu_Setting = QAction(MainWindow)
        self.Menu_Setting.setObjectName(u"Menu_Setting")
        self.Menu_History = QAction(MainWindow)
        self.Menu_History.setObjectName(u"Menu_History")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Label_RSTP = QLabel(self.centralwidget)
        self.Label_RSTP.setObjectName(u"Label_RSTP")
        self.Label_RSTP.setGeometry(QRect(30, 460, 661, 381))
        self.Label_RSTP.setTabletTracking(False)
        self.Label_RSTP.setStyleSheet(u"border: 2px solid red;\n"
"border-radius: 5px; \n"
"")
        self.Label_RSTP.setScaledContents(False)
        self.Label_RSTP.setWordWrap(False)
        self.Label_RSTP.setOpenExternalLinks(False)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(220, 420, 261, 41))
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(20)
        self.label.setFont(font1)
        self.Label_QR = QLabel(self.centralwidget)
        self.Label_QR.setObjectName(u"Label_QR")
        self.Label_QR.setGeometry(QRect(40, 60, 411, 301))
        self.Label_QR.setTabletTracking(False)
        self.Label_QR.setStyleSheet(u"border: 2px solid red;\n"
"border-radius: 5px; \n"
"")
        self.Label_QR.setScaledContents(False)
        self.Label_QR.setWordWrap(False)
        self.Label_QR.setOpenExternalLinks(False)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(160, 20, 121, 41))
        self.label_2.setFont(font1)
        self.Button_Save = QPushButton(self.centralwidget)
        self.Button_Save.setObjectName(u"Button_Save")
        self.Button_Save.setGeometry(QRect(670, 240, 161, 51))
        self.Button_Save.setFont(font)
        self.Label_Anh1 = QLabel(self.centralwidget)
        self.Label_Anh1.setObjectName(u"Label_Anh1")
        self.Label_Anh1.setGeometry(QRect(750, 460, 601, 381))
        self.Label_Anh1.setTabletTracking(False)
        self.Label_Anh1.setStyleSheet(u"border: 2px solid red;\n"
"border-radius: 5px; /* Bo g\u00f3c 5px */\n"
"")
        self.Label_Anh1.setScaledContents(False)
        self.Label_Anh1.setWordWrap(False)
        self.Label_Anh1.setOpenExternalLinks(False)
        self.Label_Anh2 = QLabel(self.centralwidget)
        self.Label_Anh2.setObjectName(u"Label_Anh2")
        self.Label_Anh2.setGeometry(QRect(860, 60, 491, 341))
        self.Label_Anh2.setTabletTracking(False)
        self.Label_Anh2.setStyleSheet(u"border: 2px solid red;\n"
"border-radius: 5px; \n"
"")
        self.Label_Anh2.setScaledContents(False)
        self.Label_Anh2.setWordWrap(False)
        self.Label_Anh2.setOpenExternalLinks(False)
        self.Label_Bienso = QLabel(self.centralwidget)
        self.Label_Bienso.setObjectName(u"Label_Bienso")
        self.Label_Bienso.setGeometry(QRect(570, 130, 261, 41))
        self.Label_Bienso.setFont(font1)
        self.Label_Bienso.setStyleSheet(u"border: 2px solid red;\n"
"border-radius: 5px; \n"
"")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(470, 180, 101, 41))
        self.label_4.setFont(font1)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(470, 130, 101, 41))
        self.label_3.setFont(font1)
        self.Label_TimeIn = QLabel(self.centralwidget)
        self.Label_TimeIn.setObjectName(u"Label_TimeIn")
        self.Label_TimeIn.setGeometry(QRect(570, 180, 261, 41))
        self.Label_TimeIn.setFont(font1)
        self.Label_TimeIn.setStyleSheet(u"border: 2px solid red;\n"
"border-radius: 5px; \n"
"")
        self.Label_ID = QLabel(self.centralwidget)
        self.Label_ID.setObjectName(u"Label_ID")
        self.Label_ID.setGeometry(QRect(570, 80, 261, 41))
        self.Label_ID.setFont(font1)
        self.Label_ID.setStyleSheet(u"border: 2px solid red;\n"
"border-radius: 5px; \n"
"")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(520, 80, 41, 41))
        self.label_7.setFont(font1)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(1050, 20, 121, 41))
        self.label_5.setFont(font1)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(1000, 420, 151, 41))
        self.label_6.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1366, 33))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menuMenu.addAction(self.Menu_Setting)
        self.menuMenu.addAction(self.Menu_History)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Qu\u00e9t xe ra", None))
        self.Menu_Setting.setText(QCoreApplication.translate("MainWindow", u"C\u00e0i \u0111\u1eb7t", None))
        self.Menu_History.setText(QCoreApplication.translate("MainWindow", u"L\u1ecbch s\u1eed", None))
        self.Label_RSTP.setText(QCoreApplication.translate("MainWindow", u"RSTP", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"CAMERA TR\u1ef0C TI\u1ebeP", None))
        self.Label_QR.setText(QCoreApplication.translate("MainWindow", u"QR", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"QU\u00c9T QR", None))
        self.Button_Save.setText(QCoreApplication.translate("MainWindow", u"Cho xe ra", None))
        self.Label_Anh1.setText(QCoreApplication.translate("MainWindow", u"Picture", None))
        self.Label_Anh2.setText(QCoreApplication.translate("MainWindow", u"RSTP", None))
        self.Label_Bienso.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Gi\u1edd v\u00e0o:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Bi\u1ec3n s\u1ed1:", None))
        self.Label_TimeIn.setText("")
        self.Label_ID.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"BI\u1ec2N S\u1ed0", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u1ea2NH CH\u1ee4P", None))
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
    # retranslateUi

