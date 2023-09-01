from ..models.channels_models import Channel
from flask import request, session

class ChannelController:
  @classmethod
  def get_channel(cls,channel_id):
    channel = Channel.get_channel(Channel(channel_id = channel_id))
    return channel.serialize(),200
  
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