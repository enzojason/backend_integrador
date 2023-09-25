from ..database import DatabaseConnection
import datetime

class Mensaje:
    """Modelo clase de usuario"""
    def __init__(self, 
                id_mensaje = None,
                mensaje = None, 
                fecha = None, 
                id_usuario = None,
                id_canal=None
                ):
        """Constructor method"""
        self.id_mensaje = id_mensaje
        self.mensaje = mensaje
        self.fecha = fecha
        self.id_usuario = id_usuario
        self.id_canal = id_canal
       
    def serialize(self):
        return {
            "id_mensaje": self.id_mensaje,
            "mensaje": self.mensaje,
            "fecha": self.fecha,
            "id_usuario": self.id_usuario,
            "id_canal": self.id_canal
        }
    
    @classmethod
    def create_mensaje(cls,mensaje,id_usuario,id_canal):
        #crea/registra un mensaje en la bdd
        query = """INSERT INTO proyecto_bdd.mensajes (mensaje,id_usuario,id_canal) VALUES (%s,%s,%s);"""
        params=mensaje,id_usuario,id_canal,
        DatabaseConnection.execute_query(query,params)
    
    @classmethod
    def get_messages(cls,id_canal):
        #obtiene todos los mensajes de un canal
        query=f"SELECT mensajes.id_mensaje,usuarios.username,mensajes.fecha,mensajes.mensaje FROM proyecto_bdd.mensajes INNER JOIN proyecto_bdd.usuarios ON mensajes.id_usuario = usuarios.id_usuario WHERE mensajes.id_canal = {id_canal} ORDER BY mensajes.fecha ASC; "
        #query=f"SELECT mensajes.id_mensaje,usuarios.username,mensajes.fecha,mensajes.mensaje,canales.descripcion FROM ((proyecto_bdd.mensajes INNER JOIN proyecto_bdd.usuarios ON mensajes.id_usuario = usuarios.id_usuario) INNER JOIN proyecto_bdd.canales ON mensajes.id_canal=canales.id_canal) WHERE mensajes.id_canal = {id_canal} ORDER BY mensajes.fecha ASC; "
        result = DatabaseConnection.fetch_all(query)
        mensajes=[]
        
        for id_mensaje,username,fecha,mensaje in result:
            mensajes.append({
                "id_mensaje" : id_mensaje,
                "username" : username,
                "dia" : fecha.strftime("%d %b,%y"),
                "hora" : fecha.strftime("%H:%M"),
                "mensaje" : mensaje,

            })
        if len(mensajes) == 0:
            return None
        else:
            return mensajes
        
        