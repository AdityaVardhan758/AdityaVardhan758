import math

while True :
    print("\n choose the math operation \n \n0- Addition \n1- substraction \n2- multiplication \n3- division \n4- modulo \n5- raising to a power \n6- square root \n7- logirithm \n8- sine \n9- cosine \n10- tangent \n")
    oper= input("\n your option from the menu: ")

    if oper== "0":
        val1= float(input("\n first value: "))
        val2= float(input("\n second value: "))
        print("\n the result is: "+str(val1+val2)+"\n")
        back= input('\n go back to the main menu?(y/n)')

        if back=="y":
            continue
        else:
            break

    elif oper == "1":
        val1 = float(input("\n first value: "))
        val2 = float(input("\n second value: "))
        print("\n the result is: " + str(val1 - val2) + "\n")
        back = input('\n go back to the main menu?(y/n)')

        if back == "y":
            continue
        else:
            break

    elif oper == "2":
        val1 = float(input("\n first value: "))
        val2 = float(input("\n second value: "))
        print("\n the result is: " + str(val1 * val2) + "\n")
        back = input('\n go back to the main menu?(y/n)')

        if back == "y":
            continue
        else:
            break
    elif oper == "3":
        val1 = float(input("\n first value: "))
        val2 = float(input("\n second value: "))
        print("\n the result is: " + str(val1 / val2) + "\n")
        back = input('\n go back to the main menu?(y/n)')

        if back == "y":
            continue
        else:
            break

    elif oper == "4":
        val1 = float(input("\n first value: "))
        val2 = float(input("\n second value: "))
        print("\n the result is: " + str(val1 % val2) + "\n")
        back = input('\n go back to the main menu?(y/n)')

        if back == "y":
            continue
        else:
            break

    elif oper == "5":
        val1 = float(input("\n base value: "))
        val2 = float(input("\n power value: "))
        print("\n the result is: " + str(math.pow(val1, val2)) + "\n")
        back = input('\n go back to the main menu?(y/n)')

        if back == "y":
            continue
        else:
            break
    elif oper=="6":
        val1= float(input("\n enter the value to extract square root:"))
        print("\n the result is: "+str(math.sqrt(val1))+"\n")
        back= input('\n go back to the main menu?(y/n)')

        if back=="y":
            continue
        else:
            break
    elif oper == "7":
        val1 = float(input("\n enter the value for calculating the logorithm to base:"))
        print("\n the result is: " + str(math.log(val1,2)) + "\n")
        back = input('\n go back to the main menu?(y/n)')

        if back == "y":
            continue
        else:
            break

    elif oper=="8":
        val1=float(input("\n enter the value(in degree) for calculating the sine:"))
        print("\n the result is:"+str(math.sin(math.radians(val1)))+"\n")
        back = input('\n go back to the main menu?(y/n)')

        if back == "y":
            continue
        else:
            break
    elif oper=="9":
        val1=float(input("\n enter the value(in degree) for calculating the cosine:"))
        print("\n the result is:"+str(math.cos(math.radians(val1)))+"\n")
        back = input('\n go back to the main menu?(y/n)')

        if back == "y":
            continue
        else:
            break
    elif oper=="10":
        val1=float(input("\n enter the value(in degree) for calculating the tangent:"))
        print("\n the result is:"+str(math.tan(math.radians(val1)))+"\n")
        back = input('\n go back to the main menu?(y/n)')

        if back == "y":
            continue
        else:
            break

    else:
        print("\n invalid option!\n")
        continue















