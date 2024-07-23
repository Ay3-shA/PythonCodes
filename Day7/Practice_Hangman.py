#Practice Hangman 
import random 

word_list = ["ardwark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)
guess = input("Guess the letter: ").lower()

for letter in chosen_word:
  if guess == letter:
    print("Right")
  else:
    print("Wrong")
