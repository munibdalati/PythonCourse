# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


name1 = name1.lower()
name2 = name2.lower()

T = int(name1.count("t")) + int(name2.count("t"))
R = int(name1.count("r")) + int(name2.count("r"))
U = int(name1.count("u")) + int(name2.count("u"))
E1 = int(name1.count("e")) + int(name2.count("e"))
L = int(name1.count("l")) + int(name2.count("l"))
O = int(name1.count("o")) + int(name2.count("o"))
V = int(name1.count("v")) + int(name2.count("v"))
E2 = int(name1.count("e")) + int(name2.count("e"))

Total1 = T+R+U+E1
Total2 = L+O+V+E2
Love_Score = int(str(Total1)+str(Total2))

if Love_Score < 10 or Love_Score > 90:
    print(f"Your score is {Love_Score}, you go together like coke and mentos.")
elif Love_Score > 40 and Love_Score < 50:
    print(f"Your score is {Love_Score}, you are alright together.")
else:
    print(f"Your score is {Love_Score}")