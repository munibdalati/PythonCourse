# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
no_of_names = len(names)
random_no = random.randint(0, no_of_names - 1)
random_name = names[random_no]

print(f"{random_name} is going to buy the meal today!")