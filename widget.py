# This Python file uses the following encoding: utf-8
import sys
import os
import resources_rc
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PySide6.QtGui import QFontDatabase, QFont, QCursor
from PySide6.QtCore import Qt
from conexion_BD import BD
from funciones_EJ import AsignarLetras, incializarEJ

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

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
        self.ui.Salir.clicked.connect(self.close)
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
                    }""")
        self.ui.Revisar.clicked.connect(lambda:AsignarLetras(self,'S', 'O', 'L'))



if __name__ == "__main__":
    app = QApplication(sys.argv)

    """
    with BD() as db:
            print("Insertando letra con ID 20 (S):", db.insertarRegistro(8))
            print("Insertando letra con ID 16 (O):", db.insertarRegistro(4))
            print("Insertando letra con ID 12 (L):", db.insertarRegistro(15))
    """

    widget = Widget()
    incializarEJ(widget)
    widget.show()
    sys.exit(app.exec())
