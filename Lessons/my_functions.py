#Adding a function 
while True:
	def adding_two_numbers(input_1,input_2):
		"""The function is implemented to get/return the sum of two numbers
PARAMETERS:
input_1: takes in the first number which is in float numbers for processing;
input_2: takes in the second number which is in float numbers for suming 
RETURN TYPE;
The return type should be in float.
EXAMPLE:
add(7,7)"""
		return input_1 + input_2
		
	input_1 = float(input("First number:"))
	input_2 = float(input("second number:"))
	if input_1 or input_2 == 0:
		print("ZeroNumber Error")
	else:
		print(adding_two_numbers(input_1,input_2))


#Subrating two numbers
	def subrating_two_numbers(input_3,input_4):
		""""The function is to return the substraction of two numbers.
PARAMETERS:
input_3: takes in the first input which is in float
input_4: takes in the second input which is in float
RETURN TYPE;
The return type should be in float
EXAMPLE;
>>>print(subrating_two_numbers(8,2))""" 
		return input_3 - input_4
	input_3 = float(input("First number:"))
	input_4 = float(input("second number:"))
	print(subrating_two_numbers(input_3,input_4))


#Multiply two numbers
	def mutiply_two_numbers(input_5, input_6):
		""""The function is to multiply two numbers.
PARAMETERS;
input_5 takes the first number to be sum in float
input_5 takes the first number to be sum in float
RETURN TYPE:
The return value should be in float
EXAMPPLE;
>>>print(multiply_two_numbers(6,4))"""

		return input_5 * input_6
	input_5 = float(input("First number:"))
	input_6 = float(input("second number:"))
	print(mutiply_two_numbers(input_5,input_6))


#Dividing of two numbers
	def dividing(input1,input2):
		"""The function is to divide two numbers.
PARAMETERS;
input1 takes the first number to be sum in float
input2 takes the first number to be sum in float
RETURN TYPE:
The return value should be in float
EXAMPLE;
>>>print(dividing_two_numbers(9,4))"""
		return input1/input2
	input1 = float(input("First number:"))
	input2 = float(input("second number:"))
	print(dividing(input1,input2))



