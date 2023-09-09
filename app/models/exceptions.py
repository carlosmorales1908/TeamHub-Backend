from flask import jsonify
from werkzeug.exceptions import HTTPException

class NotFound(HTTPException):
  def __init__(self, description = "Error: NotFound"):
    super().__init__(description)
    self.code = 404

  def get_response(self):
    response = jsonify({
    'error': {
    'name': "Not Found",
    'code': self.code,
    'description': self.description,
    }
    })
    return response

class BadRequest(HTTPException):
  def __init__(self, description = "Error: BadRequest"):
    super().__init__(description)
    self.code = 400

  def get_response(self):
    response = jsonify({
    'error': {
    'name': "Bad Request",
    'code': self.code,
    'description': self.description,
    }
    })
    return response

class Forbidden(HTTPException):
  def __init__(self, description = "Error: Forbidden"):
    super().__init__(description)
    self.code = 403

  def get_response(self):
    response = jsonify({
    'error': {
    'name': "Forbidden",
    'code': self.code,
    'description': self.description,
    }
    })
    return response

class ServerError(HTTPException):
  def __init__(self, description = "Error: ServerError"):
    super().__init__(description)
    self.code = 500

  def get_response(self):
    response = jsonify({
    'error': {
    'name': "Server Error",
    'code': self.code,
    'description': self.description,
    }
    })
    return response