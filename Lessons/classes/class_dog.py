class Animal: # Acting as the parent class method
	def __init__ (self):
		print("Animal Created")

	def whoAmI(self):
		print("Eating")
     
     def eat(self):
     	print("Eating")

class Dog(Animal): # child/descending class
#Class Attribute
	species = "mammal"
#Object Attribute is what follows beneath;
	def __init__(self, breed, name):#creating object attribute with __init__ constructor
		self.breed = breed
		self.name = name
		Animal.__init__(self)
		print("Dog Created")

	def whoAmI(self):
		print("Dog")

	def bark(self):
		print("woof!")

dog_instance = Dog(name = "lynx",breed = "Pitbull")
print(dog_instance.whoAmI())
print(dog_instance.bark()
