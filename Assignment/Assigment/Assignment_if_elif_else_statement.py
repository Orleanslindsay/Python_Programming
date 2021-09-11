run = True
while run:
	student_score = float(input("Enter student's score: "))
for student_score in range(90,100):  
	print("Awarded a laptop!")
if student_score in range(60,90):
	print("Awarded a tablet!")
if student_score in range(0,60):
	print("Awarded Nothing")
	