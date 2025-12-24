class Book:
    def __init__(self, name):
        self.name = name
    def read(self):
        raise NotImplementedError # eitake call korle error dekhabe (jodi ei method ta child class e na thake. Ar thakle child class e ja bola ache/hobe tai dekhabe) / Base class e jei method ta thakbe sei method ta child class e must thaktei hobe.
class Physics(Book):
    def __init__(self, name, lab):
        self.lab = lab
        super().__init__(name)
    def read(self):
        print('Reading physics vector chapter')

topon = Physics('topon', True)
topon.read()

print(issubclass(Physics, Book)) # means: Physics ki Book er subclass? Yes hole output ashbe True
print(isinstance(topon, Physics)) # means: topon ki Physics er instance? Yes hole output ashbe True
print(isinstance(topon, Book))

# majhe majhe sub class check korar jonn Ba instance check korar jonno khub kaje lage

topon.read()

def read(self):
        raise NotImplementedError # eitake call korle error dekhabe
# error ta na khete chaile child class e taake implement korte hobe(Physics er moddhe korechi)

def read(self):
        # pass # eta dile--kono kichu na likheleu somossha nai
        raise NotImplementedError # eta dile--child class e ei method ta implement korte baddho korbe
