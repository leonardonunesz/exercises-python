# calculate BMI (body mass index)
# < 18.5: Underweight   < 25: ideal weight     < 30: overweight     < 40: obesity       > 40: morbid obesity
weight = float(input("Digit your weight (Kg): "))
height = float(input("Digit your height (m): "))
bmi = weight / (height * height)
print("Your BMI is: {:.2f}".format(bmi))
if bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi < 25:
    print("Ideal Weight")
elif bmi >= 25 and bmi < 30:
    print("Overweight")
elif bmi >= 30 and bmi < 40:
    print("Obesity")
elif bmi >= 40:
    print('Morbid Obesity')