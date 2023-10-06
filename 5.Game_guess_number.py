# 5.Create a game 'Guess the number' Game. Let us go through Rules one by one.
# 1.Computer will generate a Random Number.
# 2.Ask user to guess the number in 10 chances.
# 3.If user guesses it right , Score him accordingly like if user guesses in first chance score is 100 ,
# in second chance score should be 90 and so on.
# 4.If guess number is greater than random number give him 'Hint : Choose a Lower Number' or less than random number
# give him 'hint : Choose a Higher Number' or if guess number is equal to random , No need to hint , just display score
# and end the game.
# 5.Also show how many chances are left.
# 6.if user could not guess the number, disclose the random number and end the game


import random
comp_number = random.randint(1, 1000)

print("Choose Your Level Easy/Medium/Hard")
choice = input("Enter the choice:").title()
if choice == "Easy":
    print("You selected Easy Level, So you have 30 chances")
    end_chance = 30

elif choice == "Medium":
    print("You selected Medium Level, So you have 20 chances")
    end_chance = 20

elif choice == Hard:
    print("You selected Hard Level, So you have 10 chances")
    end_chance = 10

else:
    pass

start_chance = 1
scored = 100

while (start_chance <= end_chance):
    print(f"Chances left {end_chance - start_chance} : ")
    user_number = int(input(f"Enter the guess number {start_chance} : "))

    if comp_number == user_number:
        print("You win")
        scored = scored
        print("Scored:", scored)
        break

    elif comp_number > user_number:
        print("Choose upper number")
        scored = scored - 10
        print("Scored:", scored)

    else:
        print("Choose lower number")
        scored = scored - 10
        print("Scored:", scored)
    start_chance = start_chance + 1
else:
    print("Sorry You lost.You ran out of your chances:")

