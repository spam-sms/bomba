from service import Service


class Ozon(Service):
    def send_sms(self):
        self.session.post('https://www.ozon.ru/api/composer-api.bx/_action/fastEntry', json={'phone': self.formatted_phone, 'otpId': '0'})

