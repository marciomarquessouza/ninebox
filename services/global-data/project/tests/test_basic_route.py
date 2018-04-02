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


if __name__ == '__main__':
    unittest.main()
