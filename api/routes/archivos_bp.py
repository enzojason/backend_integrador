from flask import Blueprint,send_from_directory
from ..controllers.archivo_controllers import ArchivoController

archivos_bp = Blueprint('archivos_bp', __name__)

archivos_bp.route('<path:nombre_archivo>')(ArchivoController.servir_archivo)
archivos_bp.route('/subir_imagen',methods=['POST'])(ArchivoController.subir_imagen)

