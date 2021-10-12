class Cuboid:#the Cuboid is the  name of  the class
	name = "Cuboid" #class attribute
	def __init__(self,lenght,breath,height,weight):#here we have given parameters which is l,b,h,w
		self.length = lenght
		self.breath = breath
		self.height = height
		self.weight = weight

	# Adding up a method, which is volume to calculate the volume 
	def volume(self):
		x = self.length
		y = self.breath
		z = self.height
		v = x * y * z
		print("The volume is :", v)

	#A method density is raised to calculate the density
	def density(self):
		x = self.length
		y = self.breath
		z = self.height
		v = x * y * z
		d = self.weight/v
		print("The density is : ", d)

	# A method surface_area is raised to calculate the surfaace area
	def surface_area(self):
		x = self.length
		y = self.breath
		z = self.height
		s = 2 * (x * y + y * z + x * z)	
		print("The surface area is : ",s)


my_cuboid = Cuboid(1,2,4,4.5)#for here we given an  instance  called my_cuboid to call out  the class
print(my_cuboid.length)
print(my_cuboid.breath)
print(my_cuboid.height)
print(my_cuboid.weight)

my_cuboid_2 = Cuboid(2,4,6,5)# This is object attribute
print(my_cuboid.name)
print(my_cuboid_2.name)
print(my_cuboid_2.length)
print(my_cuboid_2.breath)
print(my_cuboid_2.height)
print(my_cuboid_2.weight)

print(my_cuboid.density())
print(my_cuboid.surface_area())
print(my_cuboid.volume())