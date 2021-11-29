rows = int(input("Enter the number of rows: "))
i = 1
# outer file loop to print number of rows
while i <= rows:
	j = 1
# check the column after each iteration
while j <= i:
	# print odd values
	print((i * 2 - 1),end=" ")
	j = j + 1
i = i + 1
print()