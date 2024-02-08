import json
import unittest

from app import app


class NumberApiTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

        self.cases = {'3': 'Type 1', '5': 'Type 2', '15': 'Type 3'}

    def test_add_number(self):
        for k, _ in self.cases.items():
            response = self.app.post('/add_number',
                                     data=json.dumps({'number': int(k)}),
                                     content_type='application/json')

            self.assertEqual(response.status_code, 200)

    def test_add_number_fail(self):
        response = self.app.post('/add_number',
                                 data=json.dumps({'number': 'fail'}),
                                 content_type='application/json')

        self.assertEqual(response.status_code, 400)

    def test_get_number(self):

        for k, v in self.cases.items():
            response = self.app.get(f'/get_number/{int(k)}')

            data = json.loads(response.data)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data['number'], int(k))
            self.assertEqual(data['value'], v)

    def test_get_number_fail(self):
        for k, v in self.cases.items():
            response = self.app.get('/get_number/20')

            # The message is really not important here

            self.assertEqual(response.status_code, 404)

    def test_get_all(self):
        response = self.app.get('/get_all')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, self.cases)


if __name__ == '__main__':
    unittest.main()
