# Write a program to print the even and odd numbers in the range from 1 to n where n is given by the user
# and also print the sum of all even numbers and odd numbers separately.(use while loop)

sum_even = 0
sum_odd = 0
number = int(input("Enter the range:"))
start = 1
while (start <= number):
    if (start % 2) == 0:
        print("Even:",start)
        sum_even = sum_even + start
    else:
        print("Odd:", start)
        sum_odd = sum_odd + start
    start = start + 1

print("Sum of all even number in the range:",sum_even)
print("Sum of all odd number in the range:",sum_odd)