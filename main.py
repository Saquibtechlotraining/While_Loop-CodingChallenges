'''
sum = 0
for i in range(0, 10):
    number = int(input("Enter the number"))
    sum = sum + number
print(sum)
'''

'''
multiply = 1
for i in range(0, 10):
    number = int(input("Enter the number"))
    multiply = multiply * number
print(multiply)
'''

'''
start = 0
end = 10
multiply = 1
while (start <= end):
    number = int(input("Enter the number"))
    multiply = multiply * number
    start = start + 1
print(multiply)'''

'''
sum = 0
count = 0
for i in range(0, 11):
    number = int(input("Enter the number:"))
    sum = sum + number
    count = count + 1
print(sum/count)
'''

'''
start = "yes"
end = "no"
sum = 0
multiply = 1
while (start != end):
    number = int(input("Enter the number:"))
    sum = sum + number
    multiply = multiply * number
    end = input("Enter the Yes/ No:")
    if end == "yes" or end == "no":
        end = end
    else:
        print("Invalid word")
        break

print("Sum is:", sum)
print("Product is:", multiply)
'''


'''
start = 1
end = 10
sum = 0
mult = 1
count = 0

while (start <= end):
    print(start)
    number = int(input("Enter the number:"))
    sum = sum + number
    mult = mult * number
    count = count + 1
    start = start + 1

print("Sum of numbers:",sum)
print("Multiplication of numbers:",mult)
print("Average of the numbers:",sum/count)
'''










