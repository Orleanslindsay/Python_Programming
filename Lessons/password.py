#For generating a password
import random
lower = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "./,?'')*({}[]"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

orleans = lower + upper + numbers + symbols
length = 16
password ="".join(random.sample(orleans,length))
print(password)

x = [3, 4, 5, 5]
a,b,c,d = x 
print(a * b /c ** d)

add = (3 + 5)
print(add * 2)

a = 'pythonHub'
b = "pythonHub"
print(a != b)

x = y = 10,20
res = x == y
print(res)

rows = int(input("Enter rows"))
for i in range(rows + 1, 0, -1):
	for j in range(0, i -1):
		print("*", end='')
		print(" ")

		x = 'pyhton'
		print(x.find('P'))

x = [2, 3, 5, 6]
print(x[-0])

x = 0
while x<20:
	x = x + 3
print(x)		