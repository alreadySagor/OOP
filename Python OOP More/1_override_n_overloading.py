# parent class e jei naam er method ache oita jodi child class e thake taholei parent ke child override kore felteche
class Person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    def eat(self):
        print('vat mangso polau korma')
    
    def exercise(self):
        raise NotImplementedError

class Cricketer(Person):
    def __init__(self, name, age, height, weight, team):
        self.team = team
        super().__init__(name, age, height, weight)
    # override (parent class eu eat naamer method ache kintu parent class er ta kaj na kore eita korteche tai bola jay parent ke child class override kore felche)
    def eat(self):
        print('Vegetables')

    def exercise(self):
        print('Gym e poisa diya gham jorai')

    # duita odject er age ke jog korlam (sakib + mushi)[overload korlam]
    #  + sign operator overload
    # egulake Danda (dandar method) ba onek somoy magic method bola hoy
    def __add__(self, other):
        return self.age + other.age
    # * sign operator overload
    def __mul__(self, other): # (sakib * mushi) [overload korlam]
        return self.weight * other.weight 
    # len overload
    def __len__(self):
        return self.height # sakib er height ber korlam sakib obj ke overload kore
    # > operator overload
    def __gt__(self, other): # gt means greater than
        return self.age > other.age # print(sakib > mushi) er jonno overload korlam 


sakib = Cricketer('sakib', 38, 68, 91, 'BD')
sakib.eat()
sakib.exercise()

mushi = Cricketer('Mushi', 36, 65, 78, 'BD')

# sakib.eat() ke call korle Cricketer er moddhe jei eat method  ache oita execute hobe
# kintu oita jodi na thakto tahole Person er eat method execure hoto(inheritance er jonno)
# jehetu Person er ta na hoye cricketer er ta hoiche tai etake bola jay "override"

""" Overload """
# plus sign overload
print(45 + 63)
print('sakib' + 'rakib')
print([12, 98] + [5, 6, 7, 1, 2])

print(sakib + mushi) # sakib + muhsi duita obj tai eder overload kore jog korte hobe, overload chara kora jabe na
print(sakib * mushi)

print(len(sakib)) # sakib obj er len ber korte chaile ekeu overload kora lagbe

print(sakib > mushi)