from ..database import DatabaseConnection

class Message:
  """
  Message model class
  """
  def __init__(self, **kwargs):
    """
    Constructor method
    """
    self.message_id = kwargs.get('message_id')
    self.message = kwargs.get('message')
    self.creation_date = kwargs.get('creation_date')
    self.user_id = kwargs.get('user_id')
    self.channel_id = kwargs.get('user_id')

  def serialize(self):
    """
    Serialize object representation
      Returns:
        dict: Object representation
    """
    return {
      "message_id": self.message_id,
      "message": self.message,
      "creation_date": self.creation_date,
      "user_id": self.user_id,
      "channel_id": self.user_id
    }
  
  @classmethod
  def get_message(cls, message):
    """
    Get a message by message_id
    Args:
      - message: Message object
    Return:
      - message object or
      - None
    """
    query = """SELECT * FROM messages 
    WHERE message_id = %(message_id)s"""
    params = message.__dict__
    result = DatabaseConnection.fetch_one(query, params=params)

    if result is not None:
      return cls(
        message_id = result[0],
        message = result[1],
        creation_date = result[2],
        user_id = result[3],
        channel_id = result[4]
      )
    return None
  
  @classmethod
  def create_message(cls,message):
    """
    Create a message
    Args:
      - message: Message object
    """
    query = """INSERT INTO messages(message,user_id,channel_id) 
      VALUES (%(message)s,%(user_id)s,%(channel_id)s);"""
    params = message.__dict__
    DatabaseConnection.execute_query(query, params)

  @classmethod
  def update_message(cls,message):
    """
    Update a message
    Args:
      - message: Message object
    """
    query="""UPDATE messages SET 
      message=%(message)s
      WHERE message_id=%(message_id)s;"""
    params=message.__dict__
    DatabaseConnection.execute_query(query, params=params)
  
  @classmethod
  def delete_message(cls,message):
    """
    Delete a message ny message_id
    Args:
      - message: User object
    """
    sql = """DELETE FROM messages 
    WHERE message_id = %(message_id)s;"""
    params = message.__dict__
    DatabaseConnection.execute_query(sql, params)
  
  @classmethod
  def exists(cls,message_id):
    """
    Check if a message exist by message_id
    Args:
      - message_id
    Return:
      - boolean
    """
    query = """SELECT * FROM messages WHERE message_id = %s"""
    params = message_id,
    result = DatabaseConnection.fetch_one(query, params=params)
    return bool(result)