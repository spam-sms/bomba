# -*- coding: utf-8 -*-
from service import Service


class AptekaRu(Service):
    def send_sms(self):
    phone = f'+7 ({self.formatted_phone[1:4]}) {self.formatted_phone[4:7]}-{self.formatted_phone[7:9]}-{self.formatted_phone[9:11]}'
        self.session.post('https://apteka.ru/_action/auth/getForm/', data={'form[NAME]': '', 'form[PERSONAL_GENDER': '', 'form[PERSONAL_BIRTHDAY]': '', 'form[EMAIL]: '', 'form[LOGIN]': phone, 'form[PASSWORD]': '', 'get-new-password': 'Получите пароль по SMS', 'formType': 'simple', 'utc_offset': '180'})
