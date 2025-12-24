# poly ---> many (multiple)
# morph ---> shape
"""
class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        print('Animal making some sound')

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

don = Cat('Real Don')
don.make_sound()
"""
# ekhane don.make_sound ke call korle output ashbe "Animal making some sound"
# jeita asole Cat theke asche na(Animal er sound animal vede onek hote pare jemon: dog-- ghew ghew, cat-- meow meow)
# Tai Cat er nijer kono sound nai, ekhon cat er jonno sound banale by default se super ke call korbe
# kintu amra chai na se super ke call koruk(super ke call korle Animal er kache jabe)
# tai super taake kete dilam
"""
class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        print('Animal making some sound')

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    def make_sound(self):
        print('meow meow') # ekhan theke super ke kete diyechi

don = Cat('Real Don')
don.make_sound()
"""
# ekhon etake run korle default tar kache jabe na (Animal er kache) tar nijer jeita ache seitar kache jabe


# Arekti animal add korlam Dog naame e

class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        print('Animal making some sound')

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    def make_sound(self):
        print('meow meow')

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    def make_sound(self):
        print('gheu gheu')

class Goat(Animal):
    def __init__(self, name):
        super().__init__(name)
    def make_sound(self):
        print('beh beh beh')

don = Cat('Real Don')
don.make_sound()

shepard = Dog('Local Shepard')
shepard.make_sound()

mess = Goat('L M')
mess.make_sound()

less = Goat('gora gori')

# ekta list banay fellam (Object gular)
print('-------- Loop er maddhome --------')
animals = [don, shepard, mess, less]
for animal in animals:
    animal.make_sound()


# polymorphism maane holo --> eki jinisher bivinno rup thakte pare
# jemon Cat, Dog & Goat er ekta method (same naam er(make_sound)) make_sound 
# (make_sound tintar khetrei same naam kintu Cat er khetre ek rup Dog er khetre ek rup & Goat er khetre arek rup)