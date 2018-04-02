# services/global-data/project/tests/base.py

from flask_testing import TestCase

from project import create_app, db

app = create_app()

class BaseTestCase(TestCase):
    """Test app config and db"""

    def create_app(self):
        app.config.from_object('project.config.TestConfig')
        return app

    def setUp(self):
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
