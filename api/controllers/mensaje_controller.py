from ..models.mensaje_model import Mensaje
from ..models.canal_model import Canal
from flask import request
from flask_jwt_extended import get_jwt_identity,jwt_required

class MensajeController:
    @classmethod
    @jwt_required()
    def crear_mensaje(cls,nombre_canal,mensaje):
        mensaje=mensaje
        id_usuario=get_jwt_identity()
        canal=Canal.get_canal(Canal(nombre_canal=nombre_canal))
        Mensaje.create_mensaje(mensaje,id_usuario,canal.id_canal)
        return {"message":"crear mensaje"}
    
    @classmethod
    @jwt_required()
    def mostrar_mensajes(cls,nombre_canal):
        #mostrar los mensajes del canal
        canal=Canal.get_canal(Canal(nombre_canal=nombre_canal))
        mensajes=Mensaje.get_messages(canal.id_canal)
        if mensajes is not None:
            return mensajes,200
        else:
            return{"message":"no hay mensajes"},404
        
    
    