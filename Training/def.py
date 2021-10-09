def even(number):
	if number % 2 == 0:
		print(str(number) + "is an even number")
	else:
		print(str(number) + "is not an even number")
even(int(input("type number: ")))