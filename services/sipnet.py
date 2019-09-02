from service import Service


class Sipnet(Service):
    def send_sms(self):
        self.session.get('https://register.sipnet.ru/cgi-bin/exchange.dll/RegisterHelper', params={'oper': 9, 'phone': self.formatted_phone})
