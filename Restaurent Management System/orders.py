class Order:
    def __init__(self):
        self.items = {} # {} --> dictionary

    def add_item(self, item):
        if item in self.items:
            self.items[item] += item.quantity # item ta jodi cart e already thake
        else:
            self.items[item] = item.quantity # item ta jodi cart e na thake

    def remove(self, item):
        if item in self.items:
            del self.items[item]
            # amar nijer idea, delete korar por item > 0 hole cart er theke 1 minus kore dibo
            # if self.items[item] > 0:
            #     self.items[item] -= 1
    
    # @property use korar fole total_price method ta aar method nai
    # eta ekta variable hoye geche, ekhon etake func hisebe noy, variable hisebe access korte parbo
    @property
    def total_price(self):
        return sum(item.price * quantity for item, quantity in self.items.items())

    def clear(self): # cart ta khali kore dilam (Ecommerce website er system eta)
        self.items = {}