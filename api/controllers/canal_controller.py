from flask import request
from ..models.canal_model import Canal
from ..models.servidor_canal import ServidorCanal
from ..models.servidor_model import Servidor
from flask_jwt_extended import jwt_required,get_jwt_identity

class CanalController():
    @classmethod
    @jwt_required()
    def create(cls,nombre_canal):
        #crea un canal y lo agrega a la bdd
        #obtiene el id_servidor del nombre_servidor recibido por el request
        data=request.json
        nombre_servidor=data.get('nombre_servidor')
        servidor=Servidor.get(Servidor(nombre_servidor=nombre_servidor))

        #crea el canal 
        result=Canal.create_canal(nombre_canal,data.get('descripcion'),servidor.id_servidor)
        if result is not None:
            return {"message":"canal creado"},200
        else:
            return {"message":"eror en la creacion del canal"},404
        
    @classmethod
    @jwt_required()
    def mostrar_canales(cls,nombre_servidor):
        #obtener nombre de canales, del nombre de un servidor para enviarlos
        servidor=Servidor.get(Servidor(nombre_servidor=nombre_servidor))    
        result=Canal.get_canals(servidor.id_servidor)
        if result is not None:
            return { "canales": result }, 200
        else:
            return {"message":"no existen canales"},404
        
    @classmethod
    @jwt_required()
    def mostrar_canal(cls,nombre_canal):
        canal=Canal.get_canal(Canal(nombre_canal=nombre_canal))
        print("CANAL MOSTRAR ",canal)
        return canal,200
