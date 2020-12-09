# import the random module
import random

num = random.randint(0, 1) # 0 and 1 inclusive

# if the number generated is 1, it is heads and if it is 0, it is a tail.
if num == 0:
    print("Tails")
else:
    print("Heads")