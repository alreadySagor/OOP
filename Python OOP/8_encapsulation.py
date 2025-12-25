# encapsulation --> hide details
# access modifier: public, protected, private
class Bank:
    def __init__(self, holder_name, initial_deposit):
        # Public attribute
        self.holder_name = holder_name
        # Protected
        self._branch = 'Banani 11' #  1 ta _ deya mane kono kichu protect kore na, kintu etake protected variable hisebe lokjon treat korar chesta kore (etar kono rule nai). Etake outside thekeu access korte parbo
        # Private
        self.__balance = initial_deposit # Balance taake private korlam. (double _ _ diye kono kichu / attribute ke private kora hoy)

    def deposit(self, amount):
        self.__balance += amount
    
    def get_balance(self):
        return self.__balance

    def withdraw(self, amount):
        if amount < self.__balance:
            self.__balance = self.__balance - amount
            return amount
        else:
            return f'fokira taka nai'
        
rafsan = Bank('Chuto bro', 10000)
print(rafsan.holder_name)
rafsan.holder_name = 'Boro Bhai'
rafsan.balance = 0 # balance private thakay balance ta baire thke update korte parchina
# print(rafsan.__balance)
rafsan.deposit(40000)
print(rafsan.get_balance())
print(rafsan.holder_name)
print(rafsan._branch)
# print(dir(rafsan)) # eita run korle kichu command pabo seita print korle private kono kichu baire thke access korte parbo
print(rafsan._Bank__balance) # _Bank__balance ta print(dir(rafsan)) theke peyechi

# balance ta ami outside theke access korte parchi
# kintu ami chaina baire theke kew balance taake access koruk
# tar jonno amra bank class er modde init er moddhe likhe dite pari
# self.__balance = initial_deposit (double _ _ diye kono kichu / attribute ke private kora hoy)