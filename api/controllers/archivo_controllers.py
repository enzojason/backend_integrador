from flask import send_from_directory,request,jsonify
from flask_jwt_extended import jwt_required
import os,shutil
from werkzeug.utils import secure_filename

class ArchivoController:
    @classmethod
    def servir_archivo(cls,nombre_archivo):
        return send_from_directory('static/imagenes', nombre_archivo)
    
    @classmethod
    @jwt_required()
    def subir_imagen(cls):
        try:
            imagen = request.files["imagen"]
            nombre_archivo = imagen.filename
            ruta_completa = f'static/{nombre_archivo}'  # Ruta completa en la carpeta "static"
            imagen.save(ruta_completa)
            nueva_ruta = f"/static/{nombre_archivo}"
            return jsonify({"mensaje": "Imagen subida con éxito", "nuevaRuta": nueva_ruta})
        except Exception as e:
            return jsonify({"error": str(e)}), 500