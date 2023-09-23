from ..database import DatabaseConnection

class RolUsuario:

    def __init__(self, **kwargs):
        self.rol_id = kwargs.get('rol_id')
        self.nombre_rol = kwargs.get('nombre_rol')

    def serialize(self):
        return {
            "rol_id": self.rol_id,
            "nombre_rol": self.nombre_rol
        }
    
    @classmethod
    def get(cls, rol):
        query = """SELECT rol_id, nombre_rol FROM proyecto_bdd.rol_usuario WHERE rol_id = %(rol_id)s"""
        params = rol.__dict__
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return RolUsuario(
                rol_id = result[0],
                nombre_rol = result[1]
            )
        return None