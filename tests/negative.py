import unittest
from app import app


class TestFormNegative(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_form_wrong_phone(self):
        data = {
            'user_email': 'dsadsa@gmail.com',
            'user_phone': 'dasdasdsa',
            'user_text': 'dsadasdsa'
        }
        response = self.app.post('/get-form', data=data)
        exist_result = response.data.decode('utf-8').replace('\n', '').replace(' ', '')
        self.assertEqual(exist_result, '{"user_email":"email","user_phone":"text","user_text":"text"}')

    def test_form_wrong_email(self):
        data = {
            'post_email': 'dasdsa@dasdasdsadasdasad',
            'post_phone': '+7 291 456 78 20',
            'post_text': 'dsadsadas'
        }
        response = self.app.post('/get-form', data=data)
        exist_result = response.data.decode('utf-8').replace('\n', '').replace(' ', '')
        self.assertEqual(exist_result, '{"post_email":"text","post_phone":"phone","post_text":"text"}')

    def test_no_enough_args(self):
        data = {
            'post_email': 'dasdsa@dasdasdsadasdasad',
            'post_phone': '+7 291 456 78 20'
        }
        response = self.app.post('/get-form', data=data)
        exist_result = response.data.decode('utf-8').replace('\n', '').replace(' ', '')
        self.assertEqual(exist_result, '{"post_email":"text","post_phone":"phone"}')

    def test_null(self):
        response = self.app.post('/get-form')
        exist_result = response.data.decode('utf-8')
        self.assertEqual(exist_result, '{\n  "message": "No data was provided"\n}\n')

