from ..database import DatabaseConnection

class Server_User:
  """
  Server_User model class
  """
  def __init__(self, **kwargs):
      """
      Constructor method
      """
      self.server_user_id = kwargs.get('server_user_id')
      self.rol = kwargs.get('rol')
      self.server_id = kwargs.get('server_id')
      self.user_id = kwargs.get('user_id')

  def serialize(self):
    """
    Serialize object representation
      Returns:
        dict: Object representation
    """
    return {
      "server_user_id": self.server_user_id,
      "rol": self.rol,
      "server_id": self.server_id,
      "user_id": self.user_id
    }
  
  @classmethod
  def get_user_server(cls,user):
    """
    Get all servers based on user:
    Args:
      - user: User object
    Return:
      - a list with servers or
      - None
    """
    query = """SELECT s_u.server_id, s.server_name, s_u.user_id, s.img_server, u.user_name, s_u.rol FROM server_user s_u
    INNER JOIN servers s ON s_u.server_id = s.server_id
    INNER JOIN users u ON s_u.user_id = u.user_id
    WHERE u.user_id= %(user_id)s;"""
    params = user.__dict__
    result = DatabaseConnection.fetch_all(query, params=params)
    if result is not None:
      return result
    return None
  
  @classmethod
  def create_server_user(cls,server_user):
    """
    Create a reference in the intermediate table server_user when a user creates a channel
    Args:
      - server_user: Server_User object
    """
    query1 = """SET @last_server_id =last_insert_id();"""
    DatabaseConnection.execute_query(query1)
    query2="""INSERT INTO server_user(rol, user_id, server_id) VALUES ("Admin", %(user_id)s, @last_server_id);"""
    params = server_user.__dict__
    DatabaseConnection.execute_query(query2, params = params)
  
  @classmethod
  def join_server(cls,server_user):
    """
    Create a reference in the intermediate table server_user when a user joins a channel
    Args:
      - server_user: Server_User object
    """
    query="""INSERT INTO server_user(rol, user_id, server_id) VALUES ("Common", %(user_id)s, %(server_id)s);"""
    params = server_user.__dict__
    DatabaseConnection.execute_query(query, params = params)

  @classmethod
  def user_server_exist(cls,server_user):
    """
    """
    query="""SELECT * from server_user WHERE server_id = %(server_id)s and user_id = %(user_id)s;"""
    params = server_user.__dict__
    result = DatabaseConnection.fetch_one(query, params = params)
    return bool(result)