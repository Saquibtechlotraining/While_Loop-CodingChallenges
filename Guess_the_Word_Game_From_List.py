# Guess the Word Game:-

import random
list = ["devops", "analyst", "designer", "developer", "datascience"]
print("List:", list)
for word in list:
    random.shuffle(list)
comp_choice = word

print("Choose any word from the above list:")
start = 1
end = 4

while (start <= end):
    user_chance = input(f"Enter user {start} chance:")
    if user_chance == comp_choice:
        print("You Win")
        break

    start = start + 1

else:
    print("You loose, You completed all chances ")
