import my_functions
#Take first input value
number_1 = float(input("Enter first number for the computation program: "))

#Take second input value
number_2 = float(input("Enter second number for the computation program: "))

user_option = int(input(
	''''Choose 1 for Addition
	\n choose 2 for substraction
	\n choose 3 for  Multiplication
	\n choose 4 for division
	  please choose an option'''))
		

if user_option == 1:
	total_sum = my_functions.adding_two_numbers(number_1, number_2)

	print(f"The sum of {number_1} and {number_2} is {total_sum}")

elif user_option == 2:
	difference = my_functions.subrating_two_numbers(number_1, number_2)

	print(f"The difference of {number_1} and {number_2} is {difference}")

elif user_option == 3:
	product = my_functions.mutiply_two_numbers(number_1,number_2)
	print(f"The profuct of {number_1} and {number_2} is {product}")

elif user_option == 4: 
	division_results = my_functions.divide_two_numbers(number_1, number_2)
	print(f"The division_results of {number_1} and {number_2} is {division_results}")

else:
	print("You choose a wrong option!")	