from ..database import DatabaseConnection

class Servidor:
    """Modelo clase de usuario"""
    def __init__(self, 
                id_servidor = None,
                nombre_servidor = None, 
                fecha_creacion = None,
                id_administrador = None
                ):
        """Constructor method"""
        self.id_servidor = id_servidor
        self.nombre_servidor = nombre_servidor
        self.fecha_creacion = fecha_creacion
        self.id_administrador = id_administrador

    def serialize(self):
        return {
            "id_servidor": self.id_servidor,
            "nombre_servidor": self.nombre_servidor,
            "fecha_creacion": self.fecha_creacion,
            "id_administrador": self.id_administrador
                }
    
    @classmethod
    def create_servidor(cls,nombre,id_administrador):
        #crea/registra un servidor
        query = """INSERT INTO proyecto_bdd.servidores (nombre_servidor,id_administrador) VALUES (%s,%s);"""
        params=nombre,id_administrador,
        DatabaseConnection.fetch_one(query,params)
        
        
    @classmethod
    def get(cls, servidor):
        #consigue un objeto segun el del nombre_servidor
        query = """SELECT * FROM proyecto_bdd.servidores 
        WHERE nombre_servidor = %(nombre_servidor)s ;"""
        params = servidor.__dict__
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return cls(
                id_servidor = result[0],
                nombre_servidor = result[1],
                fecha_creacion = result[2],
                id_administrador = result[3]
            )
        else:
            return None
        
    