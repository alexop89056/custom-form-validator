import re
from app.schema import base_regex


class Email:
    @staticmethod
    def validate_data(email):
        regex = re.compile(base_regex.email_regex)
        return True if re.match(regex, email) else False

    @staticmethod
    def to_string():
        return 'email'


class Phone:
    @staticmethod
    def validate_data(phone):
        regex = re.compile(base_regex.phone_regex)
        return True if re.match(regex, phone) else False

    @staticmethod
    def to_string():
        return 'phone'


class Date:
    @staticmethod
    def validate_data(date):
        regex = re.compile(base_regex.date_regex)
        return True if re.match(regex, date) else False

    @staticmethod
    def to_string():
        return 'date'


class Text:
    @staticmethod
    def validate_data(text):
        return True

    @staticmethod
    def to_string():
        return 'text'


class BaseForm:
    validators = [Date, Phone, Email, Text]

    def __init__(self):
        self.email = Email()
        self.phone = Phone()
        self.date = Date()
        self.text = Text()

    def get_custom_data_type(self, data: dict):
        result_dict = {}
        for key, value in data.items():

            for validator in self.validators:
                result = validator.validate_data(value)
                if result:
                    result_dict[key] = validator.to_string()
                    break

        return result_dict
