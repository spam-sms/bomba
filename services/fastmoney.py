# -*- coding: utf-8 -*-
from service import Service
import random
import string


class FastMoney(Service):
    def send_sms(self):
        if self.country_code == 'ru':
            passwd = ''.join(random.choice(string.ascii_letters) for _ in range(9))
            self.session.post('https://fastmoney.ru/auth/registration',
                              data={'RegistrationForm[username]': '+' + self.formatted_phone,
                                    'RegistrationForm[password]': passwd, 'RegistrationForm[confirmPassword]': passwd,
                                    'yt0': 'Регистрация'})
