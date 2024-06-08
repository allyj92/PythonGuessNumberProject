#Number Guessing Game Objectives:

# Include an ASCII art logo.
import art
import random




    
turn_check = 0;
is_done = False
  
  
def check_number():
     global is_done
     if answer == number:
       print(f"You got it! The answer was {number}") 
       is_done = True
     elif answer > number :
       print("Too high.")
       print("Guess again.")
     elif answer < number :
       print("Too low")
       print("Guess again.")  
       
  
def check_stage() :
     global is_done
     if stage == "EASY" : 
       check_number()
       print(f"You have {10-turn_check} attempts remaining to guess the number.")
       if turn_check > 9 :
         print("You've run out of guesses, you lose.")
         is_done = True
  
     elif stage == "HARD"  :
       check_number()
       print(f"You have {5-turn_check} attempts remaining to guess the number.")
       if turn_check > 4 :
         print("You've run out of guesses, you lose.")
         is_done = True
  

is_gamer_over = False
while not is_gamer_over :
  art.logo()
  
  number = random.randint(1, 100)
  stage = input("Choose a difficulty. Type 'easy' or 'hard' : ").upper()
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100")
  
  
  while not is_done: 
    answer = int(input("Make a guess: "))
    turn_check += 1
    check_stage()
    
  is_game_over = input("Do you want to play again? Type 'y' or 'n' : ").upper()
  
  if is_game_over == "N" :
    is_gamer_over = True


 
    
      
  


  



  
