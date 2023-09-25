from ..database import DatabaseConnection
class UsuarioServidor():
    """Modelo clase de UsuarioServidor"""
    def __init__(self, 
                id_usuario_servidor = None,
                id_usuario = None, 
                id_servidor = None, 
                id_rol = None
                ):
        """Constructor method"""
        self.id_usuario_servidor = id_usuario_servidor
        self.id_usuario = id_usuario
        self.id_servidor = id_servidor
        self.id_rol = id_rol
    
    def serialize(self):
        return {
            "id_usuario_servidor": self.id_usuario_servidor,
            "id_usuario": self.id_usuario,
            "id_servidor":self.id_servidor,
            "id_rol": self.id_rol
        }
    
    @classmethod
    def add(cls,serv):
        query = """INSERT INTO proyecto_bdd.usuario_servidor (id_usuario,id_servidor,id_rol)
        VALUES (%s, %s, %s);"""
        params = serv.id_usuario, serv.id_servidor, serv.id_rol
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
    
    @classmethod
    def get_servers(cls,id_usuario):
        #consigue los servidores a los que pertenece segun el id_usuario
        query=f"SELECT servidores.nombre_servidor FROM servidores INNER JOIN usuario_servidor ON servidores.id_servidor = usuario_servidor.id_servidor WHERE usuario_servidor.id_usuario = {id_usuario}; "
        result = DatabaseConnection.fetch_all(query)
        servidores=[]
        if result is not None:
            for results in result:
                for servers in results:
                    servidores.append(servers)
            return servidores
        else:
            return None