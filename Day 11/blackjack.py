import random
from art import logo

def deal_card():
    cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum (cards) > 21:
        cards.append(1)
        cards.remove(11)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You lose"
    if user_score == computer_score:
        return "It's a Draw"
    elif user_score == 0:
        return "You win!"
    elif computer_score == 0:
        return "You lose!"
    elif user_score > 21:
        return "You lose!"
    elif computer_score > 21:
        return "You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"
    

def play_game ():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False
    
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not is_game_over:
        global user_score
        global computer_score 
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score} ")
        print(f"Computer's first card {computer_cards[0]} ")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            should_pick = input("Type 'y' to get another card, type 'n' to pass:")
            if should_pick == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True
        while computer_score != 0 and computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))
    
  

global final_user_score
global final_computer_score
final_user_score = 0
final_computer_score = 0
      

while input("Do you want to play a game of Blackjack? Type 'y' or 'n':") == "y":
    play_game()
    if compare(user_score, computer_score) == "You win!":
        final_user_score += 1
        print(f"Your score is {final_user_score}, and {final_computer_score} for computer")
    else:
        final_computer_score += 1
        print(f"Your score is {final_user_score}, and {final_computer_score} for computer")

print(f"Final score :{final_user_score}:{final_computer_score}")
if final_user_score > final_computer_score:
    print("Big win!!")
elif final_user_score < final_computer_score:
    print("Big lose :-(")
elif final_user_score == final_computer_score:
    print("Draw")


    