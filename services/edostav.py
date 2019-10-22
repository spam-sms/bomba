from service import Service


class Edostav(Service):
    def send_sms(self):
        self.session.post('https://krasnodar.edostav.ru/site/CheckAuthLogin', data={'phone_or_email': self.formatted_phone})
