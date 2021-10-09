password = input("Enter your password: ")
if len(password) < 8:
	raise ValueError("password should be more than 8 characters")
else:
	print(password)