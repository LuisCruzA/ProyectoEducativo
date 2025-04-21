from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton
from conexion_BD import BD

class InputTesting(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simulador de Datos")
        self.setFixedSize(200, 150)

        self.layout = QVBoxLayout(self)

        self.input1 = QLineEdit()
        self.btn_enviar = QPushButton("Enviar Datos")
        self.layout.addWidget(self.input1)
        self.layout.addWidget(self.btn_enviar)

        self.btn_enviar.clicked.connect(lambda: self.enviar_datos())

    def enviar_datos(self):
        letra = self.input1.text().upper()

        letras_validas = {
            'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,
            'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
            'K': 11, 'L': 12, 'M': 13, 'N': 14, 'Ñ': 15,
            'O': 16, 'P': 17, 'Q': 18, 'R': 19, 'S': 20,
            'T': 21, 'U': 22, 'V': 23, 'W': 24, 'X': 25,
            'Y': 26, 'Z': 27
        }

        if letra in letras_validas:
            numero = letras_validas[letra]

            with BD() as db:
                exito = db.insertarRegistro(numero)
                if exito:
                    print("Dato insertado correctamente")
                else:
                    print("Error al insertar el dato")
        else:
            print("Entrada no válida. Ingresa una sola letra A-Z.")

