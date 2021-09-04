student_score = float(input("Enter student's score: "))

if student_score >=90 and student_score <=100:  
	print("Awarded a laptop!")
elif student_score >=60 and student_score <=89:
	print("Awarded a tablet!")
elif student_score <=59:
	print("No Award")
else:
	print("In valid figure!")