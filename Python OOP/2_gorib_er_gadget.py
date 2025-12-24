class Laptop:
    def __init__(self, brand, price, color, memory):
        self.brand = brand
        self.price = price
        self.color = color
        self.memory = memory

    def run(self):
        return f'Running laptop: {self.brand}'
            
    def coding(self):
        return f'Learning python and practicing'
    
class Phone:
    def __init__(self, brand, price, color, dual_sim):
        self.brand = brand
        self.price = price
        self.color = color
        self.dual_sim = dual_sim

    def run(self):
        return f'Phone chalais na'
    
    def phone_call(self, number, text):
        return f'Sending SMS to: {number} with: {text}'
    
    def __repr__(self):
        return f'phone: {self.dual_sim}'
    
class Camera:
    def __inti__(self, brand, price, color, pixel):
        self.brand = brand
        self.price = price
        self.color = color
        self.pixel = pixel

    def run(self):
        pass

    def camera_lens(self):
        pass


""" 
    Eta theke idea jeita pailam
        -> kichu common functionality & kichu uncommon functionality thake
        -> kichu commom behavior / attributes & kichu nuncommom behavior / attributes thake 
  
Ei common and uncommon jinish take ekta chomotkarvabe organize kora
jay jate repeatation ta na hoy (same code gula amra bar bar na likhi)

etar jonno special ekta relationship ache jar naam [Inheritance]
check inheritance.py

"""