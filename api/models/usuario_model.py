from ..database import DatabaseConnection
from .rol_usuario_model import RolUsuario

from flask import jsonify
class Usuario:
    """Modelo clase de usuario"""
    def __init__(self, 
                id_usuario = None,
                username = None, 
                contrasena = None, 
                email = None,
                nombre_usuario = None, 
                apellido_usuario = None,
                fecha_creacion = None,
                imagen_perfil = None
                ):
        """Constructor method"""
        self.id_usuario = id_usuario
        self.username = username
        self.contrasena = contrasena
        self.email = email
        self.nombre_usuario = nombre_usuario
        self.apellido_usuario = apellido_usuario
        self.fecha_creacion = fecha_creacion
        self.imagen_perfil = imagen_perfil
        
    
    def serialize(self):
        return {
            "id_usuario": self.id_usuario,
            "username": self.username,
            "contrasena":self.contrasena,
            "email": self.email,
            "nombre_usuario": self.nombre_usuario,
            "apellido_usuario": self.apellido_usuario,
            "fecha_creacion": self.fecha_creacion,
            "imagen_perfil": self.imagen_perfil
            }
    
    
    @classmethod
    def is_registered(cls, usuario):
        query = """SELECT id_usuario FROM proyecto_bdd.usuarios 
        WHERE username = %(username)s and contrasena = %(contrasena)s"""
        param = usuario.__dict__
        result = DatabaseConnection.fetch_one(query, params=param)
        if result is not None:
            return True
        return False
    
    @classmethod
    def get(cls, user):
        #consigue segun el username
        query = """SELECT * FROM proyecto_bdd.usuarios 
        WHERE username = %(username)s ;"""
        params = user.__dict__
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return cls(
                id_usuario = result[0],
                username = result[1],
                contrasena = result[2],
                email = result[3],
                nombre_usuario = result[4],
                apellido_usuario = result[5],
                fecha_creacion = result[6],
                imagen_perfil = result[7]
            )
        return None
    
    @classmethod
    def create_usuario(cls, usuarios):
        #crea/registra un nuevo usuario
        query = """INSERT INTO proyecto_bdd.usuarios (username,contrasena,email,nombre_usuario,apellido_usuario,imagen_perfil) 
        VALUES (%s, %s, %s, %s, %s, %s);"""
        params = usuarios.username, usuarios.contrasena, usuarios.email, usuarios.nombre_usuario,usuarios.apellido_usuario,  usuarios.imagen_perfil
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def update_usuario(cls,campo,valor,id_usuario):
        query= f"UPDATE proyecto_bdd.usuarios SET usuarios.{campo} = '{valor}' WHERE id_usuario = {id_usuario}"
        
        result = DatabaseConnection.execute_query(query)

        if result is not None:
            return True
        return False
    
    @classmethod
    def get_user_id(cls, user):
        query = """SELECT * FROM proyecto_bdd.usuarios 
        WHERE id_usuario = %(id_usuario)s;"""
        params = user.__dict__
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return cls(
                id_usuario = result[0],
                username = result[1],
                contrasena = result[2],
                email = result[3],
                nombre_usuario = result[4],
                apellido_usuario = result[5],
                fecha_creacion = result[6],
                imagen_perfil = result[7],
            )
        return None