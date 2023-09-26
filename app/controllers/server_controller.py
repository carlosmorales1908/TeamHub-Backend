from ..models.servers_models import Server
from ..models.server_user_models import Server_User
from ..models.exceptions import NotFound, BadRequest
from ..helpers.helper import *
from flask import request, session

class ServerController:
  """
  Server controller class
  """
  @classmethod
  def get_server(cls,server_id):
    """
    Get a server by id
    """
    if not Server.exists(server_id):
      raise NotFound(description= f"Server with id {server_id} Not Found")
    
    server = Server.get_server(Server(server_id = server_id))
    channels = []
    for channel in server:
      channels.append({
        "channel_name":channel[4],
        "channel_id":channel[5]
      })

    if server:
      return {
        "server_id": server[0][0],
        "server_name": server[0][1],
        "description": server[0][2],
        "img_server": server[0][3],
        "channels":channels
      }
    
    server = Server.get_only_server(Server(server_id = server_id))
    return server.serialize(), 200
  
  @classmethod
  def get_servers(cls):
    """
    Get all servers 
    """
    result = Server.get_servers()
    servers=[]
    for server in result:
      servers.append({
        "server_id" : server[0],
        "server_name" : server[1],
        "description" : server[2],
        "img_server" : server[3]
        # "total_users": server[4]
      })
    return {"Servers":servers, "total":len(servers)},200
  
  @classmethod
  def create_server(cls):
    """
    Create a new server
    """
    data = request.json

    # --- VALIDATIONS
    validate_value_in_data("server_name",data)
    validate_value_in_data("description",data)
    validate_value_in_data("user_id",data)
    validate_is_string(data["server_name"])
    validate_is_int(data["user_id"])
    validate_len(data["server_name"])

    invalid_data('server_id',data)
    # ---

    server = Server(**data)

    verify_servername(server)
    
    Server.create_server(server)
    
    server_user = Server_User(user_id = data["user_id"])
    Server_User.create_server_user(server_user)
    return {'message': 'Server created successfully'}, 201
  
  @classmethod
  def update_server(cls,server_id):
    """
    Update a server by id
    """
    server=Server.get_server(Server(server_id = server_id))
    if not server:
      server = Server.get_only_server(Server(server_id = server_id))
    data = request.json

    if not Server.exists(server_id):
      raise NotFound(description= f"Server with id {server_id} Not Found")
    
    invalid_data('server_id',data)
    
    if ('server_name' in data):
      validate_is_string(data["server_name"])
      validate_len(data["server_name"])
      server.server_name = data['server_name']
    if ('description' in data) :
      server.description=data['description'] 
    if ('img_server' in data)  :
      server.img_server=data['img_server'] 
    
    verify_servername(server)
      
    Server.update_server(server)
    return {'message': 'Server updated successfully'}, 200
  
  @classmethod
  def delete(cls, server_id):
    """
    Delete a server by id
    """
    server = Server(server_id=server_id)

    if not Server.exists(server_id):
      raise NotFound(description= f"Server with id {server_id} Not Found to Delete")
    
    Server.delete(server)
    return {'message': 'User deleted successfully'}, 204
  
  @classmethod
  def join_server(cls):
    """
    Join a server
    """
    data = request.json
    
    validate_value_in_data("user_id",data)
    validate_value_in_data("server_id",data)
    validate_is_int(data["user_id"])
    validate_is_int(data["server_id"])

    invalid_data('server_user_id',data)
    invalid_data('rol',data)

    server_user = Server_User(**data)

    if Server_User.user_server_exist(server_user):
      raise BadRequest(description= "User already joined to this server")
    Server_User.join_server(server_user)
    return {'message': 'User joins successfully to server'}, 200