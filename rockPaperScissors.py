import random

userScore = 0
computerScore = 0

choices = ["rock", "paper", "scissors"]

while True:
    userInput = input("Type Rock, Paper, or Scissors or Q to quit: ").lower()
    if userInput == 'q':
        break

    if userInput not in choices:
        continue

    # 0 = rock | 1 = paper | 2 = scissors
    random_number = random.randint(0, 2)
    computerPick = choices[random_number]
    print("Computer chose", computerPick + ".")

    if userInput == "rock" and computerPick == "scissors":
        print("You Win!")
        userScore += 1


    elif userInput == "paper" and computerPick == "rock":
        print("You Win!")
        userScore += 1


    elif userInput == "scissors" and computerPick == "paper":
        print("You Win!")
        userScore += 1

    else:
        print("You Lose!")
        computerScore += 1


print("The user won", userScore, "times.")
print("The computer won", computerScore, "times.")
print("Goodbye, Thank You for Playing!")


