from flask import Blueprint
from ..models.exceptions import CustomException

errors = Blueprint("errors", __name__)

@errors.app_errorhandler(CustomException)
def handle_bad_request(error):
    return error.get_response()