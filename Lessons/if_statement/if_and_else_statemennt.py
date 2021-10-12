""""The code determines, if the user input is an 
even number or an odd number"""
integer_number = int(input("Enter an integer number: "))

if integer_number % 2 == 0:
	print(integer_number, "is an even number.")
else:
	print(integer_number," is an odd number.")