from ..database import DatabaseConnection

class Channel:
  def __init__(self, **kwargs):
    self.channel_id = kwargs.get('channel_id')
    self.channel_name = kwargs.get('channel_name')
    self.server_id = kwargs.get('server_id')

  def serialize(self):
    return {
      "channel_id": self.channel_id,
      "channel_name": self.channel_name,
      "server_id": self.server_id
    }
  
  @classmethod
  def get_channel(cls, server):
    """
    """
    # query = """SELECT * FROM channels 
    # WHERE channel_id = %(channel_id)s"""
    # params = server.__dict__
    # result = DatabaseConnection.fetch_one(query, params=params)

    # if result is not None:
    #   return cls(
    #     channel_id = result[0],
    #     channel_name = result[1],
    #     server_id = result[2]
    #   )
    # return None
    query = """select c.channel_id, c.channel_name, m.message_id, m.message, m.creation_date, m.user_id from channels c
          inner join servers s on c.server_id = s.server_id
          inner join messages m on c.channel_id = m.channel_id
          where c.channel_id =  %(channel_id)s"""
    params = server.__dict__
    result = DatabaseConnection.fetch_all(query, params=params)
    if result is not None:
      return result
    return None
  
  @classmethod
  def get_channels(cls,channel):
    # sql = """SELECT * FROM channels 
    # WHERE server_id = %(server_id)s"""
    sql = """SELECT c.channel_id, c.channel_name, s.server_name FROM channels c
        INNER JOIN servers s ON c.server_id = s.server_id
        WHERE c.server_id =  %(server_id)s;"""
    params = channel.__dict__
    result = DatabaseConnection.fetch_all(sql, params=params)
    if result is not None:
      return result
    else:
      return None
  
  @classmethod
  def create_channel(cls,channel):
    query = """INSERT INTO channels(channel_name,server_id) 
      VALUES (%(channel_name)s,%(server_id)s);"""
    params = channel.__dict__
    DatabaseConnection.execute_query(query, params)
  
  @classmethod
  def update_channel(cls,channel):
    query="""UPDATE channels SET 
      channel_name=%(channel_name)s,
      server_id=%(server_id)s
      WHERE channel_id=%(channel_id)s;"""
    params=channel.__dict__
    DatabaseConnection.execute_query(query, params=params)