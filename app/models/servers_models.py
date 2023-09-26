from ..database import DatabaseConnection

class Server:
  """
  Server model class
  """
  def __init__(self, **kwargs):
      """
      Constructor method
      """
      self.server_id = kwargs.get('server_id')
      self.server_name = kwargs.get('server_name')
      self.description = kwargs.get('description')
      self.img_server = kwargs.get('img_server')

  def serialize(self):
    """
    Serialize object representation
      Returns:
        dict: Object representation
    """
    return {
      "server_id": self.server_id,
      "server_name": self.server_name,
      "description": self.description,
      "img_server": self.img_server
    }
  
  @classmethod
  def get_server(cls, server):
    """
    Get a server and channels by id:
    Args:
      - server: Server object
    Return:
      - Server object or
      - None
    """
    query = """SELECT s.server_id, s.server_name, s.description, s.img_server, c.channel_name, c.channel_id FROM servers s 
            INNER JOIN channels c ON s.server_id = c.server_id 
            WHERE s.server_id =  %(server_id)s"""
    params = server.__dict__
    result = DatabaseConnection.fetch_all(query, params=params)
    if result is not None:
      return result
    return None
  
  @classmethod
  def get_only_server(cls,server):
    """
    Get a server by id:
    Args:
      - server: Server object
    Return:
      - Server object or
      - None
    """
    query = """SELECT * FROM servers WHERE server_id =  %(server_id)s"""
    params = server.__dict__
    result = DatabaseConnection.fetch_one(query, params=params)
    if result is not None:
      return cls(
        server_id = result[0],
        server_name = result[1],
        description = result[2],
        img_server = result[3]
      )
    return None

  @classmethod
  def get_servers(cls):
    """
    Get a all servers
    Return:
      - tuple with servers or
      - None
    """
    sql = """select s.server_id, s.server_name, s.description, s.img_server, count(s_u.user_id) as total_users from servers s
      inner join server_user s_u on s.server_id = s_u.server_id
      group by s.server_id;"""
    result = DatabaseConnection.fetch_all(sql)
    if result is not None:
      return result
    else:
      return None
    
  @classmethod
  def create_server(cls,server):
    """
    Create a server
    Args:
      - server: Server object
    """
    query = """INSERT INTO servers(server_name,description) 
      VALUES (%(server_name)s,%(description)s);"""
    params = server.__dict__
    DatabaseConnection.execute_query(query, params)
  
  @classmethod
  def update_server(cls,server):
    """
    Update a server
    Args:
      - server: Server object
    """
    query="""UPDATE servers SET 
      server_name=%(server_name)s,
      description=%(description)s,
      img_server=%(img_server)s
      WHERE server_id=%(server_id)s;"""
    params=server.__dict__
    DatabaseConnection.execute_query(query, params=params)
  
  @classmethod
  def delete(cls, server):
    """
    Delete a server
    Args:
      - server: Server object
    """
    query = "DELETE FROM servers WHERE server_id = %s"
    params = server.server_id,
    DatabaseConnection.execute_query(query, params=params)
  
  @classmethod
  def exists(cls,server_id):
    """
    Check if a server exist by server_id
    Args:
      - server_id
    Return:
      - boolean
    """
    query = """SELECT * FROM servers WHERE server_id = %s"""
    params = server_id,
    result = DatabaseConnection.fetch_one(query, params=params)
    return bool(result)
  
  @classmethod
  def verify_servername(cls,server):
    """
    Check if a server_name already exist in the DB
    Args:
      - server: Server object
    Return:
      - boolean
    """
    query = """SELECT server_id FROM servers 
    WHERE server_name = %(server_name)s;"""
    params = server.__dict__
    result = DatabaseConnection.fetch_one(query, params=params)
    return bool(result)