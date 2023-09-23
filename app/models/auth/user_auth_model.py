from ...database import DatabaseConnection

class UserAuth:
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
  def is_registered(cls, user):
    query = """SELECT user_id FROM users
    WHERE user_name = %(user_name)s and password = %(password)s"""
    params = user.__dict__
    result = DatabaseConnection.fetch_one(query, params=params)
    
    if result is not None:
      return True
    return False
  
  @classmethod
  def get_user_by_name(cls, user):
    query = """SELECT * FROM users
    WHERE user_name = %(user_name)s"""
    params = user.__dict__
    result = DatabaseConnection.fetch_one(query, params=params)

    if result is not None:
        return cls(
        user_id = result[0],
        user_name = result[4],
        password = result[5],
        email = result[3],
        first_name = result[1],
        last_name = result[2],
        date_of_birth = result[6]
        )
    return None

  @classmethod
  def after_loggin(cls,user):
    query = """SELECT user_id FROM users
    WHERE user_name = %(user_name)s"""
    params = user.__dict__
    result = DatabaseConnection.fetch_one(query, params=params)
    if result is not None:
        return cls(
        user_id = result[0])