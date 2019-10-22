from service import Service


class Zdesapteka(Service):
    def send_sms(self):
        phone = f'+{self.formatted_phone[0]} ({self.formatted_phone[1:4]}) {self.formatted_phone[4:7]}-{self.formatted_phone[7:9]}-{self.formatted_phone[9:11]}'
        self.session.post('https://zdesapteka.ru/ajax/smsconfirmation.php', data={'sessid': 'f8ccc39dae416f1f070d77a3ce8eaeba', 'phoneNumber': phone})
