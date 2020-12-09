print("Python Pizza Delivery!")
size = input("What is the size you'd like to order? S, M or L? ")
pepp = input("Do you want pepperoni on your pizza? Y or N? ")
cheese = input("Do you want extra cheese on your pizza? Y or N? ")

# INSTRUCTIONS:
# Small Pizza: $15
# Small Pizza: $15
# Medium Pizza: $20
# Medium Pizza: $20
# Large Pizza: $25
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1

def total_bill(size, pepp, cheese):
    bill = 0
    if size == "S":
        bill += 15
    elif size == "M":
        bill += 20
    elif size == "L":
        bill += 25
    else:
        print("Invalid Size.")
    if pepp == "Y":
        if size == "S":
            bill += 2
        elif size == "M" or size == "L":
            bill += 3
    if cheese == "Y":
        bill += 1
    elif cheese == "N":
        bill += 0

    print("Your final bill sums up to ${}." .format(bill))

total_bill(size, pepp, cheese)
