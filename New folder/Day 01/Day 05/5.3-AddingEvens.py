# input the start and end index
start = int(input("Enter the start index: "))
end = int(input("Enter the end index: "))

sum1 = 0
# loop to find the sum of even numbers from start to end
for i in range(start, end+1, 2):
    sum1 += i
print("Sum of even numbers:", sum1)