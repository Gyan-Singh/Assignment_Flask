import unittest
from flask_testing import TestCase
import openai
from main import app

class AppTestCase(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        openai.api_key = "sk-.."
        return app

    def test_homepage_rendering(self):
        response = self.client.get('/')
        statuscode=response.status_code
        self.assertEqual(statuscode, 200)


    def test_resultpage_rendering(self):
        response = self.client.get('/success')
        statuscode=response.status_code
        self.assertEqual(statuscode, 200)


    def test_chatgpt_api_integration(self):
        with self.client:
            response = self.client.post('/success', data={'Query': 'Hello'})
            self.assert200(response)
            self.assertIn(b"Query", response.data)
            self.assertIn(b"Result", response.data)
            # Add more assertions to validate the expected response from the ChatGPT API


if __name__ == '__main__':
    unittest.main()
