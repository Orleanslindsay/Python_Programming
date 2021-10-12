#  Create function to add two numbers 

def adding_two_numbers(number_1,number_2):
	"""	
	This function returns the sum of two numbers.

PARAMETERS;
number_1: float, takes in the first numbber to sum;
number_2: float, takes in the second number to sum; 

RETURN TYPE;
The return type should be in float.
EXAMPLE:
add(7,7)
"""
	total_sum = number_1 + number_2
	return total_sum

#Create function to substract two numbers
def subrating_two_numbers(number_1,number_2):
	""""The function is to return the substraction of two numbers.
PARAMETERS:
number_1: float, takes the first number
number_2: float, takes the second number

RETURN TYPE;\
The return type should be in float

EXAMPLE;
>>>subtacting_two_numbers(6,4)

subtrating_two_numbers(number_1=9, number_2=6)
""" 
	return number_1 - number_2
	

#Create function to multiply two numbers
def mutiply_two_numbers(number_1, number_2):
	""""
	This function is to multiply two numbers.
PARAMETERS;
number_1: float, takes the first  number
number_2: float, taakes  the second number

RETURN TYPE:

The return value should be in float

EXAMPPLE;
>>>multiply_two_numbers(8,9)

multiply_two_numbers(number_1=5, number_2 = 8)
"""

	
	return number_1 * number_2
	

# Create function to divide two numbers
def divide_two_numbers(number_1,number_2):
	"""The function is to divide two numbers.
PARAMETERS;
number_1: takes the first number, float
number_2: takes the first number, float

RETURN TYPE:
The return value should be in float

EXAMPLE;
>>>print(dividing_two_numbers(9,4))
"""
	if number_2 == 0:
		print("number error")

	return number_1 / number_2




