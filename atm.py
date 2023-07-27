def deposit_amt(amt):
    depo=float(input("Enter the amount you want to deposit:"))
    amt=amt+depo
    return amt

def withdraw_amt(amt):
    withd=float(input("Enter the amount you want to withdraw:"))
    if(amt>withd):
        amt-=withd
        print("Withdrawal successful. Your current account balance is" ,amt)
    else:
        print("\nInsufficient balance!")

while (True):
    amount=float(10000)
    print("1: Account Balance \n2: Money Deposit \n3: Money Withdrawal \n4: Exit")
    choice=int(input("Enter your choice:"))
    if(choice==1):
        print("Your current bank balance is:",amount)
    elif(choice==2):
        print("Deposit successful. Your current account balance is",deposit_amt(amount))
    elif(choice==3):
        withdraw_amt(amount)
    elif(choice==4):
        print("Exiting")
        break
    else:
        print('Invalid Input')
        break
