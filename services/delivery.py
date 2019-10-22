from service import Service


class Delivery(Service):
    def send_sms(self):
        self.session.post('https://krasnodar.delivery-club.ru/ajax/user_otp', data={'phone': self.formatted_phone})
