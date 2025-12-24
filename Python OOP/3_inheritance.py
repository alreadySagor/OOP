# base class/parent class
# Relationship make korbo relation_inheritance er moddhe
class Gadget: # eta base class ba parent class
    # common attribute gula ekhane niye ashlam
    def __init__(self, brand, price, color, origin):
        self.brand = brand
        self.price = price
        self.color = color
        self.origin = origin

    # common functionality/method
    def run(self):
        return f'Runnig laptop: {self.brand}'

# parent/base class er biporit hocche derived class/child class
# egulate uncommon attirbute + functionalities thake.

class Laptop:
    # common gula base class e niye gechi tai ekhane rakhlam na (comment kore rakhlam)
    def __init__(self, memory, ssd): # brand, price, color
        # self.brand = brand
        # self.price = price
        # self.color = color
        self.memory = memory
        self.ssd = ssd
    # def run(self):
    #     return f'Runnig laptop: {self.brand}'
    
    def coding(self):
        return f'Learning python and practicing'
    
class Phone:
    def __init__(self, dual_sim): # brand, price, color,
        # self.brand = brand
        # self.price = price
        # self.color = color
        self.dual_sim = dual_sim

    # def run(self):
    #     return f'phone tipa tipi kore'
    
    def phone_call(self, phone, text):
        return f'Sending SMS to: {phone} with: {text}'
    
    def __repr__(self):
        return f'phone: {self.dual_sim}'

class Camera:
    def __init__(self, pixel): # brand, price, color,
        # self.brand = brand
        # self.price = price
        # self.color = color
        self.pixel = pixel

    # def run(self):
    #     pass

    def change_lens(self):
        pass

# f = Phone(True)
# print(f.phone_call(4343, 'ur3'))
# print(Phone(True))
# print(f)
""" 
    Soja banglay Inheritance [Uttoradhikar/ Uttoradhikari]

	(Uttoradhikar shutre egula use korte pari)
    basay ekta tv ache jeita ami kini nai, tobuo ami dekhte pari, onnorao dekhte pare
    basay ekta dine_in_table ache jeita amar baba kinche, setao ami use korte pari, barikao pare
    Abar amar ekta boi ache jeita baki rao use kore[nijer taka diya kinchi]

ei khaneu jei kaajta korbo amra common functionality gula ekta class er moddhe bosai dibo

etake onek khetre bola hoy: Base class/parent class
            / (common attribute + functionality class --> bojhar subidharthe eita bolte pari)

ei gular opposite gulake bole:
    --> Derived class/child class (uncommon attribute + functinality)

sob khetre korbo na, jegular sathe mill ache seigular khetre korbo(functionality)
 jemon gorib_er_gadget er onek functionality er moddhe mil ache
"""