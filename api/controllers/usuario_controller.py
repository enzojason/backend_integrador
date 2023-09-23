from ..models.usuario_model import Usuario
from flask import request
from flask_jwt_extended import create_access_token,get_jwt_identity,jwt_required


class UsuarioController:
    @classmethod
    def login(cls):
        data = request.json
        user = Usuario(
            username = data.get('username'),
            contrasena = data.get('contrasena')
        )
        if Usuario.is_registered(user):
            username = data.get('username')
            user = Usuario.get(Usuario(username=username))
            access_token = create_access_token(identity=user.id_usuario)
            return { "token": access_token, "id_usuario": user.id_usuario }, 200
        else:
            return {"message": "Usuario o contraseña incorrectos"}, 401

    @classmethod
    @jwt_required()
    def show_profile(cls):
        print("La función getProfile se ha ejecutado.")
        id_usuario = get_jwt_identity()
        print("SESION PROFILE ", id_usuario)
        user = Usuario.get_user_id(Usuario(id_usuario=id_usuario))
        if user is None:
            return {"message": "Usuario no encontrado"}, 404
        else:
            return user.serialize(), 200

    """@classmethod
    @jwt_required()
    def logout(cls):
        resp = jsonify(message='Cierre de sesión exitoso')
        unset_jwt_cookies(resp)
        return resp, 200"""
    
    @classmethod
    def create(cls):
        #crea un nuevo usuario
        data=request.json
        user = Usuario(
            username = data.get('username'),
            contrasena = data.get('contrasena'),
            email = data.get('email'),
            nombre_usuario = data.get('nombre'),
            apellido_usuario = data.get('apellido'),
            imagen_perfil= "/static/imagenes/foto_de_perfil.png"
            #el id rol y la imagen de perfil van por defecto
            )
        Usuario.create_usuario(user)
        return user.serialize(),201
    
    @classmethod
    @jwt_required()
    def update_profile(cls):
        print("La función update_profile se ha ejecutado.")
        id_usuario = get_jwt_identity()
        data=request.json

        #verifica cada uno, y sube a la bdd
        if 'username' in data:
            username = data.get('username')
            Usuario.update_usuario('username',username,id_usuario)

        if 'contrasena' in data:
            contrasena = data.get('contrasena')
            Usuario.update_usuario('contrasena',contrasena,id_usuario)

        if 'nombre_usuario' in data:
            nombre_usuario = data.get('nombre_usuario')
            Usuario.update_usuario('nombre_usuario',nombre_usuario,id_usuario)

        if 'apellido_usuario' in data:
            apellido_usuario = data.get('apellido_usuario')
            Usuario.update_usuario('apellido_usuario',apellido_usuario,id_usuario)

        if 'email' in data:
            email = data.get('email')
            Usuario.update_usuario('email',email,id_usuario)

        return {"actualizado":"exitosos"},200