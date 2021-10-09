""""The code is programmed to determine if a specified year is a leap
year or not.
The code takes input from user in integer from since there is no year
which is a decimal(float)
METHODS EXPLANATION;
.capitalize(): capitalizes the input of the user if in strings form.
But in this code there's a condition entitled to the code. That is the 
input of the user is "exit" it capitalizes it then breaks."""
input("Press enter to run the program...")
while True:
	year = input("Enter a year: ")
	if year.capitalize() == "Exit":
		break
	elif year.capitalize() != "Exit" and year.isnumeric() == False:
		print("Invalid Entry!")
	else:
		year = int(year)	
	if ((year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)):
		print("The year", year, "is a leap year")
	else:
		print("The year",year, "is not a leap year")
		