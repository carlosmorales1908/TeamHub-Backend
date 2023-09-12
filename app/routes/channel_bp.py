from flask import Blueprint
from ..controllers.channel_controller import ChannelController

channel_bp = Blueprint('channel_bp', __name__)

channel_bp.route("/channels/<int:channel_id>", methods = ['GET'])(ChannelController.get_channel)
# channel_bp.route("/all_channels/<int:server_id>", methods = ['GET'])(ChannelController.get_channels)
channel_bp.route("/channels", methods = ['POST'])(ChannelController.create_channel)
channel_bp.route("/channels/<int:channel_id>", methods = ['PUT'])(ChannelController.update_channel)
channel_bp.route("/channels/<int:channel_id>", methods=['DELETE'])(ChannelController.delete_channel)

channel_bp.route("/show_channels", methods = ['GET'])(ChannelController.show_channels_server)