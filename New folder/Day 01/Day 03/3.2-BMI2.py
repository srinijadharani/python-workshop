weight = float(input("Enter your weight in kgs: "))
height = float(input("Enter your height in mts: "))
# BMI = (weight)/(height^2). Round the final value such that it has 1 decimal.
bmi = round(weight/(height**2), 1)

def calc_bmi(bmi):
    # BMI > 18.5 --> underweight
    # BMI between 18.5 and 25 --> normal
    # BMI between 25 and 30 --> overweight
    # BMI between 30 and 35 --> obese
    # BMI greater than 35 --> clinically obese
    if bmi < 18.5:
        print("Your BMI is {}, you are underweight." .format(bmi))
    elif bmi > 18.5 and bmi < 25:
        print("Your BMI is {}, you have normal weight." .format(bmi))
    elif bmi > 25 and bmi < 30:
        print("Your BMI is {}, you are slightly overweight." .format(bmi))
    elif bmi > 30 and bmi < 35:
        print("Your BMI is {}, you are obese." .format(bmi))
    elif bmi > 35:
        print("Your BMI is {}, you are clinically obese." .format(bmi))

calc_bmi(bmi)