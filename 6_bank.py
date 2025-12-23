class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 100000

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
    
    def withdraw(self, amount):
        if amount < self.min_withdraw:
            print(f'fokira, You can not below {self.min_withdraw}')
        elif amount > self.max_withdraw:
            print(f'bank fokir hoye jabe. You can not withdraw more than {self.max_withdraw}')
        else:
            self.balance -= amount
            print(f'Here is your money {amount}')
            # print(f'Your balance after withdraw {self.balance}') # nicher line ar ei line eki
            print(f'Your balance after withdraw {self.get_balance()}') # nicher line ar ei line eki

brac = Bank(15000)
# brac.withdraw(250)

brac.deposit(1000)
brac.withdraw(250)

buro = Bank(5000)
buro.deposit(2000)
buro.deposit(1000)
print(buro.get_balance())