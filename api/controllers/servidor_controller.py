from flask import request
from ..models.servidor_model import Servidor
from ..models.usuario_servidor_model import UsuarioServidor
from flask_jwt_extended import jwt_required,get_jwt_identity

class ServidorController:
    @classmethod
    @jwt_required()
    def create(cls,nombre_servidor):
        #el id_administrador es el mismo id_usuario de quien se encuentra la sesion activa
        id_administrador=get_jwt_identity()
        Servidor.create_servidor(nombre_servidor,id_administrador)
        user = Servidor.get(Servidor(nombre_servidor=nombre_servidor))
        usuario=UsuarioServidor(
            id_usuario=id_administrador,
            id_servidor=user.id_servidor,
            id_rol=1
        )
        a=UsuarioServidor.add(usuario)
        return {"message": "servidor creado con exito"},200
    
    @classmethod
    @jwt_required()
    def join(cls,nombre_servidor):
        id_usuario=get_jwt_identity()
        serv=Servidor.get(Servidor(nombre_servidor=nombre_servidor))
        if serv is None:
            return {"message":"servidor no encontrado"}, 404
        else:
            usuario=UsuarioServidor(
            id_usuario=id_usuario,
            id_servidor=serv.id_servidor,
            id_rol=0)
            UsuarioServidor.add(usuario)
            return {"message":"unido con exito"} ,200

    @classmethod
    @jwt_required()
    def mostrar_servidores(cls):
        id_usuario=get_jwt_identity()
        result=UsuarioServidor.get_servers(id_usuario)
        if result is not None: 
            return { "servidores": result }, 200
        else:
            return {"message":"no existen servidores"},404
        
    @classmethod
    def buscar_servidor(cls,nombre):
        servidores=Servidor.search_all(nombre)
        if servidores is not None:
            return {"servidores":servidores},200
        else:
            return {"message":"no hay servidores encontrados"},404