##ATM

pin=1231
balance=100000
a=int(input("Enter your pin:"))
if pin==a:
    print("Pin is correct")
    print("1.Balance enquiry")
    print("2.Deposit money")
    print("3.Withdrawal")
    b=int(input("Enter your option:"))
    if b==1:
        print("Your balance amount is:",balance)
        
    elif b==2:
        print("Please deposit the amount")
        amt=int(input("Enter the amount:"))
        total=amt+balance
        print("Your total balance is:",total)
        
    elif b == 3:
        amt = int(input("Enter the amount to withdraw: "))
        if amt <= balance:
            total = balance - amt
            print("Collect your amount:", amt)
            print("Your total balance is:", total)
        else:
            print("Insufficient funds.")
            print("Your balance is:", balance)
            var = int(input("Enter valid amount: "))
            if var <= balance:
                bal = balance - var
                print("Collect your amount:", var)
                print("Your balance is:", bal)
            else:

                print("Invalid, try again")   
           
elif pin==int(input("Re enter your pin:")):
    print("Your pin is correct")
    print("1.Balance enquiry")
    print("2.Deposit money")
    print("3.Withdrawal")
    b=input("Enter your option:")
    if b==1:
        print("Your balance amount is:",balance)
    elif b=="balance":
        print("You have to enter only the option number, try again")
        print("1.Balance enquiry")
        print("2.Deposit money")
        print("3.Withdrawal")
        b=int(input("Enter your option:"))
        if b==1:
            print("Your balance amount is:",balance)
            
    elif b==2:
        print("Please deposit the amount")
        amt=int(input("Enter the amount:"))
        total=amt+balance
        print("Your total balance is:",total)
    elif b=="deposit":
        print("You have to enter only the option number, try again")
        print("1.Balance enquiry")
        print("2.Deposit money")
        print("3.Withdrawal")
        b=int(input("Enter your option:"))
        if b==2:
            print("Please deposit the amount")
            amt=int(input("Enter the amount:"))
            total=amt+balance
            print("Your total balance is:",total)

    elif b==3:
        amt=int(input("Enter the amount to withdraw:"))
    elif b=="withdraw":
         print("You have to enter only the option number, try again")
         print("1.Balance enquiry")
         print("2.Deposit money")
         print("3.Withdrawal")
         b=int(input("Enter your option:"))
         if b==3:
             amt=int(input("Enter the amount to withdraw:"))
             if amt<=balance:
                 total=balance-amt
                 print("Collect your amount",amt)
                 print("Your total balance is:",total)
             else:
                print("Insufficient funds")
            
else:
    print("Wrong pin, try again")
