# services/global-data/project/tests/test_config.py

import os
import unittest

from flask import current_app
from flask_testing import TestCase
from project import create_app

app = create_app()


class TestDevlopmentConfig(TestCase):
    """Test development config"""

    def create_app(self):
        app.config.from_object('project.config.DevConfig')
        return app

    def test_app_is_development(self):
        """check the development config"""
        self.assertTrue(app.config['SECRET_KEY'] == 'my_precious')
        self.assertFalse(current_app is None)
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] ==
            os.environ.get('DATABASE_URL')
        )


class TestTestingConfig(TestCase):
    """Test testing config"""

    def create_app(self):
        app.config.from_object('project.config.TestConfig')
        return app

    def test_app_is_testing(self):
        """check the testing config"""
        self.assertTrue(app.config['SECRET_KEY'] == 'my_precious')
        self.assertTrue(app.config['TESTING'])
        self.assertFalse(app.config['PRESERVE_CONTEXT_ON_EXCEPTION'])
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] ==
            os.environ.get('DATABASE_URL_TEST')

        )


class TestProductionConfig(TestCase):
    """Test production config"""

    def create_app(self):
        app.config.from_object('project.config.ProdConfig')
        return app

    def test_app_is_production(self):
        """check the production config"""
        self.assertTrue(app.config['SECRET_KEY'] == 'my_precious')
        self.assertFalse(app.config['TESTING'])


if __name__ == '__main__':
    unittest.main()

