from ..models.messages_models import Message
from flask import request, session

class MessageController:
  @classmethod
  def get_message(cls,message_id):
    message = Message.get_message(Message(message_id = message_id))
    return message.serialize(),200
  
  @classmethod
  def create_message(cls):
    data = request.json
    message = Message(
      message = data["message"],
      user_id = data["user_id"],
      channel_id = data["channel_id"]
    )
    Message.create_message(message)
    return {}, 201
  
  @classmethod
  def update_message(cls,message_id):
    res=Message.get_message(Message(message_id = message_id))
    data = request.json

    if ('message' in data):
      res.message = data['message']

    Message.update_message(res)
    return {}, 200
  
  @classmethod
  def delete_message(self,message_id):
    Message.delete_message(Message(message_id = message_id))
    return {}, 201