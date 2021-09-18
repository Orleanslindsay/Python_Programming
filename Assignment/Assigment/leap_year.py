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
		