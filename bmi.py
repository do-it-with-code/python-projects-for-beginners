"""BMI Formula
Metric = weight (kg) / [ height (m) ]^2
Imperial = 703 * weight ( lbs ) / [ height (in ) ] ^ 2
"""

weight = input("What is your weight in pounds? ")
height = input("What is your height in inches? ")

bmi = 703 * float( weight ) / float( height ) ** 2
print("Your BMI is {}".format( bmi ) )

if bmi < 18.5:
    print("You are underweight")
elif 18.5 < bmi <= 24.9:
    print("Your weight is normal")
elif 25.0 <= bmi <=29.9:
    print("You're overweight")
else:
    print("You're obese")
