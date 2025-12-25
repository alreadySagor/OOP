import math
import time
def timer(func):
    def inner(*args, **kwargs):
        print('time started')
        start = time.time()
        #print(func) # func ke print kore dilam # get_facto ke print korche ei khan theke
        func(*args, **kwargs)
        print('time ended')
        end = time.time()
        print(f'total time taken {end - start}')
    return inner

# timer() # timmer func ke call korteche. [return hisebe dibe arekti func(inner)]
# timer()() # timer er return krito function ke(inner) call korteche

@timer # timer func ke decorator hisebe use korlam, jar fole
# get_facto func ta tar (time) kache chole jay. kemne bujbo?
# dhori ei time func er moddhe ekta func diye dilam
def get_facto(n):
    print('Factorial is starting')
    result = math.factorial(n)
    print(f'factorial of {n} is: {result}')

get_facto(n = 1200) # *args & **kwargs duitai use korar karone key chara ba key soho value pathate parbo (parameter hote pare 1 ta ba 1 er beshi ba 0 tau hote pare) (*args key chara, like: 2, 3, 545 etc) (*kwargs key soho, like n = 2, value = 10 etc)


""" 
Normal vabeu @timer er kaj ta eivabe kora jay

# vejjailla way to decorate
timer(get_facto)()
 
"""