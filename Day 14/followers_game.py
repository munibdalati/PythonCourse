import random
import os
from art import logo
from art import vs
from game_data import data



def format(account):
    choice_name = account['name']
    choice_description = account['description']
    choice_country = account['country']
    return f"{choice_name}, {choice_description}, from {choice_country}"
    
current_score = 0
continue_game = False

b = random.choice(data)

while not continue_game:
    print (logo)
    a = b
    b = random.choice(data)
    while a ==b:
        b = random.choice(data)
    
    print (f"Compare B: {format(a)} ")
    print (vs)
    print (f"Against B: {format(b)} ")
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    os.system('clear')
    if answer == "a" and a['follower_count'] > b['follower_count'] or answer == "b" and a['follower_count'] < b['follower_count']:
        current_score += 1
        
        print (f"You're right! Current score: {current_score}.")
        
    elif answer == "a" and a['follower_count'] < b['follower_count'] or answer == "b" and a['follower_count'] > b['follower_count']:
        os.system('clear')
        print (logo)
        print (f"Sorry, that's wrong. Final score: {current_score}")
        continue_game = True
    
    