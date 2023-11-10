

# here will be printing number from 1 to 5 using recursion
# must think 1st when to stop

print("\nPrinting number from 1 to 5 using recursion\n")

def printNumber( num ) :
    if (num == 5) :
        print(5)
        return
    else:
        print(num)
        printNumber(num + 1)

printNumber(1)



