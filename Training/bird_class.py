my_list = []
for list in range(450,500,2):
	lindsay = my_list.append(list)

print(my_list)
print(my_list[::2])
print(my_list[-2:1])

#list comprehension
cubes = [i**3 for i in range(5)]
lindsay = [i**3 for i in range(5) if i**3 % 2 == 0]
print(cubes)
print(lindsay)
sto = ["{b},{b},{c}".format(a =5, b=4, c = 8)]
print(sto)
nums = [33,44,54,43,67,67]
if all([i > 5 for i in nums]):
	print("All is greater than five")
if any([i % 2 == 0 for i in nums]):
	print("At least a number is even")
for i in enumerate(nums):
	print(nums)	
