from flask import Blueprint
from ..controllers.servidor_controller import ServidorController
serve_bp = Blueprint('server_bp', __name__)

serve_bp.route('/create/<string:nombre_servidor>', methods=['POST'])(ServidorController.create)
serve_bp.route('/join/<string:nombre_servidor>', methods=['POST'])(ServidorController.join)
serve_bp.route('/my_servers', methods=['GET'])(ServidorController.mostrar_servidores)
serve_bp.route('/search/<string:nombre>', methods=['GET'])(ServidorController.buscar_servidor)


