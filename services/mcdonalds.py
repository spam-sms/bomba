from service import Service


class McDonalds(Service):
    def send_sms(self):
    phone = f'8({self.formatted_phone[1:4]}){self.formatted_phone[4:7]}-{self.formatted_phone[7:9]}-{self.formatted_phone[9:11]}'
        self.session.post('http://smsgorod.ru/sendsms.php',
                          data={'number': phone})
