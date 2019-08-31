# -*- coding: utf-8 -*-
from service import Service
import random
import string


class Iqos(Service):
    def send_sms(self):
        emailrand = ''.join(random.choice(string.ascii_letters) for _ in range(6))
        passwd = ''.join(random.choice(string.ascii_letters) for _ in range(9))
        self.session.post('https://ube.pmsm.org.ru/esb/iqos-reg/submission', json={
            'data': {'firstName': self.sms_text, 'lastName': 'Петров', 'phone': self.formatted_phone,
                     'email': emailrand + '@gmail.com', 'password': passwd,
                     'passwordConfirm': passwd}})
