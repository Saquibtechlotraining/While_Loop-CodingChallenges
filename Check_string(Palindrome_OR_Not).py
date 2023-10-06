#  Write a program to check whether the given string is palindrome or not.
# Example : MADAM, MOM

word = "MADAM"
reversed_word = word[::-1]
if word == reversed_word:
    print("Palindrome word")
else:
    print("Not a Palindrome word")