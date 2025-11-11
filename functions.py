##FUNCTION :
##    function is a block of code when it is called, it will be executed or run
##    function keyword defined by "def", define a function
##    main purpose of function is reusability of code

##a=10
##print(a+10)
##print("name")
##def name():
##    print("sanjay")
##name()

##def secret():
##    print("Hello")
##secret()

##a=10   #---Global variable--can be used anywhere(used as local or global)
##b=20      
##def fun():
##    global a     #now a is global variable if "global" is used
##    a=10         #---Local variable--can be used only inside the function
##    b=20
##    print(a+b)
##fun()

##a=10
##b=20
##def fun():
##    a=20
##    b=30
##    print(a+b)
##fun()
##print(a)

##def fun():
##    var=[10,20,30,40,50]
##    for i in var:
##        if i==10:
##            b=1
##            while b<=i:
##                print(b)
##                b=b+1
##        else:
##            print(i)
##fun()


##def fun():
##    a=[10,20,30,"python"]
##    for i in range(a[0]):
##        if i==5:
##            print("sanjay")
##            break
##        else:
##            print(i)
##    b=1
##    c=[]
##    while b<a[0]:
##        c.append(b)
##        b=b+1
##    print(c)
##fun()

##def fun():
##    a={"tamil":int(input("enter your tamil mark:")),"eng":int(input("enter your eng mark:")),"maths":int(input("enter your maths mark:"))}
##    print(a["tamil"]+a["eng"]+a["maths"])
##fun()


                 ##TYPES##

##1. positional arguement :

##a=20
##b=30
##def fun(h,l):         #-parameter
##   print(h)
##   print(l)
##fun(a,b)           #- positional arguement


##a=20
##b=30
##def fun(a,b):         
##   print(a)
##   print(b)
##fun(5,60)           


##a=20
##b=30
##def fun(a,b):
##   a=10
##   b=20
##   print(a)
##   print(b)
##fun(5,60)           
##print(a)

    #or

#2.DEFAULT ARGUEMENT

##a=20
##b=30
##def fun(a=60,b=50):         
##   print(a)
##   print(b)
##fun()           

    #or

##a=20
##b=30
##def fun(a=20,b=60):         
##   print(a)
##   print(b)
##fun(30,40)           

    #or

##a=20
##b=30
##def fun(a=20,b=60):
##    a=100
##    b=200
##    print(a)
##    print(b)
##fun(30,40) 

##3 and 4 : variable length arguement :
##     1.(*arg) - non keywod arguement
##     2.(**keyword) - kewword arguement

##def Non_keyword(*a):  #a takes all the values if star given before it and saves as a tuple
##    print(a)
##Non_keyword(10,20,30,40,50,60)

##def Non_keyword(*a):
##    c=[]
##    for i in a:
##        if i ==10:
##            for j in range(i):
##                c.append(j)
##            print(c)
##Non_keyword(10,20,30,40,50,60)

##def Keyword(**a):    #stores value in a as a dictionary
##    print(a)
##
##Keyword(name="Ram",age=20)

##def Keyword(**a):    
##    for i in a:
##        print(i)#/print(a[i])
##
##Keyword(name="Ram",age=20)


##def fun(*salary):
##    print(type(salary))
##    for i in salary:
##        if i<10000:
##            print("Not eligible for credit card")
##        elif i>=20000 and i<240000:
##            print("Normal credit card")
##        else:
##            print("Premium credit card")
##fun(10000,20000,25000,8000)

##def fun():
##    return "hello"
##print(fun())

##def fun():
##    a=10
##    b=20
##    return a,b
##print(fun())

##def fun():
##    name = "ram"
##    age = 20
##    return name,age
##print(fun())

##def fun():
##    b=[]
##    for i in range(10):
##        if i%2==0:
##            b.append(i)
##    return b
##print(fun())

##input from user(name) more than 5 characters..print name...less than 5 characters..#provide more than 5 characters

##def fun():
##    name=input("Enter your name :")
##    a=[]
##    if len(name)>5:
##        a.append(name)
##    else:
##        a.append("Provide more than 5 characters")
##    return a
##print(fun())

           #or

##def fun():
##    name=input("Enter your name :")
##    if len(name)>5:
##        return name
##    else:
##        return("Provide more than 5 characters")
##print(fun())

           #or

##def fun(name):
##    if len(name)>5:
##        return name
##    else:
##        return"Provide more than 5 characters"
##print(fun(input("Enter name:")))

##def fun():
##    a="your name"                        ###############3
##    b=[]
##    for i in range(len(a)-1,-1,-1):
##        b.append(len(a)-1,-1,-1)
##    return a[i]
##print(fun())

##def main_fun():
##    a=["apple","orange","cherry","grapes"]
##    for i in range(len(a)):
##        print(i)
##    def inner_fun():
##        for i in a:
##            print(i)
##    b=10
##    c=20
##    print(b+c)
##    inner_fun()
##main_fun()

##def main_fun():
##    a=["apple","orange","cherry","grapes"]
##    for i in range(len(a)):
##        print(i)
##    def inner_fun():
##        global b
##        b=10
##        for i in a:
##            print(i)
##        def fun():
##            for i in range(len(a)):
##                print(a[i],end=" ")
##        fun()
##    inner_fun()
##main_fun()
##print(b)


##def main_fun():
##    a=["apple","orange","cherry","grapes"]
##    for i in range(len(a)):
##        print(i)
##    def inner_fun():
##        b=[]
##        for i in a:
##            b.append(len(i))
##        return b
##    return inner_fun()
##print(main_fun())





##LAMBDA, FILTER, MAP, ZIP, ENUMERATE, REDUCE



























