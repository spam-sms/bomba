from service import Service


class Dostavista(Service):
    def send_sms(self):
        if self.country_code == 'ru':
            phone = f'{self.formatted_phone[1:4]} {self.formatted_phone[4:7]}-{self.formatted_phone[7:9]}-{self.formatted_phone[9:11]}'
            cookies = self.session.get('https://dostavista.ru/').cookies
            self.session.post('https://dostavista.ru/backend/send-verification-sms', cookies=cookies, data={'phone': phone})
