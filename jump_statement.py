##Transfer statement or jump statement:
##    its alter the way a logic get executed
##         break    - terminate the loop
##         continue - skips the current iteration and proceed with next
##         pass     - its act like a place holder

##a=10,20,30,5,3,8,12,2
##for i in a:
##    if i==5:
##        ##break---prints till 30
##        print(i)
##        break
##    else:
##        print(i)

##a=10,20,8,30,5,3,8,12,2,5
##for i in a:
##    if i==5 or i==8:  #----skips 5 and 8
##        continue
##    else:
##        print(i)


a=10,20,8,30,5,3,8,12,2,5
for i in a:
    if i==5 or i==8:
        pass   #---holds place for any other value to be updated
    else:
        print(i)
