print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________
*******************************************************************************\n\n
''')


while True:
    name = input("What is your name:  ").capitalize()
    print('''  
"Welcome to Treasure Island!

You are at the crossroad. Where do you want to go?
Your mission is to find the treasure.
    ''')

    # First choice: Left or Right?
    direction = input('Which direction do you want to go? Type "Left" or "Right": ').lower()

    if direction == "left":
        # Continue the game
        request = input('You\'ve come to a lake. There is an island inside the lake. Type "Wait" to wait for a boat. Type "Swim" to swim across:  ').lower()
        
        if request == "wait":
            # Continue the game
            color = input("You've arrived at the island unharmed.  There is a house with 3 doors. One Red, one Yellow, and one Blue. Which one do you choose?:   ").lower()
            
            if color == "red":
                print(f"{name}, Game over!")
            elif color == "yellow":
                print(f"{name}, You win! Yeeey!") 
            elif color == "blue":
                print(f"{name}, Game over!")
            else:
                print(f"{name}, Game over!")
        else: 
            print(f"{name}, Game over!")  
    else:
        print(f"{name}, Game over!")

    # Ask if the player wants to play again
    play_again = input("Do you want to play again? Type 'yes' to continue or 'no' to quit:  ").lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye!")
        break
#the  above can also be written as the following:
"""
if input("Play again? Type 'yes' to continue: ").lower() != "yes":
        print("\nThanks for playing! Goodbye!")
        break
"""


# End of the game