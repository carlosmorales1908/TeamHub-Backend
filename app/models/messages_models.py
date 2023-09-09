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
  
  @classmethod
  def get_message(cls, message):
    """
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
    """
    query = """INSERT INTO messages(message,user_id,channel_id) 
      VALUES (%(message)s,%(user_id)s,%(channel_id)s);"""
    params = message.__dict__
    DatabaseConnection.execute_query(query, params)

  @classmethod
  def update_message(cls,message):
    """
    """
    query="""UPDATE messages SET 
      message=%(message)s
      WHERE message_id=%(message_id)s;"""
    params=message.__dict__
    DatabaseConnection.execute_query(query, params=params)
  
  @classmethod
  def delete_message(cls,message):
    sql = """DELETE FROM messages 
    WHERE message_id = %(message_id)s;"""
    params = message.__dict__
    DatabaseConnection.execute_query(sql, params)
  
  @classmethod
  def exists(cls,message_id):
    query = """SELECT * FROM users WHERE user_id = %s"""
    params = message_id,
    result = DatabaseConnection.fetch_one(query, params=params)
    return bool(result)