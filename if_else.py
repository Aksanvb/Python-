##Control statement -
##   control flow is the order in which the preograme get executed
##   1.Conditional statement:
##       *if
##       *if - else
##       *if - elif - else
##       *nested if
##   2.Iterative statement:
##       *for
##       *while
##   3.Transfer or Jump statement:
##       it alters the way a logic get executed
##       *break
##       *pass
##       *continue

##print("Register your name and mobile number")
##a =int(input("enter 1 if ready to register else 2:"))
##if a==1:
##    name=input("Enter your name:")
##    mno=int(input("Enter mobile number:"))
##    print("registered,","registered_name:",name,"registered mno:",mno)
##else:
##    print("not registered")


##print("Register your name and mobile number")
##print("1.Direct Register")
##print("2.Mobile Register")
##print("3.Email Register")
##a =int(input("Select the option:"))
##if a==1:
##    print("Direct Register")
##elif a==2:
##    print("Mobile Register")
##elif a==3:
##    print("Email Register")
##else:
##    print("Not registered")

##a=20
##if a>=10:
##    print("a is greater than 10")
##elif 10==10:
##    print("10 is equal to 10")
##else:
##    print("invalid")

######TASK_910 -- start an input show the above options...balance,deposit,withdraw...makes mistake by typing balance...
                  ##write statement to make it as no error...give options to type balance or deposit or withdrw
                  ##do not print insufficent funds..for 2 times..two chances for all..balance, withdraw, deposit
##ATM

##pin=1231
##balance=100000
##a=int(input("Enter your pin:"))
##if pin==a:
##    print("Pin is correct")
##    print("1.Balance enquiry")
##    print("2.Deposit money")
##    print("3.Withdrawal")
##    b=int(input("Enter your option:"))
##    if b==1:
##        print("Your balance amount is:",balance)
##    elif b==2:
##        print("Please deposit the amount")
##        amt=int(input("Enter the amount:"))
##        total=amt+balance
##        print("Your total balance is:",total)
##    elif b==3:
##        amt=int(input("Enter the amount to withdraw:"))
##        if amt<=balance:
##            total=balance-amt
##            print("Collect your amount",amt)
##            print("Your total balance is:",total)
##        else:
##            print("Insufficient funds")
##            print("Your balance is:",balance)
##            var=int(input("Enter valid amount:"))
##            if var<=balance:
##                  bal=balance-var
##                  print("Collect your amount",var)
##                  print("Your balance is:",bal)
##            else:
##                  print("Invalid, try again")
##elif pin==int(input("Re enter your pin:")):
##    print("Your pin is correct")
##    print("1.Balance enquiry")
##    print("2.Deposit money")
##    print("3.Withdrawal")
##    b=input("Enter your option:")
##    if b==1:
##        print("Your balance amount is:",balance)
##    elif b=="balance":
##        print("You have to enter only the option number, try again")
##        print("1.Balance enquiry")
##        print("2.Deposit money")
##        print("3.Withdrawal")
##        b=int(input("Enter your option:"))
##        if b==1:
##            print("Your balance amount is:",balance)
##            
##    elif b==2:
##        print("Please deposit the amount")
##        amt=int(input("Enter the amount:"))
##        total=amt+balance
##        print("Your total balance is:",total)
##    elif b=="deposit":
##        print("You have to enter only the option number, try again")
##        print("1.Balance enquiry")
##        print("2.Deposit money")
##        print("3.Withdrawal")
##        b=int(input("Enter your option:"))
##        if b==2:
##            print("Please deposit the amount")
##            amt=int(input("Enter the amount:"))
##            total=amt+balance
##            print("Your total balance is:",total)
##
##    elif b==3:
##        amt=int(input("Enter the amount to withdraw:"))
##    elif b=="withdraw":
##         print("You have to enter only the option number, try again")
##         print("1.Balance enquiry")
##         print("2.Deposit money")
##         print("3.Withdrawal")
##         b=int(input("Enter your option:"))
##         if b==3:
##             amt=int(input("Enter the amount to withdraw:"))
##             if amt<=balance:
##                 total=balance-amt
##                 print("Collect your amount",amt)
##                 print("Your total balance is:",total)
##             else:
##                print("Insufficient funds")
##                            
##else:
##    print("Wrong pin")
##
##
##a=int(input("Enter a number:"))
##if a%2 == 0:
##    print("Even number",a)
##else:
##    print("Odd number",a)





























    
