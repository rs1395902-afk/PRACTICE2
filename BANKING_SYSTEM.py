print("\n====WELCOME TO INDIAN BANK====")

balance = 25800

while True:         #MENU BAAR
    print("1 CHECK BALANCE")
    print("2 WITHDRAWL BALANCE")
    print("3 DEPOSIT BALANCE")
    print("4 EXIT")
    
    a = input("ENTER YOUR CHOICE : ")

    if a == "1":
        print(f"THE AVAILABLE BALANCE ON YOUR ACCOUNT IS : {balance} ")
    elif a == "2":
        amt = int(input("ENTER THE AMOUNT :"))
        balance = balance - amt
        print(f"YOUR AMOUNT {amt} HAS BEEN SUCCESFULLY WITHDRAWN")
        print(f"THE AVAILABLE BALANCE ON YOUR ACCOUNT IS : {balance} ")
    elif a == "3":
        amt = int(input("ENTER THE AMOUNT :"))
        balance = balance + amt
        print(f"YOUR AMOUNT {amt} HAS BEEN SUCCESFULLY DEPOSITED")
        print(f"THE AVAILABLE BALANCE ON YOUR ACCOUNT IS : {balance} ")
    elif a == "4":
        print("THANK YOU FOR VISITING")
        break
    else:
        print("INVAILD CHOICE")









    

    