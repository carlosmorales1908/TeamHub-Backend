from ..models.user_model import User
from ..models.server_user_models import Server_User
from ..models.exceptions import NotFound
from ..helpers.helper import *
from flask import request, session

class UserController:
  """
  User controller class
  """
  @classmethod
  def get_user(cls,user_id):
    """
    Get a user by id
    """
    user = User.get_user(User(user_id = user_id))
    if user is not None:
      return user.serialize(), 200
    else:
      raise NotFound(description= f"User with id {user_id} not found")
  
  @classmethod
  def create_user(cls):
    """
    Create a new user
    """
    data = request.json

    # --- VALIDATIONS
    validate_value_in_data("first_name",data)
    validate_is_string(data["first_name"])
    validate_len(data["first_name"])
    validate_value_in_data("last_name",data)
    validate_is_string(data["last_name"])
    validate_len(data["last_name"])
    validate_value_in_data("email",data)
    validate_is_string(data["email"])
    validate_value_in_data("user_name",data)
    validate_is_string(data["user_name"])
    validate_len(data["user_name"])
    validate_value_in_data("password",data)
    validate_is_string(data["password"])
    validate_len_password(data["password"])
    validate_value_in_data("date_of_birth",data)
    validate_dob(data["date_of_birth"])

    invalid_data('user_id',data)
    # ---

    user = User(**data)
    
    verify_username(user)
    verify_email(user)

    User.create_user(user)
    return {'message': 'User created successfully'}, 201
  
  @classmethod
  def update_user(cls,user_id):
    """
    Update a user by id
    """
    user=User.get_user(User(user_id = user_id))
    data = request.json

    if not User.exists(user_id):
      raise NotFound(description= f"User with id {user_id} Not Found to Update")

    invalid_data('user_id',data)
    
    if ('first_name' in data):
      validate_is_string(data["first_name"])
      validate_len(data["first_name"])
      user.first_name = data['first_name']
    if ('last_name' in data) :
      validate_len(data["last_name"])
      validate_is_string(data["last_name"]) 
      user.last_name=data['last_name'] 
    if ('email' in data)  :
      validate_is_string(data["email"])
      user.email=data['email'] 
    if ('user_name' in data) :
      validate_is_string(data["user_name"])
      validate_len(data["user_name"])
      user.user_name=data['user_name']  
    if ('password' in data) :
      validate_is_string(data["password"])
      validate_len_password(data["password"])
      user.password=data['password']  
    if ('date_of_birth' in data) :
      validate_dob(data["date_of_birth"])
      user.date_of_birth=data['date_of_birth'] 
    if ('profile_picture' in data) :
      user.profile_picture=data['profile_picture'] 
    
    verify_username(user)
    # verify_email(user)

    User.update_user(user)
    return {'message': 'User updated successfully'}, 200
  
  @classmethod
  def get_user_server(cls,user_id):
    """
    Get server and user info by user_name
    """
    # validate_is_string(data["user_name"])
    # user_name = data["user_name"]
    res=Server_User.get_user_server(User(user_id = user_id))
    servers = []
    for server in res:
      servers.append({
        "server_id" : server[0],
        "server_name" : server[1],
        "server_img": server[3]
      })
    return {"Servers":servers, "user_id":res[0][2], "user_id":user_id, "user_name":res[0][4]},200
  
  @classmethod
  def delete(cls, user_id):
    """
    Delete a user by id
    """
    user = User(user_id=user_id)
    
    if not User.exists(user_id):
      raise NotFound(description= f"User with id {user_id} Not Found to Delete")
    
    User.delete(user)
    return {'message': 'User deleted successfully'}, 204