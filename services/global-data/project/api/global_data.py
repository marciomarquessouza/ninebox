# services/global-data/project/api/global_data.py

from flask import Blueprint, jsonify

global_data_blueprint = Blueprint('global_data', __name__)


@global_data_blueprint.route('/global_data/ping', methods = ['GET'])
def ping_route():
    return jsonify({
        'status': 'success',
        'message': '...pong'
    })
