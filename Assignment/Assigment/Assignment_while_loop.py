while True:
	""""PURPOSE OF THE CODE;The code is designed to determine if a 
	student won an award or not.
	CAUTION;If the input of the user is a string it will print Invaled Entry
	if and only the user input is equal to Exit
	INPUT;the user input should be in float and then prints out the corresponing
	award pertaining to the specified range given"""
	input_value = input("Enter student's score:")
	if input_value.capitalize() == "Exit":
		break
	elif input_value.capitalize() != "Exit" and input_value.isnumeric() == False:
		print("Invalid Entry!")
	else:
		student_score = float(input_value)
	if student_score >= 90 and student_score <=100:
		print("Awarded a laptop!")
	elif student_score >=60 and student_score <= 90:
		print("Awarded a tablet!")
	elif student_score < 60 and student_score > 0:
		print("Awarded Nothing")
	else:
		print("score out of range")
#To check if the program is a leap year




