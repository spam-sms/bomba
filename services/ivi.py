from service import Service


class Ivi(Service):
    def send_sms(self):
        self.session.post('https://api.ivi.ru/mobileapi/user/register/phone/v6', data={'phone': self.formatted_phone})
