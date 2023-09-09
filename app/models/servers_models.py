from ..database import DatabaseConnection

class Server:
  def __init__(self, **kwargs):
      self.server_id = kwargs.get('server_id')
      self.server_name = kwargs.get('server_name')
      self.description = kwargs.get('description')
      self.img_server = kwargs.get('img_server')

  def serialize(self):
    return {
      "server_id": self.server_id,
      "server_name": self.server_name,
      "description": self.description,
      "img_server": self.img_server
    }
  
  @classmethod
  def get_server(cls, server):
    """
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
    sql = "SELECT * FROM servers;"
    result = DatabaseConnection.fetch_all(sql)
    if result is not None:
      return result
    else:
      return None
    
  @classmethod
  def create_server(cls,server):
    query = """INSERT INTO servers(server_name,description) 
      VALUES (%(server_name)s,%(description)s);"""
    params = server.__dict__
    DatabaseConnection.execute_query(query, params)
  
  @classmethod
  def update_server(cls,server):
    query="""UPDATE servers SET 
      server_name=%(server_name)s,
      description=%(description)s,
      img_server=%(img_server)s
      WHERE server_id=%(server_id)s;"""
    params=server.__dict__
    DatabaseConnection.execute_query(query, params=params)
  
  @classmethod
  def delete(cls, server):
    query = "DELETE FROM servers WHERE server_id = %s"
    params = server.server_id,
    DatabaseConnection.execute_query(query, params=params)
  
  @classmethod
  def exists(cls,server_id):
    query = """SELECT * FROM servers WHERE server_id = %s"""
    params = server_id,
    result = DatabaseConnection.fetch_one(query, params=params)
    return bool(result)