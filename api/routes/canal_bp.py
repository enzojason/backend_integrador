from flask import Blueprint
from ..controllers.canal_controller import CanalController
from ..controllers.mensaje_controller import MensajeController

canal_bp = Blueprint('canal_bp', __name__)

canal_bp.route('/create/<string:nombre_canal>', methods=['POST'])(CanalController.create)
canal_bp.route('/<nombre_servidor>', methods=['POST'])(CanalController.mostrar_canales)
canal_bp.route('/<string:nombre_canal>/<string:mensaje>', methods=['POST'])(MensajeController.crear_mensaje)
canal_bp.route('/<string:nombre_canal>', methods=['GET'])(MensajeController.mostrar_mensajes)


