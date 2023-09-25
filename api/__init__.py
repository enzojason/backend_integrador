from flask import Flask
from flask_cors import CORS
from config import Config
from .routes.auth_bp import auth_bp
from .routes.archivos_bp import archivos_bp
from .routes.servidor_bp import serve_bp
from .routes.mensaje_bp import mensaje_bp
from .routes.canal_bp import canal_bp
from .database import DatabaseConnection
from config import Config
from flask_jwt_extended import JWTManager


def init_app():
    """Crea y configura la aplicación Flask"""
    #database creacion
    DatabaseConnection.crear_bdd()
    DatabaseConnection.crear_tables()
    DatabaseConnection.execute_query(query="""INSERT IGNORE INTO proyecto_bdd.roles(nombre_rol,id_rol) VALUES ('invitado','0');""")
    DatabaseConnection.execute_query(query="""INSERT IGNORE INTO proyecto_bdd.roles(nombre_rol,id_rol) VALUES ('administrador','1');""")  

    app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)
    app.config['SECRET_KEY'] = Config.SECRET_KEY
    CORS(app, supports_credentials=True)
    
    app.config.from_object(Config)
    
    jwt=JWTManager(app)

    app.register_blueprint(auth_bp, url_prefix = '/auth')
    app.register_blueprint(archivos_bp,url_prefix= '/static')
    app.register_blueprint(serve_bp,url_prefix= '/server')
    app.register_blueprint(canal_bp,url_prefix= '/canal')
    app.register_blueprint(mensaje_bp,url_prefix= '/message')
    return app
