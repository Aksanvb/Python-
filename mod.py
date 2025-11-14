##def fun():
##    return "hello"
##def var():
##    for i in range(10):
##        print(i)
##
##a=input("Enter value")
##b=input("Enter value")

def fun():
    def innerfun():
        a=input("Enter your name:")
        b=int(input("Enter your age:"))
        print( "your name is {}\nyour age is {}".format(a,b))
    return innerfun()
