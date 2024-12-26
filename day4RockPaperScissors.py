import random

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors")
hand = ["Rock", "Paper", "Scissors"]
yourChoice = input("What do you choose?: ").title()

computerChoice = random.choice(hand)  # Use random.choice instead of random.choices
print(f"Computer chose: {computerChoice}")
print(f"You chose: {yourChoice}")

if yourChoice == computerChoice:
    print("Both players selected same hand. It's a tie!")
elif yourChoice == "Rock" and computerChoice == "Scissors":
    print("You win!")
elif yourChoice == "Scissors" and computerChoice == "Paper":
    print("You win!")
elif yourChoice == "Paper" and computerChoice == "Rock":
    print("You win!")
elif yourChoice in hand:  # Valid input but computer wins
    print("Computer wins!")
else:  # Handle invalid input
    print("Invalid input. Please choose Rock, Paper, or Scissors.")
