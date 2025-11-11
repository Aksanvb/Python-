##LIST :
##    It is a collection of datas
##    * mutable
##    * ordered
##    * changeable
##    * allow duplicate values
##    * allow different data types
##    * indexed

##a=[10,"python",10,20,30]
##b=a[0]
##for i in range(b):
##    if i==5:
##        print("Your name")
##    else:
##        print(i)


##var=[10,20,30,40]
##print(var[1:2])

##var=[10,20,30,40]
##print(var[::-1])


#1. APPEND:

##a=[10,20,30,40]
##a.append(50)
##print(a)
##a=int(input("Enter the value:"))
##b=[]
##c=[]
##for i in range(1,a+1):
##    if i%3==0 or i%5==0:
##        b.append(i)
##    else:
##        c.append(i)
##print(b)
##print(c)

#2. EXTEND :

##a=[10,20,30]
##b=[40,50,60]
##a.extend(b)
##print(a)

#3. INSERT :

##a=[10,20,30]
##b=[40,50,60]
##a.insert(2,"hello")   #(index,value to be inserted[string or integer])
##print(a)

#4. POP :

a=[10,20,30,40,50,60]
a.pop()   #put index value insidepop's bracket to remove particular value
print(a)

#5. REMOVE :

##a=[10,20,30,40,50,60]
##a.remove(20) # directly enterthe value to remove
##print(a)

#6. SORT :

##a=[100,20,3,40,5,60]
##a.sort()    #prints the list in ascending order
##print(a)

##7. REVERSE :

##a=[100,20,3,40,5,60]  
##a.sort(reverse=True)    #prints the list in descending order
##print(a)

##a=[100,20,3,40,5,60]
##a.reverse()
##print(a)                #reverse the list


##8. CLEAR :

##a=[1,2,3,4,5,6]
##a.clear()
##print(a)

##9. COPY :

##a=[1,2,3,4,5,6]
##b=a.copy()
##b.clear()
##print(a,b)

##10. INDEX :

##x=[1,2,30,4,5,6,2,5,2]
##b=x.index(4)
##print(b)

##11. COUNT :

##x=[1,2,30,4,5,6,2,5,2]
##c=x.count(2)
##print(c)


####NESTED LIST :
a=[1,2,30,40,50,[10,20,30,["hiii","hello"]]]  #- totally index position 5 for inside list
print(a[5][3][1])
b=a[5][3][1]
for i in b:
    print(i)





