# Este archivo se usa para declarar las funciones que se usarán en los ejercicios
from conexion_BD import BD
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QUrl
import random

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
    else:
        self.ui.Letra1.setStyleSheet("color: green;")

    if(self.ui.Letra2.text()!=letra2):
        self.ui.Letra2.setStyleSheet("color: red;")
        errores+=1
    else:
        self.ui.Letra2.setStyleSheet("color: green;")

    if(self.ui.Letra3.text()!=letra3):
        self.ui.Letra3.setStyleSheet("color: red;")
        errores+=1
    else:
        self.ui.Letra3.setStyleSheet("color: green;")

    if (errores > 0):
        audios_error = [
                   "qrc:/Audios/assets/Audios/MALO1.mp3",
                   "qrc:/Audios/assets/Audios/MALO2.mp3",
                   "qrc:/Audios/assets/Audios/MALO3.mp3",
                   "qrc:/Audios/assets/Audios/MALO4.mp3",
                   "qrc:/Audios/assets/Audios/MALO5.mp3"
               ]
        audio_aleatorio = random.choice(audios_error)
        reproducir_mp3(self, audio_aleatorio)
    return errores

def Correcto(self):
    self.ui.Retroalimentacion.setText("Correcto!!!")
    audios_correcto = [
               "qrc:/Audios/assets/Audios/BUENO1.mp3",
               "qrc:/Audios/assets/Audios/BUENO2.mp3",
               "qrc:/Audios/assets/Audios/BUENO3.mp3",
               "qrc:/Audios/assets/Audios/BUENO4.mp3",
               "qrc:/Audios/assets/Audios/BUENO5.mp3",
               "qrc:/Audios/assets/Audios/BUENO6.mp3",
               "qrc:/Audios/assets/Audios/BUENO7.mp3",
               "qrc:/Audios/assets/Audios/BUENO8.mp3"
           ]
    audio_aleatorio = random.choice(audios_correcto)
    reproducir_mp3(self, audio_aleatorio)
    self.ui.Siguiente.setEnabled(True)

def AsignarLetras(self, letra1, letra2, letra3):
    with BD() as db:
        letras = db.leerUlt3Registros()

        if len(letras) == 3:
            self.ui.Letra1.setText(str(letras[2][0]))
            self.ui.Letra2.setText(str(letras[1][0]))
            self.ui.Letra3.setText(str(letras[0][0]))
            Correccion(self,letra1, letra2, letra3)
        else:
            print("No se obtuvieron 3 letras de la base de datos.")

def LimpiarEstilos(self):
    self.ui.Letra1.setStyleSheet("")
    self.ui.Letra2.setStyleSheet("")
    self.ui.Letra3.setStyleSheet("")

def CambiarPantalla(self, pantalla):
    self.stack.setCurrentIndex(pantalla)

def reproducir_mp3(self, ruta):
    self.audio_output = QAudioOutput()
    self.player = QMediaPlayer()
    self.player.setAudioOutput(self.audio_output)
    self.player.setSource(QUrl(ruta))
    self.audio_output.setVolume(0.8)
    self.player.play()
