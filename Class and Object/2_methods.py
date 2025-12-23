class Phone:
    price = 19000
    color = 'blue'
    brand = 'samsung'
    features = ['camera', 'speaker', 'hammer']

    # selt --> bortoman object ke bojhay
    def call(self): # eti ekti method (normally eti ekti function kintu jehetu class er vitor etake add korechi/likhechi tai ekhon eti ekti method) and class er vitore function thakar fole 1 ta extra parameter amake dite hobe seta self
        print('calling one person')
    
    def send_sms(self, phone, sms):
        text = f'sending SMS to {phone} and message: {sms}'
        return text
    
my_phone = Phone()
print(my_phone.features)
my_phone.call()
result = my_phone.send_sms(43423, 'Missy, I missed to miss you')
print(result)