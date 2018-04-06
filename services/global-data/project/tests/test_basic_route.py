# services/project/tests/test_department.py

import json
import unittest

from project.tests.base import BaseTestCase


class TestRouteService(BaseTestCase):
    """Test the route tester"""

    def test_route(self):
        """test the route test (ping) """
        response = self.client.get('/global_data/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('...pong', data['message'])
        self.assertIn('success', data['status'])

    def test_add_person(self):
        with self.client:
            response = self.client.post(
                '/persons',
                data=json.dumps({
                    'name': 'marcio'
                }),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertIn('marcio was added', data['message'])
            self.assertIn('Invalid payload.', data['message'])
            self.assertIn('fail', data['status'])

    def test_add_person_invalid_json(self):
        """Ensure error is thrown if the JSON object is empty"""
        with self.client:
            response = self.client.post(
                '/persons',
                data=json.dumps({}),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Invalid payload.')

if __name__ == '__main__':
    unittest.main()
