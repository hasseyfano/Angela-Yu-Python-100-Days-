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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure")

# First choice: Left or Right?
choice1 = input('You\'re on a crossroad, where do you want to go? Type "Left" or "Right".\n').lower()

if choice1 == "left":
    # Continue the game
    choice2 = input('You\'ve come to a lake. There is an island inside the lake. Type "Wait" to wait for a boat. Type "Swim" to swim across.\n').lower()
    
    if choice2 == "wait":
        # Continue the game
        choice3 = input("You've arrived at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which one do you choose?\n").lower()
        
        if choice3 == "red":
            print("You get burned by fire. Game over!")
        elif choice3 == "yellow":
            print("Cool anjing. You win, puh sepuh!") 
        elif choice3 == "blue":
            print("Oops! You got eaten by a monster babi. Game Over!")
        else:
            print("You chose a door that doesn't exist. Game over!")
    else: 
        print("Something terrible happens. Game over!")  
else:
    print("Oh no! You've fallen into a hole. Game over!")