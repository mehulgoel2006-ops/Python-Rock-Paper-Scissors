
import random
print("Welcome to Rock Paper Scissors!")
choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

while True:

    user = input("\nChoose rock, paper or scissors: ").lower()

    if user not in choices:
        print("Invalid choice! Try again.")
        continue

    computer = random.choice(choices)

    print("You:", user)
    print("Computer:", computer)

    if user == computer:
        print("It's a tie!")

    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):

        print("You win!")
        user_score += 1

    else:
        print("Computer wins!")
        computer_score += 1

    print("Your Score:", user_score)
    print("Computer Score:", computer_score)

    again = input("\nPlay again? (yes/no): ").lower()

    if again != "yes":
        print("\nFinal Score:")
        print("You:", user_score)
        print("Computer:", computer_score)
        print("Thanks for playing!")
        break
