from ..database import DatabaseConnection

class Message:
  def __init__(self, **kwargs):
      self.message_id = kwargs.get('message_id')
      self.message = kwargs.get('message')
      self.creation_date = kwargs.get('creation_date')
      self.user_id = kwargs.get('user_id')
      self.channel_id = kwargs.get('user_id')

  def serialize(self):
    return {
      "message_id": self.message_id,
      "message": self.message,
      "creation_date": self.creation_date,
      "user_id": self.user_id,
      "channel_id": self.user_id
    }