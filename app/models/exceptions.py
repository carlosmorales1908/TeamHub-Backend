from flask import jsonify
from werkzeug.exceptions import HTTPException

class NotFound(HTTPException):
  """
  NotFound model class
  """
  def __init__(self, description = "Error: NotFound"):
    """
    Constructor method
    """
    super().__init__(description)
    self.code = 404

  def get_response(self):
    """
    Method that return an error in json format
    """
    response = jsonify({
    'error': {
    'name': "Not Found",
    'code': self.code,
    'description': self.description,
    }
    })
    return response

class BadRequest(HTTPException):
  """
  BadRequest model class
  """
  def __init__(self, description = "Error: BadRequest"):
    """
    Constructor method
    """
    super().__init__(description)
    self.code = 400

  def get_response(self):
    """
    Method that return an error in json format
    """
    response = jsonify({
    'error': {
    'name': "Bad Request",
    'code': self.code,
    'description': self.description,
    }
    })
    return response

class Forbidden(HTTPException):
  """
  Forbidden model class
  """
  def __init__(self, description = "Error: Forbidden"):
    """
    Constructor method
    """
    super().__init__(description)
    self.code = 403

  def get_response(self):
    """
    Method that return an error in json format
    """
    response = jsonify({
    'error': {
    'name': "Forbidden",
    'code': self.code,
    'description': self.description,
    }
    })
    return response

class ServerError(HTTPException):
  """
  Forbidden model class
  """
  def __init__(self, description = "Error: ServerError"):
    """
    Constructor method
    """
    super().__init__(description)
    self.code = 500

  def get_response(self):
    """
    Method that return an error in json format
    """
    response = jsonify({
    'error': {
    'name': "Server Error",
    'code': self.code,
    'description': self.description,
    }
    })
    return response