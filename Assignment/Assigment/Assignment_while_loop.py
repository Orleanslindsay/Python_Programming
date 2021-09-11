while True:
	input_value = input("Enter student's score:")
	student_score = float(input_value)
	if student_score >= 90 and student_score <=100:
		print("Awarded a laptop!")
	elif student_score >=60 and student_score <= 90:
		print("Awarded a tablet!")
	elif student_score < 60 and student_score > 0:
		print("Awarded Nothing")
	while(input_value).capitalize() == "Exit":
		break
	else:
		print("score out of range")