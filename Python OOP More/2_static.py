# static method @staticmethod (ek kaaj hocche instance se nibe na
# na niye normal ekta function outside e lekha jerokom ekhane (class er moddhe) lekha
# ekirokom. Ekatke class er upor sorasori use korte parbo) 

# difference between static method and class method
class Shopping:
    cart = [] # class attribute / static attribute
    origin = 'china'

    def __init__(self, name, location):
        self.name = name # instance attribute
        self.location = location # instance attibute

    def purchase(self, item, price, amount):
        remaining = amount - price
        print(f'Buying: {item} for price: {price} and remaning {remaining}')
    
    # static method
    @staticmethod
    def multiply(a, b): # static method use korar fole amake ekhane self dite hobe na
        result = a * b
        print(result)
        # static method korle instance er kono kichu use korte parbona


    @classmethod
    def hudai_dekhi(self, item):
        print('Hudai dekhi kintu')


# Shopping.purchase('a', 2, 3, 3)
basundhara = Shopping('basu en dhara','not populer location')
# basundhara.purchase('lungi', 500, 1000)
basundhara.hudai_dekhi('lungi')
Shopping.hudai_dekhi('Lungi') #  class er upor use kortechi @classmethod er help niye

# Shopping.hudai_dekhi('lungi) eita class er upor dekhte
# chacchi, kintu class er upor emnei dekha jay na(instance er upor jay).
# class er upor dekhte chaile oi method tar upore likhe dite hoy
# @classmethod



Shopping.multiply(3, 4) # static method er help niye class er upor (static method use korle evabe "Shopping.multiply(3, 4)" likhte parbo)

basundhara.multiply(6, 9) # instance er upor (instance use korle evabe "basundhara.multiply(6, 9)" likhte parbo)