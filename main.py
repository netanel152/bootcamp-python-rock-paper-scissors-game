import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

# Get user's choice
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors:\n"))

# Validate input at the start
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    # Print user's choice
    print("You chose:\n")
    print(game_images[user_choice])

    # Get computer's choice
    computer_choice = random.randint(0, 2)
    print("Computer chose:\n")
    print(game_images[computer_choice])


    if user_choice == computer_choice:
        print("It's a draw. 🤝")
    # Check for all the ways the user can win
    elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
        print("You win! 🎉")
    # If it's not a draw and not a win, it must be a loss
    else:
        print("You lose. 😢")