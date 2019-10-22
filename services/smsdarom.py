from service import Service


class Smsdarom(Service):
    def send_sms(self):
        self.session.get('https://go.smsdarom.ru/auth/wait/sms/' + self.formatted_phone, params={'from_reg': '1'})
