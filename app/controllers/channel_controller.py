from ..models.channels_models import Channel
from ..models.server_user_models import Server_User
from flask import request, session

class ChannelController:
  @classmethod
  def get_channel(cls,channel_id):
    channel = Channel.get_channel(Channel(channel_id = channel_id))
    messages = []
    for message in channel:
      messages.append({
        "message_id":message[2],
        "message":message[3],
        "creation_date":message[4],
        "user_id":message[5]
      })
    # channels = [channel[4] for name,id in server]
    return {
      "channel_id": channel[0][0],
      "channel_name": channel[0][1],
      "messages":messages
    }
    # return channel.serialize(),200
  
  @classmethod
  def get_channels(cls,server_id):
    result = Channel.get_channels(Channel(server_id = server_id))
    channels=[]
    for channel in result:
      channels.append({
        "channel_id" : channel[0],
        "channel_name" : channel[1],
        "server_name" : channel[2]
      })
    return {"Servers":channels, "total":len(channels)},200
  
  @classmethod
  def create_channel(cls):
    data = request.json
    user = Channel(
      channel_name = data["channel_name"],
      server_id = data["server_id"]
    )
    Channel.create_channel(user)
    return {}, 201
  
  @classmethod
  def update_channel(cls,channel_id):
    res=Channel.get_channel(Channel(channel_id = channel_id))
    data = request.json

    if ('channel_name' in data):
      res.channel_name = data['channel_name']
    if ('server_id' in data) :
      res.server_id=data['server_id'] 
    Channel.update_channel(res)
    return {}, 200
  
  @classmethod
  def show_channels_server(cls):
    """
    Muestra los canales de un servidor cuando se lo selecciona y el rol del usuario
    """
    data = request.json
    result = Channel.show_channels_server(Server_User(
      user_id = data["user_id"],
      server_id = data["server_id"]
    ))

    channels=[]
    for channel in result:
      channels.append({
        "channel_id":channel[0],
        "channel_name":channel[1],
      })
    return {"Channels":channels, 
            "rol":channel[2],
            "server_name":channel[3],
            "user_id":channel[4],
            "user_name":channel[5],
            "server_id":channel[6]},200
    