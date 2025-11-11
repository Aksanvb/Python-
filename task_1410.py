##task----print all in reverse
##a="apple","orange","cherry"
##b=""
##for i in range(len(a)):
##    b=a[i]
##    print(b[::-1],end=" ")

##task --
##p y t h o n 
##y t h o n 
##t h o n 
##h o n
##o n
##n 

a="python"
for i in range(len(a)):
    print(" ".join(a[i:]))
