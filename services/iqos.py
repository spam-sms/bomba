# -*- coding: utf-8 -*-
from service import Service


class Iqos(Service):
    def send_sms(self):
        nam9e = ''.join(random.choice(string.ascii_letters) for _ in range(6))
        nam8e = ''.join(random.choice(string.ascii_letters) for _ in range(6))
        self.session.post('https://ube.pmsm.org.ru/esb/iqos-reg/submission', json={
            'data': {'firstName': self.sms_text, 'lastName': 'Петров', 'phone': self.formatted_phone,
                     'email': nam9e + '@gmail.com', 'password': nam8e,
                     'passwordConfirm': nam8e}})
