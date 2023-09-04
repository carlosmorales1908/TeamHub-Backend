from ..models.auth.user_model import User

from flask import request, session

class UserController:

    @classmethod
    def login(cls):
        data = request.json
        user = User(
            user_name = data.get('user_name'),
            password = data.get('password')
        )
        
        if User.is_registered(user):
            session['user'] = data.get('user_name')
            return {"message": "Sesion iniciada"}, 200
        else:
            return {"message": "Usuario o contraseña incorrectos"}, 401
        
    @classmethod
    def show_profile(cls):
        user_name = session['user']
        user = User.get_user_by_name(User(user_name = user_name))
        if user is None:
            return {"message": "Usuario no encontrado"}, 404
        else:
            return user.serialize(), 200
        
    @classmethod
    def logout(cls):
        session.pop('user', None)
        return {"message": "Sesion cerrada"}, 200