##Iterative statement -- 

##FOR LOOP:
##  it is used to over the sequence again and again untill the condition ggets true

##SYNTAX
##for iterative in condition:
##    statement


##for iterative in range(5): ##iterative is variable
##    print("Chocolate")


##a=int(input("Enter a number:"))
##for iterative in range(10,-1,-1): #or (1,a),  (,,x)--step value,[prints in reverse]
##    print(iterative)


##a="Sanjay"
##for i in a[::-1]:  #if giving integer use range()
##    print(i)

##a="Sanjay"
##for i in range(len(a)-1,-1,-1):
##    print(a[i])

##a=int(input("enter number:"))
##for i in range(a):
##    if i%2==0:
##        print("Even",end=" ")
##        print(i)
##    else:
##        print("odd",end=" ")
##        print(i)


##a="Akash"
##b=""
##for i in a:
##    b=i+b   ##reversing using for
##print(b)


##a=6
##b=0
##for i in range(1,a+1):
##    b=b+i
##print("Maximum value:",b)

###divisible by 3&5--
##
##a=int(input("Enter the value:"))
##for i in range(a):
##    if i%3==0 and i%5==0:
##        print(i)



##for i in range(3):     #---- ##row
##    for j in range (3): #----##column
##        print(i,end=" ")
##    print()

##*
##* *
##* * *
##* * * *
##* * * * *

##for i in range(5):
##    for j in range(i+1):
##        print("*",end=" ")
##    print()

##* * * * *
##* * * *
##* * *
##* *
##*

##for i in range(5):
##    for j in range(5-i):
##        print("*",end=" ")
##    print()

        ##or

##for i in range(5,0,-1):
##    for j in range(i):
##        print("*",end=" ")
##    print()  

##P
##P y
##P y t
##P y t h
##P y t h o n

##a="python"
##for i in range(len(a)):
##    for j in range(i+1):
##        print(a[j],end=" ")
##    print()

##P y t h o n
##P y t h
##P y t
##P y
##P
    
##a="python"
##for i in range(len(a)):
##    for j in range(len(a)-i):
##        print(a[j],end=" ")
##    print()




   
