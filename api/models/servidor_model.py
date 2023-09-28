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
        
    @classmethod
    def search_all(cls,nombre):
        #buscar y devuelve todos los servidores que coincidan con el nombre
        query=f"SELECT servidores.nombre_servidor, COUNT(usuario_servidor.id_usuario_servidor) as cantidad_usuarios FROM servidores INNER JOIN usuario_servidor on servidores.id_servidor =usuario_servidor.id_servidor WHERE servidores.nombre_servidor LIKE '{nombre}%' GROUP BY nombre_servidor;"
        result = DatabaseConnection.fetch_all(query,nombre)
        resultado=[]
        for nombre,cantidad in result:
            resultado.append({
                "nombre_servidor":nombre,
                "cantidad_usuarios":cantidad
                }
                )
        if len(resultado) == 0:
            return None
        else:
            return resultado