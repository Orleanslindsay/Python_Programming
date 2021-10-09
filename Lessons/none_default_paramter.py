#The default parameters is none and dog
def describe_pet(name= None,animal="dog"):
	print(f"I have a {animal}")
	if name:
		print(f"It's called {name}")

print(describe_pet(animal = "cat"))
print(describe_pet())
print(describe_pet(name="Leo", animal= "Lion"))
print(describe_pet("Squid","Tiger"))
#We callout the function
