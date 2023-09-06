from ..database import DatabaseConnection

class Server_User:
  def __init__(self, **kwargs):
      self.server_user_id = kwargs.get('server_user_id')
      self.rol = kwargs.get('rol')
      self.server_id = kwargs.get('server_id')
      self.user_id = kwargs.get('user_id')

  def serialize(self):
    return {
      "server_user_id": self.server_user_id,
      "rol": self.rol,
      "server_id": self.server_id,
      "user_id": self.user_id
    }
  
  @classmethod
  def get_user_server(cls,user):
    query = """SELECT s_u.server_id, s.server_name, s_u.user_id, s.img_server FROM server_user s_u
    INNER JOIN servers s ON s_u.server_id = s.server_id
    INNER JOIN users u ON s_u.user_id = u.user_id
    WHERE u.user_name= %(user_name)s;"""
    params = user.__dict__
    result = DatabaseConnection.fetch_all(query, params=params)
    if result is not None:
      return result
    return None
  
  @classmethod
  def create_server_user(cls,server_user):
    query1 = """SET @last_server_id =last_insert_id();"""
    DatabaseConnection.execute_query(query1)
    query2="""INSERT INTO server_user(rol, user_id, server_id) VALUES ("Admin", %(user_id)s, @last_server_id);"""
    params = server_user.__dict__
    DatabaseConnection.execute_query(query2, params = params)
  
  @classmethod
  def join_server(cls,server_user):
    query="""INSERT INTO server_user(rol, user_id, server_id) VALUES ("Common", %(user_id)s, %(server_id)s);"""
    params = server_user.__dict__
    DatabaseConnection.execute_query(query, params = params)