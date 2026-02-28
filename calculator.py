while True:
    print("Please select operation")
    print("1.addition");print("2.subtraction");print("3.multiplication");print("4.Division");print("5.percentage");print("6.exit/stop")
    choice = int(input("Please choose the operation to perform:"))
    if choice==6:
        print("Thank you")
        print()
        break
    elif choice<=5:
        n1=float(input("Enter a number:"))
        n2=float(input("Enter another number:"))
        if choice==1:
            print("Addition of",n1,'and',n2,'is:',n1+n2)
            print()
        elif choice==2:
            print("subtraction of",n1,'and',n2,'is:',n1-n2)
            print()
        elif choice==3:
            print("Multiplication of",n1,'and',n2,'is:',n1*n2)
            print()
        elif choice==4:
            if n2!=0:
                print("Division of",n1,'and',n2,'is:',n1/n2)
                print()
            else:
                print("'ERROR can't divide with zero'")
                print()
        elif choice==5:
            if n2!=0:
                print("Division of",n1,'and',n2,'is:',n1%n2)
                print()
            else:
                print("'ERROR can't divide with zero'")
                print()
    else:
        print("INVALID CHOICE")
        print()