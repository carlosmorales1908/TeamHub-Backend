from ..models.channels_models import Channel
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