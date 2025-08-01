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



"""
    the above can also be written as:
    import random

while True:
    computerChoice = random.choice(('Rock', 'Paper', 'Scissors'))


    UserChoice=input("What do you choose? Type Rock, Paper or Scissors: ").title()
    print(f"\n computer chose {computerChoice} and you chose {UserChoice}\n")
    
# The rules of the game stored in a dictionary
# Key: The choice, Value: The choice it defeats
    wins_against = {
        'Rock': 'Scissors',
        'Paper': 'Rock',
        'Scissors': 'Paper'
    }

    # cleaner logic
    if UserChoice == computerChoice:
        print("It's a tie!")
    elif wins_against[UserChoice] == computerChoice:
        # Check if your choice's "losing opponent" matches what the computer chose
        print("You win!")
    else:
        print("Computer wins!")
"""


# and also as:

"""
    import random

# Use a constant for choices to avoid typos and make it easy to change.
VALID_CHOICES = ['Rock', 'Paper', 'Scissors']

while True:
    # --- 1. Get and Validate User Input ---
    prompt = "What do you choose? Type Rock, Paper, Scissors, or Quit: "
    user_choice = input(prompt).title()

    # --- 2. Add an Exit Condition ---
    if user_choice == 'Quit':
        print("Thanks for playing!")
        break # This exits the 'while True' loop

    if user_choice not in VALID_CHOICES:
        print(f"\nInvalid input. Please choose one of: {', '.join(VALID_CHOICES)}\n")
        continue # This skips the rest of the loop and starts over

    # --- 3. Game Logic ---
    computer_choice = random.choice(VALID_CHOICES)
    print(f"\nComputer chose {computer_choice} and you chose {user_choice}.\n")

    # --- 4. Determine Winner with Clean Logic ---
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        print("You win!")
    else:
        print("Computer wins!")
    
    print("-" * 20) # A separator for the next round
    
    fyi the VALID_CHOICES Constant	Centralizes your data. If you want to add "Lizard", you only change it in one place.
"""