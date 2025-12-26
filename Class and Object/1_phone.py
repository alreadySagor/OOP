class Phone:
    price = 19000
    color = 'blue'
    brand = 'samsung'

    """
    eta na likhle Phone class er object ba instance ke call ba print korle
    habijabi kichu ekta ba object ta memory'r kon location e ache seta dekhabe.

    ar __repr__ use korle er vitore ja return korbo setai print hobe. Like "Price, Color and Brand" (Evabe print korle "print(my_phone)")
    """
    def __repr__(self):
        return 'Price, Color and Brand'
    
my_phone = Phone() # Phone class er ekti object ba instance
print(my_phone)
print(my_phone.brand)
print(my_phone.color)
print(my_phone.price)