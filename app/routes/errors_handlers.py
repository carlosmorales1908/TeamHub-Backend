from flask import Blueprint
from ..models.exceptions import NotFound, BadRequest

errors = Blueprint("errors", __name__)

@errors.app_errorhandler(NotFound)
def handle_bad_request(error):
    return error.get_response()

@errors.app_errorhandler(BadRequest)
def handle_bad_request(error):
    return error.get_response()