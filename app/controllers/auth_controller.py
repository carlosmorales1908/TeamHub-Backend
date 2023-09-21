from ..models.auth.user_auth_model import UserAuth
from flask import request, session

class UserAuthController:
  """
  UserAuth controller class
  """
  @classmethod
  def login(cls):
    """
    A user logs in
    """
    data = request.json
    user = UserAuth(
      user_name = data.get('user_name'),
      password = data.get('password')
    )
    
    if UserAuth.is_registered(user):
      session['user_name'] = data.get('user_name')
      # logged = UserAuth.after_loggin(user).__dict__
      # return {"user_id":logged["user_id"]},200
      return {"message": "Sesion iniciada"}, 200
    else:
      return {"message": "Usuario o contraseña incorrectos"}, 401
      
  @classmethod
  def show_profile(cls):
    """
    Shows the data of a user logged
    """
    user_name = session.get('user_name')
    # user_name = ""
    # if "user" in session:
    #   user_name = session['user']
    user = UserAuth.get_user_by_name(UserAuth(user_name = user_name))
    if user is None:
      return {"message": "Usuario no encontrado"}, 404
    else:
      return user.serialize(), 200
      
  @classmethod
  def logout(cls):
    """
    A user logs out
    """
    session.pop('user', None)
    return {"message": "Sesion cerrada"}, 200