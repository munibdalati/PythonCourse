rock = "rock"

paper = "paper"

scissors = "scissors"

#Write your code below this line 👇
import random

game = [rock, paper, scissors]
your_choise = int(input("What is you choice? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
if your_choise > 2:
  print("You typed an invalid number, You lose")
else:
  print (f"your choice is {game[your_choise]}")

  computer_choice = random.randint(0, 2)
  print (f"computer choice is {game[computer_choice]}")

  if your_choise == 0 and computer_choice == 0:
    print("It's a draw")
  elif your_choise == 0 and computer_choice == 1:
    print("You lose")
  elif your_choise == 0 and computer_choice == 2:
    print("You win!")
  elif your_choise == 1 and computer_choice == 0:
    print("You win!")
  elif your_choise == 1 and computer_choice == 1:
    print("It's a draw")
  elif your_choise == 1 and computer_choice == 2:
    print("You lose")
  elif your_choise == 2 and computer_choice == 0:
    print("You lose")
  elif your_choise == 2 and computer_choice == 1:
    print("You win!")
  elif your_choise == 2 and computer_choice == 2:
    print("It's a draw")
  else:
    print("You type an invalid number, You lose")