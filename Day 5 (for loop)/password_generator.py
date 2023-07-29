#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
for n in range (1, (nr_letters + nr_symbols + nr_numbers + 1)):
  password_letters = random.choice(letters)
  password_numbers = random.choice(numbers)
  password_symbols = random.choice(symbols)
  
  for n in range(1, nr_letters):
    password_letters += random.choice(letters)
    
  for n in range(1, nr_symbols):
    password_numbers += random.choice(numbers)

  for n in range(1, nr_symbols):
    password_symbols += random.choice(symbols)
  
  password = password_letters + password_numbers + password_symbols
print (f"An ordered pasword for you is {password}")
password_list = list(password)
#print (password_list)

random.shuffle(password_list)

final_password = ""
for n in password_list:
    final_password += n
#OR
# final_password = ''.join(map(str, password_list))
print (f"An unordered pasword for you is {final_password}")


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P