# Take 10 values from user and find out the sum and multiplication and average of the numbers:-

start = 1
end = 10
sum = 0
mult = 1
count = 0

while (start <= end):
    number = int(input(f"Enter {start} number:"))
    sum = sum + number
    mult = mult * number
    count = count + 1
    start = start + 1

print("Sum of numbers:",sum)
print("Multiplication of numbers:",mult)
print("Average of the numbers:",sum/count)
