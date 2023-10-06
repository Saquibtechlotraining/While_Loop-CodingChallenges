#6. Take a number from user and return sum of all digits of the number:-
# Enter the Number: 484
# Sum of the digits: 16

number = 484
string = str(number)
listing = list(string)

#print(listing)
for i in range(0, len(listing)):
    listing[i] = int(listing[i])
#print(listing)

sum = 0
for x in range(0, len(listing)):
    sum = sum + listing[x]
print("Sum of the digits:", sum)