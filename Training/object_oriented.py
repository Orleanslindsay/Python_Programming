class student:
	def check_pass_fail(self):
		if self.marks >= 40:
			return True
		else:
			return False
	def __init__(self,name,marks):
		self.name = name
		self.marks = marks
student = self.("orleans",21)
print(student)
