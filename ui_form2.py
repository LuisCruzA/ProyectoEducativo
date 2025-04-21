# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form2.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QWidget)
import resources_rc

class Ui_Form2(object):
    def setupUi(self, Form2):
        if not Form2.objectName():
            Form2.setObjectName(u"Form2")
        Form2.resize(1920, 1080)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form2.sizePolicy().hasHeightForWidth())
        Form2.setSizePolicy(sizePolicy)
        Form2.setAutoFillBackground(False)
        Form2.setStyleSheet(u"")
        self.Backgr = QLabel(Form2)
        self.Backgr.setObjectName(u"Backgr")
        self.Backgr.setEnabled(True)
        self.Backgr.setGeometry(QRect(30, 0, 1920, 1080))
        sizePolicy.setHeightForWidth(self.Backgr.sizePolicy().hasHeightForWidth())
        self.Backgr.setSizePolicy(sizePolicy)
        self.Backgr.setStyleSheet(u"")
        self.Backgr.setPixmap(QPixmap(u":/Wallpaper/assets/Wallpaper/2.png"))
        self.Backgr.setScaledContents(True)
        self.Sol = QLabel(Form2)
        self.Sol.setObjectName(u"Sol")
        self.Sol.setGeometry(QRect(130, 240, 531, 471))
        self.Sol.setStyleSheet(u"background-color: transparent;\n"
"")
        self.Sol.setFrameShape(QFrame.Shape.StyledPanel)
        self.Sol.setPixmap(QPixmap(u":/images/assets/Images/1.png"))
        self.Sol.setScaledContents(True)
        self.BaseLetra1 = QLabel(Form2)
        self.BaseLetra1.setObjectName(u"BaseLetra1")
        self.BaseLetra1.setGeometry(QRect(780, 380, 181, 171))
        self.BaseLetra1.setAutoFillBackground(False)
        self.BaseLetra1.setPixmap(QPixmap(u":/iconos/assets/Iconos/8.png"))
        self.BaseLetra1.setScaledContents(True)
        self.BaseLetra2 = QLabel(Form2)
        self.BaseLetra2.setObjectName(u"BaseLetra2")
        self.BaseLetra2.setGeometry(QRect(1030, 380, 181, 171))
        self.BaseLetra2.setAutoFillBackground(False)
        self.BaseLetra2.setPixmap(QPixmap(u":/iconos/assets/Iconos/8.png"))
        self.BaseLetra2.setScaledContents(True)
        self.BaseLetra3 = QLabel(Form2)
        self.BaseLetra3.setObjectName(u"BaseLetra3")
        self.BaseLetra3.setGeometry(QRect(1280, 380, 181, 171))
        self.BaseLetra3.setAutoFillBackground(False)
        self.BaseLetra3.setPixmap(QPixmap(u":/iconos/assets/Iconos/8.png"))
        self.BaseLetra3.setScaledContents(True)
        self.Audio = QPushButton(Form2)
        self.Audio.setObjectName(u"Audio")
        self.Audio.setGeometry(QRect(930, 190, 101, 111))
        self.Audio.setStyleSheet(u"background-color: transparent;\n"
"border: none;")
        icon = QIcon()
        icon.addFile(u":/iconos/assets/Iconos/6.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Audio.setIcon(icon)
        self.Audio.setIconSize(QSize(90, 90))
        self.Siguiente = QPushButton(Form2)
        self.Siguiente.setObjectName(u"Siguiente")
        self.Siguiente.setGeometry(QRect(1080, 220, 271, 81))
        self.Siguiente.setStyleSheet(u"background-color: transparent;\n"
"border: none;")
        icon1 = QIcon()
        icon1.addFile(u":/iconos/assets/Iconos/1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Siguiente.setIcon(icon1)
        self.Siguiente.setIconSize(QSize(250, 80))
        self.Salir = QPushButton(Form2)
        self.Salir.setObjectName(u"Salir")
        self.Salir.setGeometry(QRect(1350, 30, 111, 101))
        self.Salir.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/iconos/assets/Iconos/7.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Salir.setIcon(icon2)
        self.Salir.setIconSize(QSize(90, 90))
        self.Instruccion = QLabel(Form2)
        self.Instruccion.setObjectName(u"Instruccion")
        self.Instruccion.setGeometry(QRect(800, 580, 541, 81))
        font = QFont()
        font.setFamilies([u"Baloo 2"])
        font.setPointSize(36)
        font.setBold(True)
        self.Instruccion.setFont(font)
        self.Instruccion.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.Letra1 = QLabel(Form2)
        self.Letra1.setObjectName(u"Letra1")
        self.Letra1.setGeometry(QRect(830, 410, 71, 111))
        font1 = QFont()
        font1.setFamilies([u"Baloo 2"])
        font1.setPointSize(72)
        font1.setBold(True)
        self.Letra1.setFont(font1)
        self.Letra1.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.Letra2 = QLabel(Form2)
        self.Letra2.setObjectName(u"Letra2")
        self.Letra2.setGeometry(QRect(1080, 410, 81, 111))
        self.Letra2.setFont(font1)
        self.Letra2.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.Letra3 = QLabel(Form2)
        self.Letra3.setObjectName(u"Letra3")
        self.Letra3.setGeometry(QRect(1340, 410, 71, 111))
        self.Letra3.setFont(font1)
        self.Letra3.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.Retroalimentacion = QLabel(Form2)
        self.Retroalimentacion.setObjectName(u"Retroalimentacion")
        self.Retroalimentacion.setGeometry(QRect(720, 690, 851, 81))
        self.Retroalimentacion.setFont(font)
        self.Retroalimentacion.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.Revisar = QPushButton(Form2)
        self.Revisar.setObjectName(u"Revisar")
        self.Revisar.setGeometry(QRect(1360, 560, 101, 101))
        self.Revisar.setStyleSheet(u"background-color: transparent;\n"
"border: none;")
        icon3 = QIcon()
        icon3.addFile(u":/iconos/assets/Iconos/4.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Revisar.setIcon(icon3)
        self.Revisar.setIconSize(QSize(90, 90))

        self.retranslateUi(Form2)

        QMetaObject.connectSlotsByName(Form2)
    # setupUi

    def retranslateUi(self, Form2):
        Form2.setWindowTitle(QCoreApplication.translate("Form2", u"Widget", None))
        self.Backgr.setText("")
        self.Sol.setText("")
        self.BaseLetra1.setText("")
        self.BaseLetra2.setText("")
        self.BaseLetra3.setText("")
        self.Audio.setText("")
        self.Siguiente.setText("")
        self.Salir.setText("")
        self.Instruccion.setText(QCoreApplication.translate("Form2", u"Completa la palabra", None))
        self.Letra1.setText(QCoreApplication.translate("Form2", u"S", None))
        self.Letra2.setText(QCoreApplication.translate("Form2", u"O", None))
        self.Letra3.setText(QCoreApplication.translate("Form2", u"L", None))
        self.Retroalimentacion.setText("")
        self.Revisar.setText("")
    # retranslateUi

