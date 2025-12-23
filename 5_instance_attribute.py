class Shop:
    shopping_mall = 'Jamuna'
    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = [] # cat is an instance attribute
    
    def add_to_cart(self, item):
        self.cart.append(item)

mehjabeen = Shop('Mehjabeen')
mehjabeen.add_to_cart('shoes')
mehjabeen.add_to_cart('phone')
print(mehjabeen.cart)

nisho = Shop('Nisho')
nisho.add_to_cart('cap')
nisho.add_to_cart('watch')
print(nisho.cart)

apurvo = Shop('Apurvo')
apurvo.add_to_cart('chiruni')
print(apurvo.cart)