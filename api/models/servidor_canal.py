from ..database import DatabaseConnection

class ServidorCanal:
    """Modelo clase de ServidorCanal"""
    def __init__(self, 
                id_servidor_canal = None,
                id_servidor = None, 
                id_canal = None
                ):
        """Constructor method"""
        self.id_servidor_canal = id_servidor_canal
        self.id_servidor = id_servidor
        self.id_canal = id_canal
    
    def serialize(self):
        return {
            "id_servidor_canal": self.id_servidor_canal,
            "id_servidor": self.id_servidor,
            "id_canal":self.id_canal
        }
    
    @classmethod
    def add(cls,canal):
        query = """INSERT INTO proyecto_bdd.servidor_canal (id_usuario,id_servidor,id_canal)
        VALUES (%s, %s, %s);"""
        params = canal.id_usuario, canal.id_servidor, canal.id_rol
        result = DatabaseConnection.execute_query(query, params=params)
        if result is not None:
            return True
        else:
            return False
        """if result is not None:
            return cls(
                id_usuario_servidor = result[0],
                id_usuario = result[1],
                id_servidor = result[2],
                id_rol = result[3]
            )
        else:
            return None
        """
    