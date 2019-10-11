from service import Service
import random
import string



class Maxidom(Service):
    def send_sms(self):
        if self.country_code == 'ru':
            email = ''.join(random.choice(string.ascii_letters) for _ in range(9)) + '@mail.ru'
            phone = f'8({self.phone[1:4]}){self.phone[4:7]}-{self.phone[7:9]}-{self.phone[9:11]}'
            self.session.get('https://www.maxidom.ru/ajax/doRegister.php',
                             params={'send_code_again': 'Y', 'phone': phone,
                                     'email': email, 'code_type': 'phone'})
