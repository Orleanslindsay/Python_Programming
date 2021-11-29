def patern(n):
	num = 1
	for i in range(0,n):
		for j in range(0, i + 1):
			print(num,end=" ")
			num=num +1
		print("\r")
n =5
patern(n)


li = [1,2,3]
print(li.pop(1))