def describe_pet(animal,name):
	print(f"I have a {animal}")
	print(f"It's called {name}")

#Use Keyword arguments	
print(describe_pet(animal = "dog", name = "lynx"))

#Use Positioal arguments
print(describe_pet("dog", "lynx"))