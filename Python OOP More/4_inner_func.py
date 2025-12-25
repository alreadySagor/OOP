"""
python e parameter hisebe ekta shongkha
ba ekta string ba chaile ekta function keu pathano jay
abar ami function er vitore aro ekta(ba onek) function likhte pari
eijonno python e function ke bola hoy --> function is a first class object
"""
def double_decker():
    print('starting the double decker')
    def inner_fun():
        print('inside the inner')
        return 3000
    return inner_fun

# print(double_decker())
# print(double_decker()()) # inner function ke soho call korlam


def do_something(work):
    print('work started')
    # print(work)
    work()
    print('Work ended')

# do_something(2)
# do_something('Ami busy')

def coding():
    print('coding in python')

# do_something(coding) # coding function ke do_something er parameter hisebe pathacchi

def sleeping():
    print('sleeping and dreaming')

do_something(sleeping)