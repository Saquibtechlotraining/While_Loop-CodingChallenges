# Create a simple calculator using loops (The program should be menu driven which runs till user exits itself.
# Means the program must ask the user every time to whether he want to continue or exit).
# Print Appropriate Message for this.(use while() loop)

'''
start = 1
end = float('inf')

while (start <= end):
    choice = input("Enter the choice continue or exit:").lower()
    if choice == "continue":
        print("........Calculation.......")
        x = """        Addition(+)
        Subtraction(-)
        Multiplication(*)
        Division(/)   """
        print(x)
        num_1 = int(input("Enter the first number:"))
        num_2 = int(input("Enter the second number:"))
        op = input("Enter the operator")
        if op == "+":
            print("Sum of two number:", num_1 + num_2)

        elif  op == "-":
            print("Subtraction of two number:", num_1 - num_2)


        elif op == "*":
            print("Multiplication of two number:", num_1 * num_2)

        else:
            if op == "/":
                print("Division of two number:", num_1 / num_2)
            else:
                print("Invalid Operator")
        start = start + 1

    elif choice == "exit":
        break
    else:
        print("Invalid choice")
        break
'''

while True:
    print("....Calculation....")
    x = """    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Exit"""
    print(x)
    num_1 = int(input("Enter the first number:"))
    num_2 = int(input("Enter the second number:"))
    ch = int(input("Enter the operator:"))

    if ch == 1:
        print("Addition of two numbers:", num_1 + num_2)
    elif ch == 2:
        print("Subtraction of two numbers:", num_1 - num_2)
    elif ch == 3:
        print("Multiplication of two numbers:", num_1 * num_2)
    elif ch == 4:
        if (num_1 > num_2):
            if num_2 == 0:
                print("Denominator can't be zero")
            else:
                print("Division of two numbers:", num_1 / num_2)
        elif (num_2 > num_1):
            if num_1 == 0:
                print("Denominator can't be zero")
            else:
                print("Division of two numbers:", num_2 / num_1)

        else:
            print(num_1 / num_2)
    elif ch == 5:
        break
    else:
        print("Invalid operator")



