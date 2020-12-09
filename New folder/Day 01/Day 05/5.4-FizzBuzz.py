# input the start and end index
start = int(input("Enter the start index: "))
end = int(input("Enter the end index: "))

# if the number is divisible by 3, print Fizz instead of that number
# if the number is divisible by 5, print Buzz instead of that number
# if the number is divisible both by 3 and 5, print FizzBuzz instead of that number
for i in range(start, end+1):
    if i%3 ==0 and i%5 == 0:
        i = "FizzBuzz"
        print(i)
    elif i%3 == 0:
        i = "Fizz"
        print(i)
    elif i%5 == 0:
        i = "Buzz"
        print(i)
    else:
        print(i)