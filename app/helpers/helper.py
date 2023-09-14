from ..models.exceptions import BadRequest, Forbidden, ServerError
from ..models.user_model import User
from ..models.servers_models import Server
from datetime import date

def validate_dob(dob):
  """
  Validate that the date of birth doesn't exceed the current year
  """
  hoy = date.today()
  dob = date.fromisoformat(dob)
  edad = hoy.year - dob.year - ((hoy.month, hoy.day) < (dob.month, dob.day))
  if edad <= 0:
    raise BadRequest(description= "Invalid data for Birthday Date.")

def validate_is_string(data):
  """
  Validate if a data is a string
  """
  if not isinstance(data, str):
    raise BadRequest(description= f"{data} must be a string.")
  
def validate_is_int(data):
  """
  Validate if a data is a integer
  """
  if not isinstance(data, int):
    raise BadRequest(description= f"{data} must be an integer.")

def validate_len(data):
  """
  Validate if the data len is less than 3
  """
  if len(data) < 3:
    raise BadRequest(description = f"{data} must have more than 4 characters")
    
def validate_len_password(password):
  """
  Validate if the password len is less than 3
  """
  if len(password) < 8:
    raise BadRequest(description = f"password must have more than 8 characters")
  
def validate_len_message(message):
  """
  Validate if the password len is less than 1
  """
  if len(message) < 1:
    raise BadRequest(description = f"message must have more than 1 characters")

def validate_value_in_data(value,data):
  """
  Validate if value is in data
  """
  if not value in data:
    raise Forbidden(description = f"{value} is missing to create User")

def invalid_data(value,data):
  """
  Validate if value isn't in data
  """
  if value in data:
    raise BadRequest(description=f"{value} must not be passed as a parameter")

def verify_username(user):
  """
  Validate if a user name already exist
  """
  if User.verify_username(user):
    raise BadRequest(description="user_name already exist")
  
def verify_email(user):
  """
  Validate if a email already exist
  """
  if User.verify_email(user):
    raise BadRequest(description="email already exist")

def verify_servername(server):
  """
  Validate if a server name already exist
  """
  if Server.verify_servername(server):
    raise BadRequest(description="server_name already exist")