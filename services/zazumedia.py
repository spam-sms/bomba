from service import Service


class Zazumedia(Service):
    def send_sms(self):
        self.session.get('https://go.zazumedia.ru/auth/wait/sms/' + self.formatted_phone, params={'from_reg': '1'})
