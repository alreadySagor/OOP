class Phone:
    # Sobar jonno ba sob phone er jonno eki. Sob phone china te toiri eta bojhate
    manufactured = 'China'

    # অন্যান্য ল্যাঙ্গুয়েজ এ দেয় constructor হিসেবে আর পাইথন এ দেয় __init__ হিসেবে
    # মনে করি আমি একটি ফোন বানাবো, ফোনটির গঠন একি থাকবে (সকল ফোনের গঠন প্রায় একি) শুধু মালিক, কোম্পানি, মূল্য, কালার এগুলা আলাদা থাকবে
    # মনে করি আমি একটি গাড়ি বানাবো, সকল গাড়ির গঠন একি থাকে কিন্তু ব্র্যান্ড, ফিচারস এগুলা আলাদা আলাদা হয়ে থাকে ।
    # এটি একটি ফরমা বা ছাঁচ এর ন্যায় কাজ করে

    # Constructor. object gulake construct korteche/korche
    # object তৈরি হওয়ার সাথে সাথেই অটো কল হয়
    def __init__(self, owner, brand, price):
        # self ta hocche bortoman object , self.owner namer ei attribute tate parameter hisebe prapto ei owner (value/maan) ta save hocche
        self.owner = owner # প্যারামিটার হিসেবে যে owner টা আসবে সেটা
        # self ta hocche bortoman object , self.brand namer ei attribute tate parameter hisebe prapto ei brand (value/maan) ta save hocche
        self.brand = brand # প্যারামিটার হিসেবে যে brand টা আসবে সেটা
        # self ta hocche bortoman object , self.price namer ei attribute tate parameter hisebe prapto ei price (value/maan) ta save hocche
        self.price = price # প্যারামিটার হিসেবে যে price টা আসবে সেটা


    def send_sms(self, phone, sms):
        text = f'sending to: {phone} {sms}'
        print(text)

my_phone = Phone('kala Chan', 'Oppo', 9800)
# print(my_phone)

print(my_phone.ownar, my_phone.brand, my_phone.price)

my_phone = Phone('Dhola Chan', 'Xiaomi', 18100)
print(my_phone.ownar, my_phone.brand, my_phone.price)

her_phone = Phone('She Kala Chan er Jaan', 'Iphone', 100000)
print(her_phone.ownar, her_phone.brand, her_phone.price)

me = my_phone.send_sms(1234, 'Teka diye kinchi')
her = her_phone.send_sms(9876, 'Amio Teka diye kinchi')

dad_phone = Phone('Abba', 'Nokia', 3000)
print(dad_phone.ownar, dad_phone.brand, dad_phone.price)

# একই ক্লাস কে কল করছি, কল করার সময় তার __init__ এর মদ্ধে আমরা যেই প্যারামিটার গুলা দিচ্ছি সেটার উপর ডিপেন্ড করে সে আমাদেরকে নতুন একটা instance দিচ্ছে