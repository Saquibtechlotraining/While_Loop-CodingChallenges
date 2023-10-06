# Write a program to check whether the number given by the user is an Armstrong number or not.
# (An Armstrong number is the number whose digits cubes sum is equal to the original number.
# Such as 153 as 1^3 + 5^3+3^3 = 1 + 125 + 27 = 153)

num = int(input("Enter the number:"))         # 153
number = str(num)                            # '153'

list_string= list(number)                 # ['1', '5', '3']

for x in range(0, len(list_string)):
    list_string[x] = int(list_string[x])
values = list_string                      # [1, 5, 3]

sum = 0
for i in range(0, len(values)):           # [1, 5, 3]
    sum = sum + ((values[i]) ** 3)        # 1**3 + 5**3 + 3**3 = 153

result = str(sum)                         # '153'

if result == number:                      # if '153' == '153'
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
