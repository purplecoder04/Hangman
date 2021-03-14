from replit import clear
import random
from hangman_art import stages, logo
from hangman_wordlist import word_list

word=random.choice(word_list)
lives= 6
print(f'Pssst, the solution is {word}.')
display=[]
word_len= len(word)
for i in range(word_len):
  display.append("_")
print(f"{logo}")
guessed = ""
end_of_game = False
while not end_of_game:
  user_guess = input("Guess a letter: \n").lower()
  clear()
  if user_guess in display:
    print(f"you already guessed: {user_guess}")

  
  for i in range(word_len):
    letter = word[i]
    if user_guess == letter:
      display[i]= letter

  if user_guess not in word:
    print(f"{user_guess} Not in word 😟")
    lives-= 1
    if lives == 0:
      end_of_game = True
      print("You Lose 😭")
    
  print(f"{' '.join(display)}")
  if "_" in display:
    end_of_game = False
    print(f"{stages[lives]}")
  else:
    end_of_game= True
    print("you won 🥳 🥳")
    
    

    
    