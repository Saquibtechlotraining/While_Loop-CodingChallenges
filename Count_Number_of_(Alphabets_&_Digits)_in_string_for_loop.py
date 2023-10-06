# Write a program to count the number of alphabets and no of digits in a string using loops.

string = "saquib ahmad123 gufi"
string_1 = string.replace(" ", "")
count_digit = 0
count_alphabet = 0

for i in range(0, len(string_1)):
    if (string_1[i].isdigit()):
        count_digit += 1
    elif (string_1[i].isalpha()):
        count_alphabet += 1
    else:
        print("Invalid character")
print("Number of digits in a string:", count_digit)
print("Number of alphabets in a string:", count_alphabet)