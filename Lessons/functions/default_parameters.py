#This is for default parameters
def describe_pet(name,animal="dog"):
	print(f"I have a {animal}")
	print(f"It's called {name}")
#Ignore default/operational parameter
print(describe_pet(name = "Lynx"))
#Modify default parameter
print(describe_pet(name = "Hardy", animal="cat"))
# Use positional arguments
print(describe_pet("Angelos","dog"))