##a=[1,2,30,40,50,[10,20,30,["hiii10","hello"]]]
##take 10 out and loop and only even no print

a=[1,2,30,40,50,[10,20,30,["hiii10","hello"]]]
b=a[5][3][0]
print(b)
for i in a:
    if i%2==0:
        print(i)
