# Este archivo se usa para la conexión con la BD (PostgreSQL - Railway)
import psycopg2

class BD:
    def __init__(self):
        self.conn = psycopg2.connect(
            host="switchback.proxy.rlwy.net",
            database="railway",
            port='26531',
            user="postgres",
            password="NEQeVpJyeryGWYTgCXVTgRkGCtdYUguV"
        )
        self.cursor = self.conn.cursor()

    def execute(self, query, params=()):
            self.cursor.execute(query, params)
            self.conn.commit()
            return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def insertarRegistro(self, letra): #Numero de la letra
        query = "INSERT INTO Registros(letraID) VALUES (%s)"
        try:
            self.cursor.execute(query, (letra,))
            self.conn.commit()
            return True
        except Exception as e:
            print("Error al insertar: ", e)
            self.conn.rollback()
            return False

    def leerUltRegistro(self): #Lee el ultimo registro
        query = "SELECT b.letra FROM Registros r JOIN Bloques b ON r.letraID = b.id ORDER BY id LIMIT 1"
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Exception as e:
            print("Error al leer: ", e)
            return []

    def leerUlt3Registros(self): #Lee el ultimo registro
        query = "SELECT b.letra FROM Registros r JOIN Bloques b ON r.letraID = b.id ORDER BY registro_id DESC LIMIT 3"
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Exception as e:
            print("Error al leer: ", e)
            return []

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
