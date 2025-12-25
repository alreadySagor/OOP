# singleton --> one single instance
# if you want a new instance, you will get the old one(Already Created) instance

class Singleton:
    __instance = None
    def __init__(self):
        if Singleton.__instance is None:
            Singleton.__instance = self
        else:
            raise Exception('This is Singleton. Already have an instance, use that one by calling get_instance method')
        
    @staticmethod
    def get_instance(): # static method add korar fole self dite holo na.
        if Singleton.__instance is None:
            Singleton() # prothom bar call
        return Singleton.__instance # already thakle


first = Singleton.get_instance()
second = Singleton.get_instance()
third = Singleton.get_instance()
print(first)
print(second)
print(third)

# last = Singleton() # call korte parbona