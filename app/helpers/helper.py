from ..models.exceptions import BadRequest, Forbidden, ServerError
from ..models.user_model import User
from ..models.servers_models import Server
from datetime import date

def validate_dob(dob):
  hoy = date.today()
  dob = date.fromisoformat(dob)
  edad = hoy.year - dob.year - ((hoy.month, hoy.day) < (dob.month, dob.day))
  if edad <= 0:
    raise BadRequest(description= "Invalid data for Birthday Date.")

def validate_is_string(attribute):
  if not isinstance(attribute, str):
    raise BadRequest(description= f"{attribute} must be a string.")
  
def validate_is_int(attribute):
  if not isinstance(attribute, int):
    raise BadRequest(description= f"{attribute} must be an integer.")

def validate_len(attribute):
  if len(attribute) < 4:
    raise BadRequest(description = f"{attribute} must have more than 4 characters")
    
def validate_len_password(password):
  if len(password) < 8:
    raise BadRequest(description = f"password must have more than 8 characters")
  
def validate_len_message(message):
  if len(message) < 1:
    raise BadRequest(description = f"message must have more than 1 characters")

def validate_value_in_data(value,data):
  if not value in data:
    raise Forbidden(description = f"{value} is missing to create User")

def invalid_data(value,data):
  if value in data:
    raise BadRequest(description=f"{value} must not be passed as a parameter")

def verify_username(user):
  if User.verify_username(user):
    raise BadRequest(description="user_name already exist")
  
def verify_email(user):
  if User.verify_email(user):
    raise BadRequest(description="email already exist")

def verify_servername(server):
  if Server.verify_servername(server):
    raise BadRequest(description="server_name already exist")