username='Aditya'
password='Junno143'

c_name=input("enter the username:")
c_password=str(input("enter your passwod:"))

if c_name==username and c_password==password:
    print('''
    1.deposite
    2.withdraw
    3.ministatement
    4.exit
    ''')

    amount=100000
    option=int(input("select your option:"))
    if option==1:
        dep=int(input("enter the amount:"))
        amount+=dep
        print("total amount:",amount)

    elif option==2:
        withdrawl= int(input("enter the amount:"))
        amount-=withdrawl
        print("total amount:",amount)



    elif option==3:
        print("========ATM=========")
        print("username:",username)
        print("total amount:",amount)
        print("thanks for Visiting")
        print("=====================")

    elif option==4:
        exit()

else:
    print("please enter correct logins")
