# This Python file uses the following encoding: utf-8
import sys
import os
import resources_rc
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PySide6.QtGui import QFontDatabase, QFont
from conexion_BD import BD

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
        self.label = QLabel(self)
        self.label.setScaledContents(True)  # Escalar imagen
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.label)
        self.setLayout(layout)

        # Fuente personalizada
        font_path = os.path.join(os.path.dirname(__file__), "fonts", "Baloo2-Bold.ttf")
        font_id = QFontDatabase.addApplicationFont(font_path)
        if font_id != -1:
            family = QFontDatabase.applicationFontFamilies(font_id)[0]
            app_font = QFont(family, 12)
            self.setFont(app_font)
        else:
            print("No se pudo cargar la fuente personalizada.")



if __name__ == "__main__":
    app = QApplication(sys.argv)

    """
    bd = BD()
    with BD() as db:
            print("Última letra insertada:", db.leerUltRegistro())
            print("Insertando letra con ID 5 (E):", db.insertarRegistro(5))
            print("Última letra insertada:", db.leerUltRegistro())
    """

    widget = Widget()
    widget.show()
    sys.exit(app.exec())
