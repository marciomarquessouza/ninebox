# services/global-data/project/__init__.py


import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

# instantiate the app
app = Flask(__name__)

# set config
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

# instantiate the db
db = SQLAlchemy(app)


# model
class Department(db.Model):
    """Departments and company divisions"""
    __tablename__ = "departments"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=True)
    description = db.Column(db.String(4000), nullable=False)
    company_code_01 = db.Column(db.String(255), nullable=False)
    company_code_02 = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, name, description, company_code_01, company_code_02, is_active):
        self.name = name
        self.description = description
        self.company_code_01 = company_code_01
        self.company_code_02 = company_code_02
        self.is_active = is_active


# routes
@app.route('/global-data/ping', methods=['GET'])
def ping_route():
    return jsonify({
        'status': 'success',
        'message': '...pong'
    })
