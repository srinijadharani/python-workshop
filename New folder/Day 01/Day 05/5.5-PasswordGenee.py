import random
# list of all letters, numbers, and symbols
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
# input the number of letters, symbols, and numbers you want in you pwd
nlet= int(input("How many letters would you like in your password? ")) 
nsym = int(input("How many symbols would you like? "))
nnum = int(input("How many numbers would you like? "))

password = ""

# choose a random letter, number, and symbol from the lists defined above
for let in range(0, nlet):
    random_letter = random.choice(letters)
    password += random_letter
    
for num in range(0, nnum):
    random_number = random.choice(numbers)
    password += random_number

for sym in range(0, nsym):
    random_symbol = random.choice(symbols)
    password += random_symbol

# shuffle the characters in password randomly
pwd = "".join(random.sample(password, len(password)))
print("Your password is:", pwd)