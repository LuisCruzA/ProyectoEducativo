# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu_principal.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)
import rc_resources

class Ui_MenuPrincipal(object):
    def setupUi(self, MenuPrincipal):
        if not MenuPrincipal.objectName():
            MenuPrincipal.setObjectName(u"MenuPrincipal")
        MenuPrincipal.resize(1920, 1080)
        self.Backgr = QLabel(MenuPrincipal)
        self.Backgr.setObjectName(u"Backgr")
        self.Backgr.setGeometry(QRect(0, -20, 1941, 1121))
        self.Backgr.setPixmap(QPixmap(u":/Wallpaper/assets/Wallpaper/7.png"))
        self.Principiante = QPushButton(MenuPrincipal)
        self.Principiante.setObjectName(u"Principiante")
        self.Principiante.setGeometry(QRect(90, 370, 321, 311))
        self.Principiante.setStyleSheet(u"background-color: transparent;\n"
"border: none;")
        icon = QIcon()
        icon.addFile(u":/images/assets/Images/19.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Principiante.setIcon(icon)
        self.Principiante.setIconSize(QSize(300, 300))
        self.Basico = QPushButton(MenuPrincipal)
        self.Basico.setObjectName(u"Basico")
        self.Basico.setGeometry(QRect(430, 370, 321, 311))
        self.Basico.setStyleSheet(u"background-color: transparent;\n"
"border: none;")
        icon1 = QIcon()
        icon1.addFile(u":/images/assets/Images/20.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Basico.setIcon(icon1)
        self.Basico.setIconSize(QSize(300, 300))
        self.Intermedio = QPushButton(MenuPrincipal)
        self.Intermedio.setObjectName(u"Intermedio")
        self.Intermedio.setGeometry(QRect(750, 370, 321, 311))
        self.Intermedio.setStyleSheet(u"background-color: transparent;\n"
"border: none;")
        icon2 = QIcon()
        icon2.addFile(u":/images/assets/Images/21.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Intermedio.setIcon(icon2)
        self.Intermedio.setIconSize(QSize(300, 300))
        self.Avanzado = QPushButton(MenuPrincipal)
        self.Avanzado.setObjectName(u"Avanzado")
        self.Avanzado.setGeometry(QRect(1070, 370, 321, 311))
        self.Avanzado.setStyleSheet(u"background-color: transparent;\n"
"border: none;")
        icon3 = QIcon()
        icon3.addFile(u":/images/assets/Images/22.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Avanzado.setIcon(icon3)
        self.Avanzado.setIconSize(QSize(300, 300))
        self.LblPrincipiante = QLabel(MenuPrincipal)
        self.LblPrincipiante.setObjectName(u"LblPrincipiante")
        self.LblPrincipiante.setEnabled(True)
        self.LblPrincipiante.setGeometry(QRect(160, 690, 271, 61))
        font = QFont()
        font.setFamilies([u"Baloo 2"])
        font.setPointSize(28)
        font.setBold(True)
        self.LblPrincipiante.setFont(font)
        self.LblPrincipiante.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.LblBasico = QLabel(MenuPrincipal)
        self.LblBasico.setObjectName(u"LblBasico")
        self.LblBasico.setEnabled(True)
        self.LblBasico.setGeometry(QRect(550, 690, 151, 61))
        self.LblBasico.setFont(font)
        self.LblBasico.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.LblIntermedio = QLabel(MenuPrincipal)
        self.LblIntermedio.setObjectName(u"LblIntermedio")
        self.LblIntermedio.setEnabled(True)
        self.LblIntermedio.setGeometry(QRect(810, 690, 241, 61))
        self.LblIntermedio.setFont(font)
        self.LblIntermedio.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.LblAvanzado = QLabel(MenuPrincipal)
        self.LblAvanzado.setObjectName(u"LblAvanzado")
        self.LblAvanzado.setEnabled(True)
        self.LblAvanzado.setGeometry(QRect(1170, 690, 211, 61))
        self.LblAvanzado.setFont(font)
        self.LblAvanzado.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.retranslateUi(MenuPrincipal)

        QMetaObject.connectSlotsByName(MenuPrincipal)
    # setupUi

    def retranslateUi(self, MenuPrincipal):
        MenuPrincipal.setWindowTitle(QCoreApplication.translate("MenuPrincipal", u"Form", None))
        self.Backgr.setText("")
        self.Principiante.setText("")
        self.Basico.setText("")
        self.Intermedio.setText("")
#if QT_CONFIG(tooltip)
        self.Avanzado.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.Avanzado.setText("")
        self.LblPrincipiante.setText(QCoreApplication.translate("MenuPrincipal", u"Principiante", None))
        self.LblBasico.setText(QCoreApplication.translate("MenuPrincipal", u"B\u00e1sico", None))
        self.LblIntermedio.setText(QCoreApplication.translate("MenuPrincipal", u"Intermedio", None))
        self.LblAvanzado.setText(QCoreApplication.translate("MenuPrincipal", u"Avanzado", None))
    # retranslateUi

