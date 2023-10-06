#2. Print a multiplication table of number given by the user:-

number = int(input("Enter the number of the table:"))
start = 1
end = 10
while start <= end:
    print(number, "X", start, "=", start * number)
    start = start + 1