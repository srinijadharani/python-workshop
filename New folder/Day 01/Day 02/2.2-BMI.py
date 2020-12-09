height = float(input("Enter your height in mts: "))
weight = float(input("Enter your weight in kgs: "))
bmi = round(weight/(height**2), 0)
print("Your BMI is:", int(bmi))