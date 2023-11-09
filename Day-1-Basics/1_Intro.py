
def print5(n) :
    print(n)

def print4(n) :
    print(n)
    print5(5)

def print3(n) :
    print(n)
    print4(4)
def print2(n):
    print(n)
    print3(3)

def print1(n) :
    print(n)
    print2(2)

def printCall() :
    print1(1)

# print numberr from 1 to 5. you can only call one function.
printCall()
# that's y calling one main funciton and that will call other and from the main function.
# PS- Here printCall() working as main function

