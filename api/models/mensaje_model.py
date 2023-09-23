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
        result = DatabaseConnection.fetch_all(query)
        mensajes=[]
        print("RESULT ",result)
        if result is not None and len(mensajes)!= 0:
            for id_mensaje,username,fecha,mensaje in result:
                mensajes.append({
                    "id_mensaje" : id_mensaje,
                    "username" : username,
                    "dia" : fecha.strftime("%d %b,%y"),
                    "hora" : fecha.strftime("%H:%M"),
                    "mensaje" : mensaje
                })
            #print(list(map(lambda x: x.strftime("%d"),fechas)))
            return mensajes
        else:
            return None
        
        """if result is not None:
            return cls(
            id_mensaje = result[0],
            mensaje = result[1],
            fecha = result[2],
            hora = result[3],
            id_usuario = result[4],
            id_canal = result[5]
            )"""