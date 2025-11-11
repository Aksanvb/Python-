##a=[10,20,30,40,[30,40,10,50,60,70]]
##b=[]
##for i in a:
##    if type(i)==list:                ##to print the list inside using loop
##        for j in i:
##            print(j)

##TASK :`
    
a = [10, 20, 30, 40]
numbers = []
i = 0
while i<len(a):
    num = 0
    while num<=a[i]:
        if num%2== 0 and num not in numbers:
            numbers.append(num)
        num += 1
    i += 1
print(numbers)
    
