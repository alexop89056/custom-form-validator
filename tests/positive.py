import unittest
from app import app


class TestFormPositive(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_user_form(self):
        data = {
            'user_email': 'dsadsa@gmail.com',
            'user_phone': '+7 123 456 78 90',
            'user_text': 'dsadasdsa'
        }
        response = self.app.post('/get-form', data=data)
        exist_result = response.data.decode('utf-8').replace('\n', '').replace(' ', '')
        self.assertEqual(exist_result, '{"form_name":"OrderForm"}')

    def test_post_form(self):
        data = {
            'post_email': 'dasdsa@mail.ru',
            'post_phone': '+7 291 456 78 20',
            'post_text': 'dsadsadas'
        }
        response = self.app.post('/get-form', data=data)
        exist_result = response.data.decode('utf-8').replace('\n', '').replace(' ', '')
        self.assertEqual(exist_result, '{"form_name":"PostForm"}')

    def test_register_form(self):
        data = {
            'reg_email': 'dasdasdsa@mail.ru'
        }
        response = self.app.post('/get-form', data=data)
        exist_result = response.data.decode('utf-8').replace('\n', '').replace(' ', '')
        self.assertEqual(exist_result, '{"form_name":"RegisterForm"}')

    def test_lead_form(self):
        data = {
            'lead_email': 'dasasdasasdas@mail.ru',
            'lead_phone': '+7 091 200 78 20'

        }
        response = self.app.post('/get-form', data=data)
        exist_result = response.data.decode('utf-8').replace('\n', '').replace(' ', '')
        self.assertEqual(exist_result, '{"form_name":"LeadForm"}')

    def test_additional_args(self):
        data = {
            'user_email': 'dsadsa@gmail.com',
            'user_phone': '+7 123 456 78 90',
            'user_text': 'dsadasdasasd',
            'user_age': '25'

        }
        response = self.app.post('/get-form', data=data)
        exist_result = response.data.decode('utf-8').replace('\n', '').replace(' ', '')
        self.assertEqual(exist_result, '{"form_name":"OrderForm"}')

