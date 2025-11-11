##task

a=10,25,3,99,7
b=0                  ###min valuee
for i in a:
    if i>b:
        b=i
print(b)
c=0
for i in a:
    if i>c and i<b:
        c=i
print(c)



##task-- fruit-"apple","orange","cherry" --in reverse using for

##a="apple","orange","cherry"
##b=""
##for i in range(len(a)):
##    b=a[i]
##    print(b[::-1],end=" ")               


##task

##a=10
##b=1
##for i in range(1,a):
##    b=b*i
##print(b)


##task

##a=10
##b=0
##c=0
##for i in range(1,a+1):
##    b=b+i
##    if b%2==0:
##        c=c+b
##print(b)
##print(c)


##task

##0 1 2
##0 1 2
##0 1 2
##0 1 2
##0 1 2

##for i in range(5):     #---- ##row
##    for j in range (3): #----##column
##        print(j,end=" ")
##    print()
































