#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
#this coding has a very small problem
import random
from art import logo

def checker(number_of_attempts):
    print(f"You have {number_of_attempts} attempts remaining to guess the number.")
    guess = 0        
    for i in range (number_of_attempts):
        guess = int(input("Make a guess: "))
        if guess < easy_random and i < number_of_attempts:
             print("Too low.")
             if i == number_of_attempts:
                return
             print("Guess again")
             print(f"You have {number_of_attempts-i-1} attempts remaining to guess the number.")
        elif guess > easy_random and i < number_of_attempts:
             print("Too high.")
             if i == number_of_attempts:
                return
             print("Guess again")
             print(f"You have {number_of_attempts-i-1} attempts remaining to guess the number.")
        elif guess == easy_random:
             print(f"You got it! The answer was {easy_random}")
             return
             continue_game = True
    print("You've run out of guesses, you lose.")
    return

def difficulty ():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        checker (10)
    elif difficulty == "hard":
        checker (5)
print(logo)
print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.")

easy_random = random.randint(1, 100)
print(f"Pssst, the correct answer is {easy_random}")

difficulty ()
