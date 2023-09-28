from ..models.mensaje_model import Mensaje
from ..models.canal_model import Canal
from ..models.servidor_model import Servidor

from flask import request
from flask_jwt_extended import get_jwt_identity,jwt_required

class MensajeController:
    @classmethod
    @jwt_required()
    def crear_mensaje(cls,id_canal,mensaje):
        mensaje=mensaje
        id_usuario=get_jwt_identity()
        Mensaje.create_mensaje(mensaje,id_usuario,id_canal)
        mensajes=Mensaje.get_messages(id_canal)
        if mensajes is not None:
            return mensajes,200
        else:
            return{"message":"no hay mensajes"},404
    
    @classmethod
    @jwt_required()
    def mostrar_mensajes(cls,id_canal):
        #mostrar los mensajes del canal

        canal=Canal.get_canal(Canal(id_canal=id_canal))
        mensajes=Mensaje.get_messages(id_canal)
        
        if mensajes is not None:
            return {"mensajes":mensajes,
                    "nombre_canal":canal.nombre_canal,
                    "descripcion":canal.descripcion,
                    "fecha_creacion":canal.fecha_creacion
                    },200
        else:
            return{"nombre_canal":canal.nombre_canal,
                    "descripcion":canal.descripcion,
                    "fecha_creacion":canal.fecha_creacion,
                    "message":"no hay mensajes"
                    },404
    
    @classmethod
    @jwt_required()
    def modificar_mensaje(cls,id_mensaje,mensaje):
        id_usuario=get_jwt_identity()
        mensaje_obj=Mensaje.get_message_id(Mensaje(id_mensaje=id_mensaje))
        
        if (mensaje_obj.id_usuario==id_usuario):
            Mensaje.upload_message(mensaje,id_mensaje)
            return {"message":"modificado"},200
        
        else:
            return {"message":"solo puede modificar mensajes propios"},401

    