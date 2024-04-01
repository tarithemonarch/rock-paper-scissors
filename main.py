import random
numlist = ["rock", "paper","scissors"]
user_wins = 0
comp_wins = 0
while True:
    choose = input("rock,paper,scissors or quit:")
    if choose == "quit":
        break

    if choose not in numlist:
        continue

    rand = random.randint(0, 2)
    num = numlist[rand]
    print(f"The computer picked {num}")

    if choose == "rock" and num == "scissors":
       print("You won")
       user_wins+=1
       continue

    if choose == "paper" and num == "rock":
        print("You won")
        user_wins+=1
        continue

    if choose == "scissors" and num == "paper":
        print("You won")
        user_wins+=1
        continue
    if choose == num:
        print("Draw")
        continue

    else:
        print("You lost")
        comp_wins+=1
        continue

print(f"You won {user_wins} times")
print(f"You lost {comp_wins} times")
print("Goodbye")
