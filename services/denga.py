import random
import string

from service import Service


class Denga(Service):
    def send_call(self):
        name = ''.join(random.choice(string.ascii_letters) for _ in range(6))
        passwd = ''.join(random.choice(string.ascii_letters) for _ in range(9))
        self.session.get('https://online.denga.ru/admin/api/json/registration',
                         data={'phone': self.formatted_phone, 'email': name + '@gmail.com',
                               'password': passwd, 'passwordConfirmation': passwd})
