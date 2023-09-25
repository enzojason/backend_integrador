from flask import Blueprint
from ..controllers.mensaje_controller import MensajeController

mensaje_bp = Blueprint('mensaje_bp', __name__)

mensaje_bp.route('/<string:nombre_canal>/<string:mensaje>', methods=['POST'])(MensajeController.crear_mensaje)
mensaje_bp.route('/<string:nombre_canal>', methods=['GET'])(MensajeController.mostrar_mensajes)
