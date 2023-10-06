#3. Write a program to find the factorial of a number using while loop:-

start = 1
number = int(input("Enter the number of which we want a factorial of:"))
f = 1
while(start <= number):
    f = f * start
    start = start + 1
print("Factorial of", number, "is", f)
