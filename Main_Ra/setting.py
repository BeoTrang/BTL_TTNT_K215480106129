# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setting.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTextEdit,
    QWidget)

class Ui_SettingWindow(object):
    def setupUi(self, SettingWindow):
        if not SettingWindow.objectName():
            SettingWindow.setObjectName(u"SettingWindow")
        SettingWindow.resize(592, 479)
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(14)
        SettingWindow.setFont(font)
        self.centralwidget = QWidget(SettingWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(280, 30, 121, 31))
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(20)
        self.label.setFont(font1)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 70, 101, 31))
        self.label_2.setFont(font)
        self.TE_LinkRSTP = QTextEdit(self.centralwidget)
        self.TE_LinkRSTP.setObjectName(u"TE_LinkRSTP")
        self.TE_LinkRSTP.setGeometry(QRect(110, 70, 471, 31))
        self.TE_LinkRSTP.setFont(font)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(270, 110, 161, 31))
        self.label_3.setFont(font1)
        self.TE_IP = QTextEdit(self.centralwidget)
        self.TE_IP.setObjectName(u"TE_IP")
        self.TE_IP.setGeometry(QRect(110, 150, 311, 31))
        self.TE_IP.setFont(font)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 150, 101, 31))
        self.label_4.setFont(font)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 190, 101, 31))
        self.label_5.setFont(font)
        self.TE_Port = QTextEdit(self.centralwidget)
        self.TE_Port.setObjectName(u"TE_Port")
        self.TE_Port.setGeometry(QRect(110, 190, 91, 31))
        self.TE_Port.setFont(font)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 230, 101, 31))
        self.label_6.setFont(font)
        self.TE_TK = QTextEdit(self.centralwidget)
        self.TE_TK.setObjectName(u"TE_TK")
        self.TE_TK.setGeometry(QRect(110, 230, 261, 31))
        self.TE_TK.setFont(font)
        self.TE_MK = QTextEdit(self.centralwidget)
        self.TE_MK.setObjectName(u"TE_MK")
        self.TE_MK.setGeometry(QRect(110, 270, 261, 31))
        self.TE_MK.setFont(font)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 270, 101, 31))
        self.label_7.setFont(font)
        self.TE_Database = QTextEdit(self.centralwidget)
        self.TE_Database.setObjectName(u"TE_Database")
        self.TE_Database.setGeometry(QRect(110, 310, 261, 31))
        self.TE_Database.setFont(font)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 310, 101, 31))
        self.label_8.setFont(font)
        self.BT_Save = QPushButton(self.centralwidget)
        self.BT_Save.setObjectName(u"BT_Save")
        self.BT_Save.setGeometry(QRect(480, 350, 101, 51))
        self.BT_Save.setFont(font)
        SettingWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(SettingWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 592, 33))
        SettingWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(SettingWindow)
        self.statusbar.setObjectName(u"statusbar")
        SettingWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SettingWindow)

        QMetaObject.connectSlotsByName(SettingWindow)
    # setupUi

    def retranslateUi(self, SettingWindow):
        SettingWindow.setWindowTitle(QCoreApplication.translate("SettingWindow", u"C\u00e0i \u0111\u1eb7t", None))
        self.label.setText(QCoreApplication.translate("SettingWindow", u"CAMERA", None))
        self.label_2.setText(QCoreApplication.translate("SettingWindow", u"Link RSTP:", None))
        self.label_3.setText(QCoreApplication.translate("SettingWindow", u"DATABASE", None))
        self.label_4.setText(QCoreApplication.translate("SettingWindow", u"\u0110\u1ecba ch\u1ec9 IP:", None))
        self.label_5.setText(QCoreApplication.translate("SettingWindow", u"Port:", None))
        self.label_6.setText(QCoreApplication.translate("SettingWindow", u"T\u00e0i kho\u1ea3n:", None))
        self.label_7.setText(QCoreApplication.translate("SettingWindow", u"M\u1eadt kh\u1ea9u:", None))
        self.label_8.setText(QCoreApplication.translate("SettingWindow", u"Database:", None))
        self.BT_Save.setText(QCoreApplication.translate("SettingWindow", u"L\u01afU", None))
    # retranslateUi

