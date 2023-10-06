# Write a program to calculate the sum of first n natural numbers. This n is given by the user using loop:-

start = 1
end = int(input("Enter the first n natural number:"))
sum = 0
while(start <= end):
    sum = sum + start
    start = start + 1
print("Sum of the first", end, "natural numbers:", sum)

