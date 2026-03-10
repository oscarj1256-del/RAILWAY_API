from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    db.init_app(app)

    from app.routes.user_routes import user_bp 
    from app.routes.clientes_routes import cliente_bp
    
    # Registramos el Blueprint de usuarios y le agregamos el prefijo '/api/users'
    # Esto hace que todas las rutas definidas en user_bp comiencen con:
    # http://127.0.0.1:5000/api/users
    app.register_blueprint(user_bp, url_prefix="/api/users")
    app.register_blueprint(cliente_bp, url_prefix="/api/clientes")

    return app
