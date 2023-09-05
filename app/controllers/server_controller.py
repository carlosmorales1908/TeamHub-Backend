from ..models.servers_models import Server
from ..models.server_user_models import Server_User
from flask import request, session

class ServerController:
  @classmethod
  def get_server(cls,server_id):
    server = Server.get_server(Server(server_id = server_id))
    channels = []
    for channel in server:
      channels.append({
        "channel_name":channel[4],
        "channel_id":channel[5]
      })
    # channels = [channel[4] for name,id in server]
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
    user = Server(
      server_name = data["server_name"],
      description = data["description"]
    )
    Server.create_server(user)
    
    server_user = Server_User(user_id = data["user_id"])
    Server_User.create_server_user(server_user)
    return {}, 201
  
  @classmethod
  def update_server(cls,server_id):
    res=Server.get_server(Server(server_id = server_id))
    data = request.json

    if ('server_name' in data):
      res.server_name = data['server_name']
    if ('description' in data) :
      res.description=data['description'] 
    if ('img_server' in data)  :
      res.img_server=data['img_server'] 
    Server.update_server(res)
    return {}, 200
  
  @classmethod
  def join_server(cls):
    data = request.json
    server_user = Server_User(
      user_id = data["user_id"],
      server_id = data["server_id"]
      )
    Server_User.join_server(server_user)
    return {}, 200