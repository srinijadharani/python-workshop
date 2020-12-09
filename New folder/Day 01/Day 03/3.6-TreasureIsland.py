print("Welcome to Treasure Island! Your mission is to find the treasure.")

# THERE ARE NO RULES. MAKE YOUR OWN!

direction = input("Choose left or right: L or R? ")
if direction == "R":
    print("Oh, no! You fall into a hole, game over.")
elif direction == "L":
    swim_wait = input("You come across a lake. Do you choose to swim across the lake or wait for a boat? Choose S to swim or W to wait: S or W? ")
    if swim_wait == "S":
        print("Oh, no! A trout has attacked you, game over.")
    elif swim_wait == "W":
        door = input("Now you're standing in front of three doors. Which door would you choose? Y (Yellow), R (Red), or B (Blue)? ")
        if door == "Y":
            print("You Win!")
        elif door == "B":
            print("You are being eaten by beasts! Game over.")
        elif door == "R":
            print("You are burnt by fire! Game over.")
        else:
            print("Invalid, game over.")