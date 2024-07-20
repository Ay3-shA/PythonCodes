#Hangman
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

lives = 6

display = []
word_length = len(chosen_word)
for _ in range(word_length):
  display += "_"
print (display)


end_of_game = False
while not end_of_game:
  guess = input("Guess a letter.\n").lower()

  if guess not in chosen_word:
    lives -= 1
    if lives == 0:
      end_of_game = True
      print("\nYOU LOSE!!!\n")
  
  for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter
  
  print(display)
  
  if "_" not in display:
    end_of_game = True
    print("\nYOU WIN!!!\n")
  

  print (stages[lives])

#----------------------------------------------------------
    
    

