##take input as tamil eng and maths and also their values
##add the values and print

var=int(input("Enter tamil mark:"))
a={"tamil":var,"english":int(input("enter english mark:")),"maths":int(input("Enter maths mark:"))}
b=0
for i in a:
    if i=="tamil":
        if a[i]>=80:
            print("Good")
    print(a[i])
    b=b+a[i]
print("Total:",b)
