# services/global-data/project/-_init__.py

import unittest

from flask.cli import FlaskGroup
from project import create_app, db
from project.api.models import Department
from project.api.models import Person
from project.api.models import Address

app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command()
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command()
def test():
    """Run the tests without the code coverage"""
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

@cli.command()
def seed_db():
    """Seed database"""
    db.session.add(Person(name='Marcio'))
    db.session.add(Address(email='marciomultimedia@gmail.com',person_id=1))
    db.session.commit()


if __name__ == '__main__':
    cli()
