class Animal:
	# Constructor of the class
	def __init__ (self,name):
		self.name = name

	#Abstract method, defined by cinvention only
	def speak(self):
		raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):

	def speak(self):
		return self.name + " says Woof!"

class Cat(Animal):

	def speak(self):
		return self.name + " says Meow"

fido = Dog("Fido")
isis = Cat("Isis")

print(fido.speak())
print(isis.speak())