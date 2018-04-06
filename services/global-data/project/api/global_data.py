# services/global-data/project/api/global_data.py

from flask import Blueprint, jsonify, request
from sqlalchemy import exc

from project.api.models import Person
from project import db

global_data_blueprint = Blueprint('global_data', __name__)


@global_data_blueprint.route('/global_data/ping', methods = ['GET'])
def ping_route():
    return jsonify({
        'status': 'success',
        'message': '...pong'
    })

@global_data_blueprint.route('/persons', methods=['POST'])
def add_person():
    post_data = request.get_json()
    response_object = {
        'status': 'fail',
        'message': 'Invalid payload.'
    }

    if not post_data:
        return jsonify(response_object), 400

    name = post_data.get('name')

    try:
        db.session.add(Person(name=name))
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': f'{name} was added'
        }
        return jsonify(response_object), 201
    except exc.IntegrityError as e:
        db.session.rollback()
        return jsonify(response_object), 400

