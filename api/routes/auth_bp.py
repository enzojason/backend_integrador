from flask import Blueprint
from ..controllers.usuario_controller import UsuarioController
auth_bp = Blueprint('auth_bp', __name__)

auth_bp.route('/login', methods=['GET','POST'])(UsuarioController.login)
auth_bp.route('/profile', methods=['GET'])(UsuarioController.show_profile)
auth_bp.route('/register',methods=['POST','GET'])(UsuarioController.create)
auth_bp.route('/update',methods=['POST','GET'])(UsuarioController.update_profile)

auth_bp.route('/update_imagen',methods=['POST'])(UsuarioController.update_image)
auth_bp.route('/load_imagen',methods=['GET'])(UsuarioController.load_image)

