from ..models.messages_models import Message
from ..models.exceptions import NotFound
from ..helpers.helper import *
from flask import request, session

class MessageController:
  @classmethod
  def get_message(cls,message_id):

    if not Message.exists(message_id):
      raise NotFound(description= f"Message with id {message_id} Not Found")
    
    message = Message.get_message(Message(message_id = message_id))
    return message.serialize(),200
  
  @classmethod
  def create_message(cls):
    data = request.json

    # --- VALIDATIONS
    validate_value_in_data("message",data)
    validate_value_in_data("user_id",data)
    validate_value_in_data("channel_id",data)
    validate_is_string(data["message"])
    validate_is_int(data["user_id"])
    validate_is_int(data["channel_id"])
    validate_len_message(data["message"])

    invalid_data('message_id',data)
    invalid_data('creation_date',data)
    # ---

    message = Message(**data)
    Message.create_message(message)
    return {'message': 'Message created successfully'}, 201
  
  @classmethod
  def update_message(cls,message_id):
    message=Message.get_message(Message(message_id = message_id))
    data = request.json

    validate_value_in_data("message",data)
    invalid_data('message_id',data)
    invalid_data('creation_date',data)

    if ('message' in data):
      validate_is_string(data["message"])
      validate_len_message(data["message"])
      message.message = data['message']

    Message.update_message(message)
    return {'message': 'Message updated successfully'}, 200
  
  @classmethod
  def delete_message(self,message_id):
    Message.delete_message(Message(message_id = message_id))
    return {}, 201