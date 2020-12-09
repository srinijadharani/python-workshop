import random
import my_module

print("Module Implementation:")
print("My name is:", my_module.name)
print(my_module.age)

print("Print a random whole number between 1 and 10 (inclusive):")
# randint generates a random number in a given range (inclusive of the lower and upper limit)
random_integer = random.randint(1, 10)
print("Random integer:", random_integer)

print("Print a random floating point number:")
# Remember this is always [0.0, 1.0). It means, 0.0 is included, but 1.0 is not. 
# The random values can go upto 0.9999 but never reach 0.1.
random_float = random.random()
print("Random floating point number:", random_float)

# random floating point value between 0 and 5
random_float5 = random.random() * 5
print("Random floating point number between 0 and 5:", random_float5)

# love calculator
love_score = round(random.random() * 100, 2)
print("The love score of you with your partner is:", love_score)
