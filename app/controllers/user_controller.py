from ..models.user_model import User
from ..models.server_user_models import Server_User
from flask import request, session

class UserController:
  @classmethod
  def get_user(cls,user_id):
    user = User.get_user(User(user_id = user_id))
    return user.serialize(),200
  
  @classmethod
  def create_user(cls):
    data = request.json
    user = User(
      first_name = data["first_name"],
      last_name = data["last_name"],
      email = data["email"],
      user_name = data["user_name"],
      password = data["password"],
      date_of_birth = data["date_of_birth"],
    )
    User.create_user(user)
    return {}, 201
  
  @classmethod
  def update_user(cls,user_id):
    res=User.get_user(User(user_id = user_id))
    data = request.json

    if ('first_name' in data):
      res.first_name = data['first_name']
    if ('last_name' in data) :
      res.last_name=data['last_name'] 
    if ('email' in data)  :
      res.email=data['email'] 
    if ('user_name' in data) :
      res.user_name=data['user_name']  
    if ('password' in data) :
      res.password=data['password']  
    if ('date_of_birth' in data) :
      res.date_of_birth=data['date_of_birth'] 
    if ('profile_picture' in data) :
      res.profile_picture=data['profile_picture'] 

    User.update_user(res)
    return {}, 200
  
  @classmethod
  def get_user_server(cls):
    data = request.json
    user_name = data["user_name"]
    res=Server_User.get_user_server(User(user_name = user_name))
    servers = []
    for server in res:
      servers.append({
        "server_id" : server[0],
        "server_name" : server[1],
        "server_img": server[3]
      })
    return {"Servers":servers, "user_id":res[0][2], "user_name":user_name},200