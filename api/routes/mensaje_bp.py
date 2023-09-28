from flask import Blueprint
from ..controllers.mensaje_controller import MensajeController

mensaje_bp = Blueprint('mensaje_bp', __name__)

mensaje_bp.route('/<int:id_canal>/<string:mensaje>', methods=['POST'])(MensajeController.crear_mensaje)
mensaje_bp.route('/<int:id_canal>', methods=['GET'])(MensajeController.mostrar_mensajes)
mensaje_bp.route('/modify/<int:id_mensaje>/<string:mensaje>', methods=['POST'])(MensajeController.modificar_mensaje)
