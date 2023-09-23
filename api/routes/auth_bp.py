from flask import Blueprint
from ..controllers.usuario_controller import UsuarioController
auth_bp = Blueprint('auth_bp', __name__)

auth_bp.route('/login', methods=['GET','POST'])(UsuarioController.login)
auth_bp.route('/profile', methods=['GET'])(UsuarioController.show_profile)
#auth_bp.route('/logout', methods=['POST'])(UsuarioController.logout)
auth_bp.route('/register',methods=['POST','GET'])(UsuarioController.create)
auth_bp.route('/update',methods=['POST','GET'])(UsuarioController.update_profile)


