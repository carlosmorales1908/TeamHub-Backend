from flask import Blueprint

from ..controllers.auth_controller import UserAuthController

auth_bp = Blueprint('auth_bp', __name__)

auth_bp.route('/login', methods=['POST'])(UserAuthController.login)
auth_bp.route('/profile', methods=['GET'])(UserAuthController.show_profile)
auth_bp.route('/logout', methods=['GET'])(UserAuthController.logout)