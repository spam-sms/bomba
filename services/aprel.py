from service import Service


class AptekaAprel(Service):
    def send_sms(self):
        if self.country_code == 'ru':
            phone = f'{self.formatted_phone[1:10]}'
            self.session.post('https://apteka-april.ru/ajax/', data={'action': 'sendConfitmSMS', 'phone': phone})
