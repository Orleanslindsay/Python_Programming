name = input("Enter your name: ")
height_m = float(input("Enter your height in meter: "))
weight_kg = float(input("Enter your weight in kilogram: "))

bmi = weight_kg / height_m ** 2

if bmi < 18.5:
	print("Your BMI is: ",bmi)
	print(name +  " is underweight.")

elif bmi >= 18.5 and bmi < 25:
	print("Your BMI is: ",bmi)
	print(name +  " is in normal weight.")

elif bmi >= 25 and bmi < 30:
	print("Your BMI is: ",bmi)
	print(name +  " is overweight.")

else:
	print("Your BMI is: ",bmi)
	print(name +  " is obese.")	
