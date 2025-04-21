# This Python file uses the following encoding: utf-8
import sys
import os
import resources_rc
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QStackedWidget, QPushButton
from PySide6.QtGui import QFontDatabase, QFont, QCursor
from PySide6.QtCore import Qt, QEvent
from conexion_BD import BD
from funciones_EJ import AsignarLetras, incializarEJ, CambiarPantalla, reproducir_mp3

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py

from InputTest import InputTesting
from ui_form import Ui_Widget
from ui_menu_principal import Ui_MenuPrincipal
from ui_form2 import Ui_Form2

class Widget(QWidget):
    def __init__(self, stack):
        super().__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.stack = stack

        # Pantalla completa
        self.showFullScreen()

        # Fuente personalizada
        font_path = os.path.join(os.path.dirname(__file__), "fonts", "Baloo2-Bold.ttf")
        font_id = QFontDatabase.addApplicationFont(font_path)
        if font_id != -1:
            family = QFontDatabase.applicationFontFamilies(font_id)[0]
            app_font = QFont(family, 12)
            self.setFont(app_font)
        else:
            print("No se pudo cargar la fuente personalizada.")

        #Botón Salir
        self.ui.Salir.clicked.connect(stack.close)
        self.ui.Salir.setCursor(QCursor(Qt.PointingHandCursor))
        self.ui.Salir.setStyleSheet("""
                        QPushButton {
                        background-color: transparent;
                        border: none;
                    }

                        QPushButton:hover {
                        background-color: transparent;
                        border: none;
                        padding-bottom: 5px;
                        padding-top: 15px;
                    }""")
        #Botón Revisar
        self.ui.Revisar.setCursor(QCursor(Qt.PointingHandCursor))
        self.ui.Revisar.setStyleSheet("""
                        QPushButton {
                        background-color: transparent;
                        border: none;
                    }

                        QPushButton:hover {
                        background-color: transparent;
                        border: none;
                        padding-bottom: 5px;
                        padding-top: 15px;
                    }


                    """)
        self.ui.Revisar.clicked.connect(lambda:AsignarLetras(self,'S', 'O', 'L'))
        #Botón Audio
        self.ui.Audio.setCursor(QCursor(Qt.PointingHandCursor))
        self.ui.Audio.setStyleSheet("""
                        QPushButton {
                        background-color: transparent;
                        border: none;
                    }

                        QPushButton:hover {
                        background-color: transparent;
                        border: none;
                        padding-bottom: 5px;
                        padding-top: 15px;
                    }


                    """)
        self.ui.Audio.clicked.connect(lambda:reproducir_mp3(self, "qrc:/Audios/assets/Audios/SOL.mp3"))
        #Botón Siguiente
        self.ui.Siguiente.setCursor(QCursor(Qt.PointingHandCursor))
        self.ui.Siguiente.setStyleSheet("""
                        QPushButton {
                        background-color: transparent;
                        border: none;
                    }

                        QPushButton:hover {
                        background-color: transparent;
                        border: none;
                        padding-bottom: 5px;
                        padding-top: 15px;
                    }


                    """)
        self.ui.Siguiente.clicked.connect(lambda:CambiarPantalla(self, 2))
        incializarEJ(self)

class MenuPrincipal(QWidget):
    def __init__(self, stack):
        super().__init__()
        self.ui = Ui_MenuPrincipal()
        self.ui.setupUi(self)
        self.stack = stack

        self.botones_con_labels = {
            self.ui.Principiante: self.ui.LblPrincipiante,
            self.ui.Basico: self.ui.LblBasico,
            self.ui.Intermedio: self.ui.LblIntermedio,
            self.ui.Avanzado: self.ui.LblAvanzado
        }

        for boton, label in self.botones_con_labels.items():
            boton.setCursor(QCursor(Qt.PointingHandCursor))
            boton.installEventFilter(self)
            label.hide()
            boton.setStyleSheet("""
                QPushButton {
                    background-color: transparent;
                    border: none;
                }
                QPushButton:hover {
                    background-color: transparent;
                    border: none;
                    padding-bottom: 5px;
                    padding-top: 15px;
                }
            """)
        self.ui.Basico.clicked.connect(lambda:CambiarPantalla(self, 1))

    def eventFilter(self, source, event):
        if source in self.botones_con_labels:
            label = self.botones_con_labels[source]
            if event.type() == QEvent.Enter:
                label.show()
            elif event.type() == QEvent.Leave:
                label.hide()
        return super().eventFilter(source, event)

class Ejercicio2(QWidget):
    def __init__(self, stack):
        super().__init__()
        self.ui = Ui_Form2()
        self.ui.setupUi(self)
        self.stack = stack

if __name__ == "__main__":
    app = QApplication(sys.argv)

    """
    with BD() as db:
            print("Insertando letra con ID 20 (S):", db.insertarRegistro(8))
            print("Insertando letra con ID 16 (O):", db.insertarRegistro(4))
            print("Insertando letra con ID 12 (L):", db.insertarRegistro(15))
    """

    #Stack para cambiar de pantallas
    stack = QStackedWidget()
    MenuP = MenuPrincipal(stack)
    widget = Widget(stack)
    Ej2 = Ejercicio2(stack)

    stack.addWidget(MenuP)
    stack.addWidget(widget)
    stack.addWidget(Ej2)

    stack.setCurrentIndex(0)
    stack.showFullScreen()
    stack.show()

    """
    simulador = InputTesting()
    simulador.show()
    """
    sys.exit(app.exec())
