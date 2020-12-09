list1 = ["⭕", "⭕", "⭕"]
list2 = ["⭕", "⭕", "⭕"]
list3 = ["⭕", "⭕", "⭕"]
# create a treasure map
map = [list1, list2, list3]
# print the treasure map in an order
print(f"{list1}\n{list2}\n{list3}")

num = input("Enter location: ")
# split the entered 'string' into two separate integers
horizontal = int(num[0])
vertical = int(num[1])

# place an X in the location given
map[vertical-1][horizontal-1] = "❌"
# print the final treasure map
print(f"{list1}\n{list2}\n{list3}")

