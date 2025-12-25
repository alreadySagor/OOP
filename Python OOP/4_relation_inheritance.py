class Gadget:
    def __init__(self, brand, price, color, origin):
        self.brand = brand
        self.price = price
        self.color = color
        self.origin = origin

    def run(self):
        return f'Runnig Device: {self.brand}'
    
class Laptop:
    def __init__(self, memory, ssd):
        self.memory = memory
        self.ssd = ssd
    
    def coding(self):
        return f'Learning python and practicing'
    
class Phone(Gadget): # Gadget and Phone er moddhe Relation make korlam 
# class Phone:
    def __init__(self, brand, price, color, origin, dual_sim):
        self.dual_sim = dual_sim
        super().__init__(brand, price, color, origin)

    def phone_call(self, phone, text):
        return f'Sending SMS to: {phone} with: {text}'
    
    def __repr__(self):
        return f'phone: {self.brand}, {self.price}, {self.origin}, {self.dual_sim}'

class Camera:
    def __init__(self, pixel):
        self.pixel = pixel
    def change_lens(self):
        pass


# Inheritance

my_phone = Phone('iphone', 120000, 'silver', 'china', True) # mone kori dual sim = true
# my_phone.phone_call()
print(my_phone.brand)
print(my_phone)
# ekhane sudhu true pabo baki properties gula pacchi na
# baki properties gula pete gele amader ke "Gadget & Phone" er moddhe
# relation make korte hobe
