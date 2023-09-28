import mysql.connector

class DatabaseConnection:
    _connection = None

    @classmethod
    def get_connection(cls):
        if cls._connection is None:
            cls._connection = mysql.connector.connect(
            host = '127.0.0.1',
            user = 'root',
            port = '3306',
            password = 'root'
            
            )
        return cls._connection

    
    
    @classmethod
    def execute_query(cls, query, params=None):
        cursor = cls.get_connection().cursor()
        cursor.execute(query, params)
        cls._connection.commit()
        return cursor
    
    @classmethod
    def fetch_all(cls, query, database_name=None, params=None):
        cursor = cls.get_connection().cursor()
        cursor.execute(query, params)
        return cursor.fetchall()
    
    @classmethod
    def fetch_one(cls, query, params=None):
        cursor = cls.get_connection().cursor()
        cursor.execute(query, params)
        return cursor.fetchone()
    
    @classmethod
    def close_connection(cls):
        if cls._connection is not None:
            cls._connection.close()
            cls._connection = None

    @classmethod
    def crear_bdd(cls):
        cursor=cls.get_connection().cursor()
        create_database ="CREATE DATABASE IF NOT EXISTS proyecto_bdd"
        cursor.execute(create_database)

    @classmethod
    def crear_tables(cls):
        #crea las tablas
        cursor=cls.get_connection().cursor()
        query ="USE proyecto_bdd;"
        cursor.execute(query)

        create_tables="""CREATE TABLE IF NOT EXISTS roles(
                            id_rol INT NOT NULL UNIQUE ,
                            nombre_rol  CHAR(40) UNIQUE,
                            PRIMARY KEY(id_rol)
                            )"""
        cursor.execute(create_tables)

        create_tables="""CREATE TABLE IF NOT EXISTS usuarios(
                            id_usuario INT NOT NULL UNIQUE AUTO_INCREMENT,
                            username VARCHAR(40) NOT NULL,
                            contrasena VARCHAR(40) NOT NULL,
                            email VARCHAR(40) NULL,
                            nombre_usuario CHAR(30) NULL,
                            apellido_usuario CHAR(30) NULL,
                            fecha_creacion DATETIME NOT NULL DEFAULT NOW(),
                            imagen_perfil BLOB NULL,
                            PRIMARY KEY(id_usuario)
                        )"""
        cursor.execute(create_tables)

        create_tables="""CREATE TABLE IF NOT EXISTS servidores(
                            id_servidor INT  NOT NULL UNIQUE AUTO_INCREMENT,
                            nombre_servidor VARCHAR(40) NOT NULL,
                            fecha_creacion DATETIME NOT NULL DEFAULT NOW(),
                            id_administrador INT NOT NULL,
                            PRIMARY KEY(id_servidor),
                            FOREIGN KEY (id_administrador) REFERENCES usuarios(id_usuario)
                        )"""
        cursor.execute(create_tables)

        create_tables = """CREATE TABLE IF NOT EXISTS canales (
                            id_canal INT  NOT NULL UNIQUE AUTO_INCREMENT,
                            nombre_canal VARCHAR(40) NOT NULL,
                            fecha_creacion DATETIME NOT NULL DEFAULT NOW(),
                            descripcion TEXT,
                            id_servidor INT,
                            FOREIGN KEY (id_servidor) REFERENCES servidores(id_servidor),
                            PRIMARY KEY(id_canal)
                            )"""
        cursor.execute(create_tables)

        create_tables="""CREATE TABLE IF NOT EXISTS mensajes(
                            id_mensaje INT  NOT NULL UNIQUE AUTO_INCREMENT,
                            mensaje VARCHAR(254) NULL,
                            fecha DATETIME NOT NULL DEFAULT NOW(),
                            id_usuario INT NOT NULL,
                            id_canal INT NOT NULL,
                            PRIMARY KEY(id_mensaje),
                            FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
                            FOREIGN KEY (id_canal) REFERENCES canales(id_canal)
                            )"""
        cursor.execute(create_tables)

        create_tables="""CREATE TABLE IF NOT EXISTS usuario_servidor(
                            id_usuario_servidor INT NOT NULL UNIQUE AUTO_INCREMENT,
                            id_usuario INT NOT NULL,
                            id_servidor INT NOT NULL,
                            id_rol INT NOT NULL,
                            PRIMARY KEY(id_usuario_servidor),
                            CONSTRAINT fk_id_rol FOREIGN KEY (id_rol) REFERENCES roles(id_rol),
                            CONSTRAINT fk_id_usuario_servidor FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
                            CONSTRAINT fk_id_servidor FOREIGN KEY (id_servidor) REFERENCES servidores(id_servidor)
                            )"""
        cursor.execute(create_tables)
