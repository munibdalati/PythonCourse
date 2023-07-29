import random
#random integer between 1 and 10
random_integer = random.randint(1, 10)
print(random_integer)

#random float between 0 and 0.99
random_float01 = random.random()
print(random_float01)

#random float between 0 and 4.99 (type1)
random_float05 = random.random() * 5
print(random_float05)

#random float between 0 and 4.99 (type2)
random_float = random.uniform(0,5)
print(random_float)