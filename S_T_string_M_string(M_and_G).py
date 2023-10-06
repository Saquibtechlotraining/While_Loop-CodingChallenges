# Take two strings S and T from user which is of length 5 and print appropriate message if length is less or greater than 5.
# You have to build a new String M which is based on the following condition -
# a) if character at ith index of both S and T are same then ith character of M is G
# b) If character at ith index of both S and T are not equal or same then ith character of M is B
#
# Determine the string M using above condition
#
# Sample Input            Sample Output
#
# ABCDE                          BBGBB
# EDCBA
#
# ROUND                         GBBBB
# RINGS
#
# START                           GGBBG

S = input("Enter the S string:").upper()
T = input("Enter the T string:").upper()
if len(S) == 5 and len(T) == 5:
    M_string = ""
    for i in range(0, len(S)):
        for j in range(0, len(T)):
            if i == j and S[i] == T[j]:
                M_string = M_string + "G"
            elif i == j and S[i] != T[j]:
                M_string = M_string + "B"

    print("M_String:", M_string)

elif len(S) > 5 and len(T) == 5:
    print("Length of S cannot be greater than 5")

elif len(S) == 5 and len(T) > 5:
    print("Length of T cannot be greater than 5")

elif len(S) > 5 and len(T) > 5:
    print("Length of S and T cannot be greater than 5")

elif len(S) < 5 and len(T) == 5:
    print("Length of S cannot be smaller than 5")

elif len(S) == 5 and len(T) < 5:
    print("Length of T cannot be smaller than 5")

else:
    print("Length of S and T cannot be smaller than 5")