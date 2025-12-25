# read only --> you can not set the value. value can not be changed

# getter --> get a value of a property through a method. most of the time, you will get the value of a
# private attribute

# setter --> set a value of a property through a method. most of the time, you will set the value
# of a private property

class User:
    def __init__(self, name, age, money):
        self.name = name
        self._age = age
        self.__money = money

    # age ekta method, kichu kichu somoy amar eita dorkar hoite pare je
    # age take ami ekta attribute er moto kore use korte chai
    # sekhetre ekhane use korte pari @property (eta use korle eta ar method akare na hoye attribute e convert kore felche)
    """ ------------------------------------ """
    """# getter without any setter is readonly attribute """
    @property # decorator (@ diye kono kichu ekta funtion er upor lekha thakle setake decorator bole)
    def age(self):
        return self._age
    
    # getter [read kora jacche kintu set kora jacche na tai getter]
    @property
    def salary(self):
        return self.__money
    """ ------------------------------------ """
    # getter thakle setter banate parbo
    # setter
    @salary.setter # ekahane: salary hocche getter take setter banalam
    def salary(self, value):
        if value < 0:
            return 'salary can not be negative'
        self.__money += value
    """ ------------------------------------ """
samsu = User('Kopa', 21, 12000)

# print(samsu.__money)
# print(samsu.age()) # eta ekhon aar kaj korbena (karon eta method akare)
print(samsu.age) # attribute akare

print(samsu.salary)
samsu.salary = 4500 # getter ke setter korar karone ekhon set korte parbo
print(samsu.salary)


""" 
    kichu kichu khetre onek programming language ei ekta kaj kore
    seta hocche erokom private property ke set korar jonno
    getter and setter use kore

    getter and setter python er khetre getter gulo by default read only hoy
    onno prog: language er getter and setter dilei hoy

"""



""" #-----------------------------------------
    # normal vabe salary use korte chaile method akare print korte hobe karon ekhon eti ekti method [print(samsu.salary())]
    def salary(self):
        return self.__money
    #-----------------------------------------

    # attribute akare salary use korte chaile print korte hobe [print(samsu.salary)] & def er age dite hobe @property (eta ekta getter type er jinish hoye jay)
    def salary(self):
        return self.__money
    #-----------------------------------------
"""