import json
import unittest

from app import app


class NumberApiTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_save_number(self):
        response = self.app.post('/numbers',
                                 data=json.dumps({'number': 15}),
                                 content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['value'], "Type 3")

    def test_get_number_value(self):
        self.app.post('/numbers',
                      data=json.dumps({'number': 15}),
                      content_type='application/json')
        response = self.app.get('/numbers/15')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['value'], "Type 3")

    def test_get_all_numbers(self):
        self.app.post('/numbers',
                      data=json.dumps({'number': 3}),
                      content_type='application/json')
        self.app.post('/numbers',
                      data=json.dumps({'number': 5}),
                      content_type='application/json')
        response = self.app.get('/numbers')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('3', data)
        self.assertIn('5', data)

    def test_404_for_nonexistent_number(self):
        response = self.app.get('/numbers/999')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
