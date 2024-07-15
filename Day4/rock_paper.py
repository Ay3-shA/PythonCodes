#Day3 Project
#Rock Paper Scissors Game

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

your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if your_choice >= 3 or your_choice <0: 
  print("You typed an invalid number, you lose!!!")
else:
  print(f"You chose {game_images[your_choice]} ")
  computer = random.randint(0, 2)
  print(f"Computer chose {game_images[computer]}")

  
  if (your_choice == 0 and computer == 2) or your_choice > computer:
    print ("You Win!!!")
  elif (your_choice == 2 and computer == 0) or computer > your_choice:
    print ("You lose!!!")
  elif your_choice == computer:
    print("It's a Draw")


#-------------------------------------------------------------------------
