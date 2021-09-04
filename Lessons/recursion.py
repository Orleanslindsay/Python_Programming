def timer(num):
	if num <= 0:
		print('AddictivePython')
	else:
		print(num)
		timer(num - 1)
print(timer(10))