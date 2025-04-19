# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
import rc_resources

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1920, 1080)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        Widget.setAutoFillBackground(False)
        Widget.setStyleSheet(u"")
        self.Backgr = QLabel(Widget)
        self.Backgr.setObjectName(u"Backgr")
        self.Backgr.setEnabled(True)
        self.Backgr.setGeometry(QRect(30, 0, 1920, 1080))
        sizePolicy.setHeightForWidth(self.Backgr.sizePolicy().hasHeightForWidth())
        self.Backgr.setSizePolicy(sizePolicy)
        self.Backgr.setStyleSheet(u"background-image: url(:/Wallpaper/assets/Wallpaper/2.svg);")
        self.Backgr.setPixmap(QPixmap(u":/Wallpaper/assets/Wallpaper/2.png"))
        self.Backgr.setScaledContents(True)
        self.Sol = QLabel(Widget)
        self.Sol.setObjectName(u"Sol")
        self.Sol.setGeometry(QRect(130, 240, 531, 471))
        self.Sol.setStyleSheet(u"background-color: transparent;\n"
"")
        self.Sol.setFrameShape(QFrame.Shape.StyledPanel)
        self.Sol.setPixmap(QPixmap(u":/images/assets/Images/1.png"))
        self.Sol.setScaledContents(True)
        self.BaseLetra1 = QLabel(Widget)
        self.BaseLetra1.setObjectName(u"BaseLetra1")
        self.BaseLetra1.setGeometry(QRect(780, 380, 181, 171))
        self.BaseLetra1.setAutoFillBackground(False)
        self.BaseLetra1.setPixmap(QPixmap(u":/iconos/assets/Iconos/8.png"))
        self.BaseLetra1.setScaledContents(True)
        self.BaseLetra2 = QLabel(Widget)
        self.BaseLetra2.setObjectName(u"BaseLetra2")
        self.BaseLetra2.setGeometry(QRect(1030, 380, 181, 171))
        self.BaseLetra2.setAutoFillBackground(False)
        self.BaseLetra2.setPixmap(QPixmap(u":/iconos/assets/Iconos/8.png"))
        self.BaseLetra2.setScaledContents(True)
        self.BaseLetra3 = QLabel(Widget)
        self.BaseLetra3.setObjectName(u"BaseLetra3")
        self.BaseLetra3.setGeometry(QRect(1280, 380, 181, 171))
        self.BaseLetra3.setAutoFillBackground(False)
        self.BaseLetra3.setPixmap(QPixmap(u":/iconos/assets/Iconos/8.png"))
        self.BaseLetra3.setScaledContents(True)
        self.Audio = QPushButton(Widget)
        self.Audio.setObjectName(u"Audio")
        self.Audio.setGeometry(QRect(930, 210, 101, 91))
        self.Audio.setStyleSheet(u"background-color: transparent;\n"
"border: none;")
        icon = QIcon()
        icon.addFile(u":/iconos/assets/Iconos/6.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Audio.setIcon(icon)
        self.Audio.setIconSize(QSize(90, 90))
        self.Siguiente = QPushButton(Widget)
        self.Siguiente.setObjectName(u"Siguiente")
        self.Siguiente.setGeometry(QRect(1080, 220, 271, 81))
        self.Siguiente.setStyleSheet(u"background-color: transparent;\n"
"border: none;")
        icon1 = QIcon()
        icon1.addFile(u":/iconos/assets/Iconos/1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Siguiente.setIcon(icon1)
        self.Siguiente.setIconSize(QSize(250, 80))
        self.Salir = QPushButton(Widget)
        self.Salir.setObjectName(u"Salir")
        self.Salir.setGeometry(QRect(1360, 40, 101, 91))
        self.Salir.setStyleSheet(u"background-color: transparent;\n"
"border: none;")
        icon2 = QIcon()
        icon2.addFile(u":/iconos/assets/Iconos/7.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Salir.setIcon(icon2)
        self.Salir.setIconSize(QSize(90, 90))
        self.Instruccion = QLabel(Widget)
        self.Instruccion.setObjectName(u"Instruccion")
        self.Instruccion.setGeometry(QRect(870, 610, 541, 81))
        font = QFont()
        font.setFamilies([u"Baloo 2"])
        font.setPointSize(36)
        font.setBold(True)
        self.Instruccion.setFont(font)
        self.Instruccion.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.Letra1 = QLabel(Widget)
        self.Letra1.setObjectName(u"Letra1")
        self.Letra1.setGeometry(QRect(830, 420, 71, 101))
        font1 = QFont()
        font1.setFamilies([u"Baloo 2"])
        font1.setPointSize(72)
        font1.setBold(True)
        self.Letra1.setFont(font1)
        self.Letra1.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.Letra2 = QLabel(Widget)
        self.Letra2.setObjectName(u"Letra2")
        self.Letra2.setGeometry(QRect(1080, 420, 81, 101))
        self.Letra2.setFont(font1)
        self.Letra2.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.Letra3 = QLabel(Widget)
        self.Letra3.setObjectName(u"Letra3")
        self.Letra3.setGeometry(QRect(1340, 420, 71, 101))
        self.Letra3.setFont(font1)
        self.Letra3.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.Backgr.setText("")
        self.Sol.setText("")
        self.BaseLetra1.setText("")
        self.BaseLetra2.setText("")
        self.BaseLetra3.setText("")
        self.Audio.setText("")
        self.Siguiente.setText("")
        self.Salir.setText("")
        self.Instruccion.setText(QCoreApplication.translate("Widget", u"Completa la palabra", None))
        self.Letra1.setText(QCoreApplication.translate("Widget", u"S", None))
        self.Letra2.setText(QCoreApplication.translate("Widget", u"O", None))
        self.Letra3.setText(QCoreApplication.translate("Widget", u"L", None))
    # retranslateUi

