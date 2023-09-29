from flask import Flask, request, session
from flask_cors import CORS
from config import Config

from .routes.auth_bp import auth_bp
from .routes.user_bp import user_bp
from .routes.server_bp import server_bp
from .routes.channel_bp import channel_bp
from .routes.message_bp import message_bp
from .routes.errors_handlers import errors

from .database import DatabaseConnection

def init_app():
  """Crea y configura la aplicación Flask"""
  app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)
  CORS(app, supports_credentials=True)
  app.config.from_object(
      Config
  )
  DatabaseConnection.set_config(app.config)

  app.register_blueprint(auth_bp, url_prefix = '/auth')
  app.register_blueprint(user_bp, url_prefix = '/api')
  app.register_blueprint(server_bp, url_prefix = '/api')
  app.register_blueprint(channel_bp, url_prefix = '/api')
  app.register_blueprint(message_bp, url_prefix = '/api')
  app.register_blueprint(errors, url_prefix = '/')

  # PROTEGE RUTAS ANTES DE INICAR SESION
  # ------- COMENTAR PARA PROBAR LA API
  @app.before_request
  def antes_de_cada_peticion():
    ruta = request.path
    if not 'user_name' in session and ruta != "/login" and ruta != "/profile" and ruta != "/logout" and not ruta.startswith("/auth"):
        return {"msg":"Debes iniciar sesion primero"},404
  # -----
    
  return app