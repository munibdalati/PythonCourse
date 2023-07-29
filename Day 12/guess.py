import random
from art import logo

HARD_TURN = 5
EASY_TURN = 10

def check_answer(guess, answer, turn):
    if guess > answer:
        print("Too high")
        return turn - 1
    elif guess < answer:
        print("Too low")
        return turn - 1
    else:
        print(f"you win {guess} is the correct numbet")

def set_difficulty():
    level = input("what level did you want to play, hard or easy? ")
    if level == "easy":
        return EASY_TURN
    elif level == "hard":
        return HARD_TURN

def game():
    print(logo)
    print ("Welcome to the game")
    print ("Think of a number between 1 and 100")
    answer = random.randint(1, 100)
    turn = set_difficulty ()
    guess = 0

    while guess != answer:
        print (f"no of attempt remaining is {turn}")
        guess = int(input("Make a guess: "))
        turn = check_answer(guess, answer, turn)
        if turn == 0:
            print("you lose")
            return
        elif guess != answer:
            print("Guess again")

game()
        