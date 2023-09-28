from flask import Blueprint
from ..controllers.usuario_controller import UsuarioController
user_bp = Blueprint('user_bp', __name__)

user_bp.route('/login', methods=['GET','POST'])(UsuarioController.login)
user_bp.route('/profile', methods=['GET'])(UsuarioController.show_profile)
user_bp.route('/register',methods=['POST','GET'])(UsuarioController.create)
user_bp.route('/update',methods=['POST','GET'])(UsuarioController.update_profile)

user_bp.route('/update_imagen',methods=['POST'])(UsuarioController.update_image)
user_bp.route('/load_imagen',methods=['GET'])(UsuarioController.load_image)

