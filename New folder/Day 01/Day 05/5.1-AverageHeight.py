student_heights = input("Enter a list of student heights: ")
# convert the given string of heights into a list using split()
student_heights = student_heights.split()

# convert all the items in student_scores into integers
for i in range(0, len(student_heights)):
    student_heights[i] = int(student_heights[i])

# since sum1 and length are used in a loop and then iterated, initialize them to 0
sum1 = 0
length = 0
for i in student_heights:
    sum1 += i
    length += 1
# print the average height value
print("Average Height:", int(round(sum1/length, 0)))