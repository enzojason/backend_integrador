from ..database import DatabaseConnection
from flask import jsonify
class Canal:
    """Modelo clase de canal"""
    def __init__(self, 
                id_canal = None,
                nombre_canal = None, 
                fecha_creacion = None,
                descripcion = None,
                id_servidor  = None,):
        "Constructor"
        self.id_canal = id_canal
        self.nombre_canal = nombre_canal
        self.fecha_creacion = fecha_creacion
        self.descripcion = descripcion
        self.id_servidor = id_servidor
    def serialize(self):
        return {
            "id_canal": self.id_canal,
            "nombre_canal": self.nombre_canal,
            "fecha_creacion": self.fecha_creacion,
            "descripcion" :self.descripcion,
            "id_servidor" : self.id_servidor
                }
    
    @classmethod
    def create_canal(cls,nombre,descripcion,id_servidor):
        #crea/registra un canal
        query = """INSERT INTO proyecto_bdd.canales (nombre_canal,descripcion,id_servidor) VALUES (%s,%s,%s);"""
        params=nombre,descripcion,id_servidor
        result = DatabaseConnection.execute_query(query,params)
        if result is not None:
            return result
        else:
            return None
        
    @classmethod
    def get_canals(cls,id_servidor):
        #obtiene lista de nombres de canales, que pertenece a un servidor
        query = f"SELECT nombre_canal,fecha_creacion,descripcion FROM proyecto_bdd.canales WHERE canales.id_servidor = {id_servidor};"
        result = DatabaseConnection.fetch_all(query)
        canales=[]
        if result is not None:
            for nombre,fecha,descripcion in result:
                canales.append(nombre)
            return canales
        else:
            return None
        
    @classmethod
    def get_canal(cls,canal):
        #consigue el canal segun el nombre del canal
        query = """SELECT id_canal,nombre_canal,fecha_creacion,descripcion,id_servidor FROM proyecto_bdd.canales 
        WHERE nombre_canal = %(nombre_canal)s ;"""
        params = canal.__dict__ 
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return cls(
                id_canal = result[0],
                nombre_canal = result[1], 
                fecha_creacion = result[2],
                descripcion = result[3],
                id_servidor  = result[4],
            )
        else:
            return None
        
        