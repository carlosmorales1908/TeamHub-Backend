from ..database import DatabaseConnection

class Channel:
  """
  Channel model class
  """
  def __init__(self, **kwargs):
    """
    Constructor method
    """
    self.channel_id = kwargs.get('channel_id')
    self.channel_name = kwargs.get('channel_name')
    self.server_id = kwargs.get('server_id')

  def serialize(self):
    """
    Serialize object representation
      Returns:
        dict: Object representation
    """
    return {
      "channel_id": self.channel_id,
      "channel_name": self.channel_name,
      "server_id": self.server_id
    }
  
  @classmethod
  def get_channel(cls, channel):
    """
    Get a channel and its messages by channel_id
    Args:
      - channel: Channel object
    Return:
      - list or
      - None
    """
    query = """select c.channel_id, c.channel_name, m.message_id, m.message, m.creation_date, m.user_id, u.user_name from channels c
      inner join servers s on c.server_id = s.server_id
      inner join messages m on c.channel_id = m.channel_id
      inner join users u on m.user_id = u.user_id
      where c.channel_id =  %(channel_id)s
      order by m.creation_date;"""
    params = channel.__dict__
    result = DatabaseConnection.fetch_all(query, params=params)
    if result is not None:
      return result
    return None
  
  @classmethod
  def get_only_channel(cls,channel):
    """
    Get a channel by channel_id
    Args:
      - channel: Channel object
    Return:
      - channel object or
      - None
    """
    query = """SELECT * FROM channels WHERE channel_id =  %(channel_id)s"""
    params = channel.__dict__
    result = DatabaseConnection.fetch_one(query, params=params)
    if result is not None:
      return cls(
        channel_id = result[0],
        channel_name = result[1],
        server_id = result[2]
      )
    return None
  
  @classmethod
  def create_channel(cls,channel):
    """
    Create a channel
    Args:
      - channel: Channel object
    """
    query = """INSERT INTO channels(channel_name,server_id) 
      VALUES (%(channel_name)s,%(server_id)s);"""
    params = channel.__dict__
    DatabaseConnection.execute_query(query, params)
  
  @classmethod
  def update_channel(cls,channel):
    """
    Update a channel
    Args:
      - channel: Channel object
    """
    query="""UPDATE channels SET 
      channel_name=%(channel_name)s,
      server_id=%(server_id)s
      WHERE channel_id=%(channel_id)s;"""
    params=channel.__dict__
    DatabaseConnection.execute_query(query, params=params)
  
  @classmethod
  def delete_channel(cls, channel):
    """
    Delete a channel by channel_id
    Args:
      - channel: Channel object
    """
    query = "DELETE FROM channels WHERE channel_id = %s"
    params = channel.channel_id,
    DatabaseConnection.execute_query(query, params=params)
  
  @classmethod
  def exists(cls,channel_id):
    """
    Check if a channel exist by channel_id
    Args:
      - channel_id
    Return:
      - boolean
    """
    query = """SELECT * FROM channels WHERE channel_id = %s"""
    params = channel_id,
    result = DatabaseConnection.fetch_one(query, params=params)
    return bool(result)

  @classmethod
  def show_channels_server(cls,server_user):
    """
    Get all channels from a server
    Args:
      - server_user: server_user object
    Return:
      - a list with channels or
      - None
    """
    query="""SELECT c.channel_id, c.channel_name, s_u.rol, s.server_name, s_u.user_id, u.user_name, s_u.server_id  FROM server_user s_u
    INNER JOIN channels c ON s_u.server_id = c.server_id
    INNER JOIN servers s ON s_u.server_id = s.server_id
    INNER JOIN users u ON s_u.user_id = u.user_id
    WHERE u.user_id = %(user_id)s AND s_u.server_id=%(server_id)s;"""
    params = server_user.__dict__
    result = DatabaseConnection.fetch_all(query, params=params)
    if result is not None:
      return result
    else:
      return None
    
  @classmethod
  def get_total_msgs_in_channel(cls, channel):
    query = """select count(message_id)
    from messages
    where channel_id = %(channel_id)s"""
    params = channel.__dict__
    result = DatabaseConnection.fetch_one(query, params=params)
    if result is not None:
      return result
    return None