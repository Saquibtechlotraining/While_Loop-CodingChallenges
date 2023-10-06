# Take a string, a substring and an index value from a user and add this substring in the string at the index specified.
# The program must not throw any error whether the index not in the range of the [0, length of string].
# Sample :
# String  = abcdef
# Substring = jkl
# Index = 3
# Modified String = abcjkldef

string = input("Enter the string:").lower()
substring = input("Enter the substring:").lower()
index = int(input("Enter the index:"))
if (string.isalpha()):
    if (substring.isalpha()):
        if len(string) > index:
            semi_result = string.replace(string[index:], substring)
            rest_string = string[index:]
            print("Modified String:", semi_result + rest_string)
        else:
            print("Index out of range")
    else:
        print("Invalid substring only characters")
else:
    print("Invalid string only characters")
