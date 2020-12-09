import random
print("Welcome to the Rock, Paper, Scissors game created in Python!")
print("Type 0 for Rock, 1 for Paper, and 2 for Scissors. Good Luck!")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# let the user input 0, 1, or 2 for rock, paper, and scissors
user_choice = int(input("Enter your choice: 0, 1, or 2? "))

print("Your play is:")
if user_choice == 0:
    print("Rock", rock)
elif user_choice == 1:
    print("Paper", paper)
else:
    print("Scissors", scissors) # if user_choice is 2

# from 0, 1, 2 the computer chooses one integer randomly
random_choice = random.randint(0, 2)
print("Computer's play is:")
if random_choice == 0:
    print("Rock", rock)
elif random_choice == 1:
    print("Paper", paper)
else:
    print("Scissors", scissors) # if random_choice is 2

# logic for playing rock, paper, scissors
# rock 0 wins against scissors 2
# scissor 2 wins against paper 1
# paper 1 wins against rock 0

"""
0 & 2 --> 0
2 & 1 --> 1
1 & 0 --> 0
"""

if user_choice == 0 and random_choice == 2:
    print("You win!")
elif user_choice == 2 and random_choice == 1:
    print("Computer wins!")
elif user_choice == 1 and random_choice == 0:
    print("Computer wins!")
elif user_choice == random_choice:
    print("It's a draw!")
elif random_choice > user_choice:
      print("You lose")
elif user_choice > random_choice:
  print("You win!")













