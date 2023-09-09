from ..models.servers_models import Server
from ..models.server_user_models import Server_User
from ..models.exceptions import NotFound
from ..helpers.helper import *
from flask import request, session

class ServerController:

  @classmethod
  def get_server(cls,server_id):

    if not Server.exists(server_id):
      raise NotFound(description= f"Server with id {server_id} Not Found")
    
    server = Server.get_server(Server(server_id = server_id))
    channels = []
    for channel in server:
      channels.append({
        "channel_name":channel[4],
        "channel_id":channel[5]
      })
    return {
      "server_id": server[0][0],
      "server_name": server[0][1],
      "description": server[0][2],
      "img_server": server[0][3],
      "channels":channels
    }
  
  @classmethod
  def get_servers(cls):
    result = Server.get_servers()
    servers=[]
    for server in result:
      servers.append({
        "server_id" : server[0],
        "server_name" : server[1],
        "description" : server[2],
        "img_server" : server[3]
      })
    return {"Servers":servers, "total":len(servers)},200
  
  @classmethod
  def create_server(cls):
    data = request.json

    # --- VALIDATIONS
    validate_value_in_data("server_name",data)
    validate_value_in_data("description",data)
    validate_value_in_data("user_id",data)
    validate_is_string(data["server_name"])
    validate_is_int(data["user_id"])
    validate_len(data["server_name"])
    # ---

    server = Server(**data)
    Server.create_server(server)
    
    server_user = Server_User(user_id = data["user_id"])
    Server_User.create_server_user(server_user)
    return {'message': 'Server created successfully'}, 201
  
  @classmethod
  def update_server(cls,server_id):
    server=Server.get_server(Server(server_id = server_id))
    data = request.json

    if not Server.exists(server_id):
      raise NotFound(description= f"Server with id {server_id} Not Found")
    
    if ('server_name' in data):
      validate_is_string(data["server_name"])
      validate_len(data["server_name"])
      server.server_name = data['server_name']
    if ('description' in data) :
      server.description=data['description'] 
    if ('img_server' in data)  :
      server.img_server=data['img_server'] 
      
    Server.update_server(server)
    return {'message': 'Server updated successfully'}, 200
  
  @classmethod
  def delete(cls, server_id):
    server = Server(server_id=server_id)

    if not Server.exists(server_id):
      raise NotFound(description= f"Server with id {server_id} Not Found to Delete")
    
    Server.delete(server)
    return {'message': 'User deleted successfully'}, 204
  
  @classmethod
  def join_server(cls):
    data = request.json

    validate_value_in_data("user_id",data)
    validate_value_in_data("server_id",data)
    validate_is_int(data["user_id"])
    validate_is_int(data["server_id"])

    server_user = Server_User(**data)

    Server_User.join_server(server_user)
    return {'message': 'User joins successfully to server'}, 200