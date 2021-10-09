#The program is to determine the score of students and their relevant award
run = True
while run:
	student_score = float(input("Enter student's score: "))
	"""The student_score takes input  from the user.
	the input can take in float
	the range gives a specified start point and end point for 
	the user input to suit inorder to meet the condition of wining
	an award"""
for student_score in range(90,100):  
	print("Awarded a laptop!")
if student_score in range(60,90):
	print("Awarded a tablet!")
if student_score in range(0,60):
	print("Awarded Nothing")
	