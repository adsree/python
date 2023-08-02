class student:
    def __init__(self, name,rollno):
        self.name=name
        self.rollno=rollno
    def display(self):
        pin=int(input("Enter the roll number of the student"))
        
    def age(self):
        age=(input("Enter the age of  student:"))
        return age


new=[]
while True:
    print ("Enter your choices\n1.Create student \n2.Show student details\n3.enter student age \n4.enter mark \n5.Exit")
    ch=int(input("Enter the choice:"))
    if ch==1:
        name=input("Enter the name of student")
        rollno=int(input("Enter the roll no of the student"))
        account=bank(name,acno,bal)
        new.append(account)
        print("Account created sucessfully, Your current balance is",account.bal)
       
    elif ch==2:
        pin=int(input("Enter your pin number"))
        for i in new:
            if i.pin == pin:
                print("Welcome" ,i.name,", Your current bank balance is:",i.bal)
    elif ch==3:
        pin=int(input("Enter your pin number"))
        for i in new:
            if i.pin == pin:
                i.bal = account.deposit()
                print("Deposit successful. Your current account balance is",i.bal)
            else:
                print("You have entered wrong pin number")
                exit()
    
    elif ch==4:
        pin=int(input("Enter your pin number"))
        for i in new:
            if i.pin == pin:
                i.bal = account.withdraw()
                print("Withdrawal successful. Your current account balance is" ,i.bal)
            else:
                print("You have entered wrong pin number")
                exit()
        
    elif ch==5:
        print("Exiting")
        break
    else:
        print("invalid number") 
        break