# Write a program to reverse the String using while loop.

string = "saquib"
reversed_value = len(string) - 1
reversed_string = ""

while (reversed_value >= 0):
    reversed_string = reversed_string + string[reversed_value]
    reversed_value = reversed_value - 1

print("Reversed String using While loop:", reversed_string)


# Write a program to reverse the String using For loop.

string = "saquib"
reversed_string = ""

for i in range(len(string)-1, -1, -1):
    reversed_string = reversed_string + string[i]
print("Reversed String using For loop:",reversed_string)
