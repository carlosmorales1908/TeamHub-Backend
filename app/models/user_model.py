from ..database import DatabaseConnection
# from datetime import  datetime

class User:
  """
  User model class
  """
  def __init__(self, **kwargs):
    """
    Constructor method
    """
    self.user_id = kwargs.get('user_id')
    self.user_name = kwargs.get('user_name')
    self.password = kwargs.get('password')
    self.email = kwargs.get('email')
    self.first_name = kwargs.get('first_name')
    self.last_name = kwargs.get('last_name')
    self.date_of_birth = kwargs.get('date_of_birth')
    self.profile_picture = kwargs.get('profile_picture')
  
  def serialize(self):
    """
    Serialize object representation
      Returns:
        dict: Object representation
    """
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
    """
    Check if a user is registered:
    Args:
      - user: User object
    Return:
      - tuple with user id or
      - False
    """
    query = """SELECT user_id FROM users
    WHERE user_name = %(user_name)s and password = %(password)s"""
    params = user.__dict__
    result = DatabaseConnection.fetch_one(query, params=params)
    if result is not None:
        return True
    return False
  
  @classmethod
  def get_user_by_name(cls, user):
    """
    Get a user by user_name:
    Args:
      - user: User object
    Return:
      - User object or
      - None
    """
    query = """SELECT * FROM users
    WHERE user_name = %(user_name)s"""
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
        date_of_birth = result[6]
        )
    return None
  
  @classmethod
  def get_user(cls, user):
    """
    Get a user by user_id
    Args:
      - user: User object
    Return:
      - User object or
      - None
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
        date_of_birth = result[6]
      )
    return None
  
  @classmethod
  def create_user(cls,user):
    """
    Create a user
    Args:
      - user: User object
    """
    query = """INSERT INTO users(first_name,last_name,email,user_name,password,date_of_birth) 
      VALUES (%(first_name)s,%(last_name)s,%(email)s,%(user_name)s,%(password)s,%(date_of_birth)s);"""
    params = user.__dict__
    DatabaseConnection.execute_query(query, params)

  @classmethod
  def update_user(cls,user):
    """
    Update a user
    Args:
      - user: User object
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
  
  @classmethod
  def delete(cls, user):
    """
    Delete a user by user_id
    Args:
      - user: User object
    """
    query = "DELETE FROM users WHERE user_id = %s"
    params = user.user_id,
    DatabaseConnection.execute_query(query, params=params)
  
  @classmethod
  def exists(cls,user_id):
    """
    Check if a user exist by user_id
    Args:
      - user_id
    Return:
      - boolean
    """
    query = """SELECT * FROM users WHERE user_id = %s"""
    params = user_id,
    result = DatabaseConnection.fetch_one(query, params=params)
    return bool(result)
  
  @classmethod
  def verify_username(cls,user):
    """
    Check if a user_name already exist in the DB
    Args:
      - user: User object
    Return:
      - boolean
    """
    query = """SELECT user_id FROM users 
    WHERE user_name = %(user_name)s;"""
    params = user.__dict__
    result = DatabaseConnection.fetch_one(query, params=params)
    return bool(result)
  
  @classmethod
  def verify_email(cls,user):
    """
    Check if a email already exist in the DB
    Args:
      - user: User object
    Return:
      - boolean
    """
    query = """SELECT user_id FROM users 
    WHERE email = %(email)s;"""
    params = user.__dict__
    result = DatabaseConnection.fetch_one(query, params=params)
    return bool(result)