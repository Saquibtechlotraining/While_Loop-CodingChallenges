# 8.Take integer inputs from user until he/she presses q (Ask to press q to quit after every integer input ).
# Print average and product of all numbers.

# Enter the number : 5
# do you want to quit ? no
# Enter the number : 10
# do you want to quit ? no
# Enter the number : 25
# do you want to quit ? yes
# Sum is 40
# Product is 1250

start = "yes"
end = "no"
sum = 0
multiply = 1
while (start != end):
    number = int(input("Enter the number:"))
    sum = sum + number
    multiply = multiply * number
    user_yes_no = input("Enter the Yes/ No:").lower()

    if user_yes_no == "yes":
        break

    elif user_yes_no == "no":
        user_yes_no = user_yes_no

    else:
        print("Invalid word")
        break

print("Sum is:", sum)
print("Product is:", multiply)