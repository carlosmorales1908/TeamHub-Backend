from ..models.channels_models import Channel
from ..models.server_user_models import Server_User
from ..models.exceptions import NotFound
from ..helpers.helper import *
from flask import request, session

class ChannelController:
  """
  Channel controller class
  """
  @classmethod
  def get_channel(cls,channel_id):
    """
    Get a channel by id
    """
    if not Channel.exists(channel_id):
      raise NotFound(description= f"Channel with id {channel_id} Not Found")
    
    channel = Channel.get_channel(Channel(channel_id = channel_id))
    messages = []
    for message in channel:
      messages.append({
        "message_id":message[2],
        "message":message[3],
        "creation_date":message[4],
        "user_id":message[5]
      })
    
    if channel:
      return {
        "channel_id": channel[0][0],
        "channel_name": channel[0][1],
        "messages":messages
      }
    channel = Channel.get_only_channel(Channel(channel_id = channel_id))
    return channel.serialize(), 200
  
  @classmethod
  def create_channel(cls):
    """
    Create a new channel
    """
    data = request.json

    # --- VALIDATIONS
    validate_value_in_data("channel_name",data)
    validate_value_in_data("server_id",data)
    validate_is_string(data["channel_name"])
    validate_is_int(data["server_id"])
    validate_len(data["channel_name"])

    invalid_data('channel_id',data)
    # ---

    channel = Channel(**data)
    Channel.create_channel(channel)
    return {'message': 'Channel created successfully'}, 201
  
  @classmethod
  def update_channel(cls,channel_id):
    """
    Update a channel by id
    """
    channel=Channel.get_channel(Channel(channel_id = channel_id))
    if not channel:
      channel = Channel.get_only_channel(Channel(channel_id = channel_id))
    data = request.json

    if not Channel.exists(channel_id):
      raise NotFound(description= f"Channel with id {channel_id} Not Found")
    
    invalid_data('channel_id',data)
    
    if ('channel_name' in data):
      validate_is_string(data["channel_name"])
      validate_len(data["channel_name"])
      channel.channel_name = data['channel_name']
    if ('server_id' in data) :
      validate_is_int(data["server_id"])
      channel.server_id=data['server_id'] 

    Channel.update_channel(channel)
    return {'message': 'Channel updated successfully'}, 200
  
  @classmethod
  def delete_channel(cls, channel_id):
    """
    Delete a channel by id
    """
    channel = Channel(channel_id=channel_id)

    if not Channel.exists(channel_id):
      raise NotFound(description= f"Channel with id {channel_id} Not Found to Delete")
    
    Channel.delete_channel(channel)
    return {'message': 'Channel deleted successfully'}, 204
  
  @classmethod
  def show_channels_server(cls):
    """
    Show all channels on a server and the user rol
    """
    data = request.json

    validate_value_in_data("user_id",data)
    validate_value_in_data("server_id",data)
    validate_is_int(data["user_id"])
    validate_is_int(data["server_id"])

    result = Channel.show_channels_server(Server_User(**data))

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

  @classmethod
  def get_total_msgs_in_channel(cls, channel_id):
    if not Channel.exists(channel_id):
      raise NotFound(description= f"Channel with id {channel_id} Not Found")
    
    channel = Channel.get_total_msgs_in_channel(Channel(channel_id = channel_id))
    return {"total msgs": channel},200