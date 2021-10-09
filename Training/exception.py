try:
	raise MyE("Hello there Orleans")
except NameError:
	print("Hey, Orleans")

print("\n")
def test(x):
	try:
		if x == 0:
			raise NotsobadError("a moderately bad error","not too bad")
	except NotsobadError,e:
		print('Error args: %s')
test(0)