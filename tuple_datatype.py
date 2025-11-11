##TUPLE :
##    immutable
##    unchangeable
##    ordered
##    indexed
##    allow duplicate values
##    allow different data types
##    much faster than list(less memory)

##a=(10,20,30,40,50,10,"hello python")
##b=a[0]
##for i in a:
##    print(i)
##for i in range(b):
##    print(i)

##b=list(a)
##b.append(60)
##c=tuple(b)
##print(c)

##b=[]
##for i in range(a[0]):     #or a[0]+1
##    if i%2==0:            #to print the even no under 10 in the tuple
##        b.append(i)
##print(tuple(b))

##a=("apple","orange","cherry")
##b=list(a)
##b.insert(1,"banana")
##a=tuple(b)
##print(a)

##a=(10,20,30,10,50,10)
##b=a.count(10)   #count of the particular value
##c=a.index(30)   #index of the particular value
##print(b,c)

