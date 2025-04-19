# Este archivo se usa para declarar las funciones que se usarán en los ejercicios
from conexion_BD import BD
def incializarEJ(self):
    BorrarLetras(self)
    self.ui.Siguiente.setEnabled(False)

def BorrarLetras(self):
    self.ui.Letra1.setText("")
    self.ui.Letra2.setText("")
    self.ui.Letra3.setText("")
    self.ui.Retroalimentacion.setText("")

def Correccion(self, letra1, letra2, letra3):
    errores = Corregir(self, letra1, letra2, letra3)
    if(errores>0):
        self.ui.Retroalimentacion.setText(f"Tienes  {errores} errores por corregir")
    else:
        Correcto(self)

def Corregir(self, letra1, letra2, letra3):
    LimpiarEstilos(self)
    errores = 0
    if(self.ui.Letra1.text()!=letra1):
        self.ui.Letra1.setStyleSheet("color: red;")
        errores+=1

    if(self.ui.Letra2.text()!=letra2):
        self.ui.Letra2.setStyleSheet("color: red;")
        errores+=1

    if(self.ui.Letra3.text()!=letra3):
        self.ui.Letra3.setStyleSheet("color: red;")
        errores+=1
    return errores

def Correcto(self):
    LimpiarEstilos(self)
    self.ui.Letra1.setStyleSheet("color: green;")
    self.ui.Letra2.setStyleSheet("color: green;")
    self.ui.Letra3.setStyleSheet("color: green;")
    self.ui.Retroalimentacion.setText("Correcto!!!")
    self.ui.Siguiente.setEnabled(True)

def AsignarLetras(self, letra1, letra2, letra3):
    with BD() as db:
        letras = db.leerUlt3Registros()

        if len(letras) == 3:
            self.ui.Letra1.setText(str(letras[0][0]))
            self.ui.Letra2.setText(str(letras[1][0]))
            self.ui.Letra3.setText(str(letras[2][0]))
            Correccion(self,letra1, letra2, letra3)
        else:
            print("No se obtuvieron 3 letras de la base de datos.")

def LimpiarEstilos(self):
    self.ui.Letra1.setStyleSheet("")
    self.ui.Letra2.setStyleSheet("")
    self.ui.Letra3.setStyleSheet("")
