student_scores = input("Enter student scores: ")
# convert the given string of scores into a list using split()
student_scores = student_scores.split(", ")

# converts all the items in student_scores into integers
for score in range(0, len(student_scores)):
    student_scores[score] = int(student_scores[score])

highest = student_scores[0]

for i in range(0, len(student_scores)):
    if student_scores[i] > highest:
        highest = student_scores[i]

print("The highest score in the class is:", highest)

