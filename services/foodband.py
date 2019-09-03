import random
from service import Service


class Foodband(Service):
    def send_sms(self):
        self.session.post('https://foodband.ru/', data={'event': 'regsendcode', 'phone': self.formatted_phone[1:], 'session': random.randint(100000, 999999), 'g-recaptcha-response': ''})
