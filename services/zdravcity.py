from service import Service


class Zdravcity(Service):
    def send_sms(self):
        phone = f'{self.formatted_phone[1:11]}'
        self.session.post('https://zdravcity.ru/ajax/sendcode.php', data={'phone': phone, 'bxsid': '', 'sms1': 'Y', 'typeAction': 'regUser'})
