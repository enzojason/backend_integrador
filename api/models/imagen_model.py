from ..database import DatabaseConnection

class Imagen:
    @classmethod
    def update_imagen(cls, valor,id_usuario):
        #actauliza la imagen de perfil de un usuario
        query = """UPDATE proyecto_bdd.usuarios SET usuarios.imagen_perfil=%s WHERE id_usuario=%s;"""
        params = valor,id_usuario,
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def load_imagen(cls,id_usuario):
        #devuelve la imagen de perfil del usuario
        query = """SELECT imagen_perfil FROM proyecto_bdd.usuarios WHERE id_usuario=%s;"""
        params = id_usuario,
        result=DatabaseConnection.fetch_one(query, params=params)
        return result[0] 
    
