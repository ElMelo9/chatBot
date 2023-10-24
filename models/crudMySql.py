import mysql.connector
from datetime import datetime


class MySQL:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='chatbot'
        )
        self.cursor = self.connection.cursor()
        print("db conectada!")

    def close(self):
        self.connection.close()
        print("db desconectada!")

    def insert_usuario(self, data):
        query = """
            INSERT INTO usuarios (id_tipoDoc, doc_usuario, nombre_usuario, email_usuario, telefono_usuario)
            VALUES (%s, %s, %s, %s, %s)
        """
        values = (
            data['id_tipoDoc'],
            data['doc_usuario'],
            data['nombre_usuario'],
            data['email_usuario'],
            data['telefono_usuario']
        )
        self.cursor.execute(query, values)
        self.connection.commit()
        print("insert usario done!")

    def insert_historial_chat(self, id_usuario, conversation_history):
        fecha_historialChat = datetime.now().date()
        query = """
            INSERT INTO historialChat (id_usuario, fecha_historialChat, chat_usuario)
            VALUES (%s, %s, %s)
        """
        for chat_entry in conversation_history:
            fecha_historialChat
            values = (id_usuario, fecha_historialChat, chat_entry)
            self.cursor.execute(query, values)
        self.connection.commit()
        print("insert_historial_chat done!")

    def get_id_usuario(self, nombre):
        query = "SELECT id_usuario FROM usuarios WHERE nombre_usuario = %s"
        self.cursor.execute(query, (nombre,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            return 0  

    def get_fechasHistorial(self):
        query = "SELECT DISTINCT fecha_historialChat FROM historialchat"
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        
        # Procesar los resultados en una lista
        fechas_historial = [result[0] for result in results]
        
        return fechas_historial 
    
    def get_usuariosHistorial(self):
        query = "SELECT DISTINCT nombre_usuario from historialchat as a INNER JOIN usuarios as b on a.id_usuario=b.id_usuario "
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        
        # Procesar los resultados en una lista
        usuarios_historial = [result[0] for result in results]
        
        return usuarios_historial  
    

    def get_historialChat(self, nombre,fecha):
        query = "SELECT chat_usuario from historialchat as a INNER JOIN usuarios as b on a.id_usuario=b.id_usuario WHERE fecha_historialChat= %s and nombre_usuario= %s"
        self.cursor.execute(query, (fecha,nombre,))
        results = self.cursor.fetchall()
        # Procesar los resultados en una lista
        historialChat = [result[0] for result in results]  

        return historialChat  
    