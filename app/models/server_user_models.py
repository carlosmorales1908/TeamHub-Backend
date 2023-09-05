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