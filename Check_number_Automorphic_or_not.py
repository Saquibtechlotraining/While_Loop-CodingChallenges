# Write a program to check whether the number is automorphic number or not.(A number is said to be automorphic number
# if the original number is present on the right of the square of that number.)
# For example :
# 1.     5 is an automorphic number as its square is 25 and 5 is at its right side.
# 2.     Similary 25  - square 625 and 25 is at its right side.

number = int(input("Enter the number:"))
num = str(number)
product = number * number
result = str(product)
if result.endswith(num):
    print("Automorphic Number")
else:
    print("Not Automorphic Number")
