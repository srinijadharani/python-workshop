import random

names_string = input("Enter everybody's names separated by a comma: ")
# convert the names_string into a list separated by a comma
names = names_string.split(", ")
# how many names do we have
total_names = len(names)
# generate a random index number from the list of names
random_name = random.randint(0, total_names-1)
# the name corresponding to the random index number generated above
final_name = names[random_name]
print(final_name, "is going to pay the whole amount.")