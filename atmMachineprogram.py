userName = "venumadhav"
passWord = "venu123"
Cname = input("enter your name: ")
CpassWord = str(input("enter your password: "))
if Cname == userName and CpassWord == passWord:
    print('''
    1.deposite
    2.withdraw
    3.mini statement
    4.exit
    ''')
    amount = 50000
    option = int(input("select your option"))
    if option == 1:
        dep = int(input("enter your amount"))
        amount += dep
        print("total amount",amount)
    elif option == 2:
        withd = int(input("enter your amount"))
        amount -= withd
        print("total amount",amount)
    elif option == 3:
        print("=====ATM=====")
        print("userName:",userName)
        print("passWord:",passWord)
        print("=============")
else:
    print("please enter correct details")
