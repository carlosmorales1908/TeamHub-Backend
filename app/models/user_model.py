from ..database import DatabaseConnection
from datetime import  datetime

class User:
  def __init__(self, **kwargs):
      self.user_id = kwargs.get('user_id')
      self.user_name = kwargs.get('user_name')
      self.password = kwargs.get('password')
      self.email = kwargs.get('email')
      self.first_name = kwargs.get('first_name')
      self.last_name = kwargs.get('last_name')
      self.date_of_birth = kwargs.get('date_of_birth')
      self.profile_picture = kwargs.get('profile_picture')
  
  def serialize(self):
    return {
      "user_id": self.user_id,
      "user_name": self.user_name,
      "password": self.password,
      "email": self.email,
      "first_name": self.first_name,
      "last_name": self.last_name,
      "date_of_birth": (self.date_of_birth).strftime("%d/%m/%y")
    }
  
  @classmethod
  def get_user(cls, user):
    """
    Recibe como parámetro objeto de tipo User.
    Retorna una tupla con los datos del usuario si lo encuentra
    """
    query = """SELECT * FROM users 
    WHERE user_id = %(user_id)s"""
    params = user.__dict__
    result = DatabaseConnection.fetch_one(query, params=params)

    if result is not None:
      return cls(
        user_id = result[0],
        user_name = result[1],
        password = result[2],
        email = result[3],
        first_name = result[4],
        last_name = result[5],
        date_of_birth = result[6],
      )
    return None
  
  @classmethod
  def create_user(cls,user):
    """
    Recibe como parámetro objeto de tipo User.
    """
    query = """INSERT INTO users(first_name,last_name,email,user_name,password,date_of_birth) 
      VALUES (%(first_name)s,%(last_name)s,%(email)s,%(user_name)s,%(password)s,%(date_of_birth)s);"""
    params = user.__dict__
    DatabaseConnection.execute_query(query, params)

  @classmethod
  def update_user(cls,user):
    """
    Recibe como parámetro objeto de tipo User.
    """
    query="""UPDATE users SET 
      first_name=%(first_name)s,
      last_name=%(last_name)s,
      email=%(email)s,
      user_name=%(user_name)s,
      password=%(password)s,
      date_of_birth=%(date_of_birth)s,
      profile_picture=%(profile_picture)s
      WHERE user_id=%(user_id)s;"""
    params=user.__dict__
    DatabaseConnection.execute_query(query, params=params)