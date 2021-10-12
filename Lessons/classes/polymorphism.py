class Dog:
	def __init__ (self,name):
		self.name = name

	def speak(self):
		return self.name + " says Woof!"
		
class cat:
	def __init__ (self,name):
		self.name = name

	def speak(self):
		return self.name + " says Meow"

niko = Dog("Niko")
felix = cat("felix")

print(niko.speak())
print(felix.speak())

# using for loop to call the methods
# Demonstrating a polymorphism in for loop
object_instances = [niko,felix]
for object_instance in object_instances:
	print(object_instance.speak())

#Demonstrating polymorphism with a function
def pet_speak(pet):
	print(pet.speak())