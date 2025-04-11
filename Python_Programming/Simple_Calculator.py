def Calculator():
    print("==Welcome to Simple Calculator ==")
    try:
        num1 = float(input("Enter the first Number : "))
        operator = input("Choose any operation (+, -, *, /) or (1,2,3,4): ")
        num2 = float(input("Enter the second number : "))

        if operator == '+' or operator =="1":
            result = num1+ num2
            print("The Result is ", result)
        elif operator =='-' or operator =="2":
            result = num1 - num2
            print("The result is " , result)
        elif operator =='*' or operator =="3":
            result = num1 * num2
            print("The Result is ", result)
        elif operator =='/' or operator =="4":
            if operator != 0:
                result = num1/num2
                print("The result is ", result)
            else:
                print("Error : Division by Zero is not allowed")
        else:
            print("please choose correct operation")

    except ValueError:
        print("Invalid input : please enter the numberic value ")


Calculator()