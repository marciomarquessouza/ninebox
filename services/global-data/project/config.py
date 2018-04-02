# services/global-data/project/config.py

import os


class BasicConfig():
    """Basic Configuration"""
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'my_precious'


class DevConfig(BasicConfig):
    """Development Configuration"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class TestConfig(BasicConfig):
    """Test Configuration"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL_TEST')


class ProdConfig(BasicConfig):
    """Produciton Configuration"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
