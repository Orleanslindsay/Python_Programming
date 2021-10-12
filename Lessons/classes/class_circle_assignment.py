from math import pi
class Circle:
	name = "circle"
	def __init__ (self,radius,sector,arc):
		
		self.radius = radius 
		self.sector = sector 
		self.arc = arc
	# Adding a method to calculate the circumference of the circle
	def circumference_of_circle(self):
	
		r = self.radius
		c = 2 * pi * r 
		print("The circumference of the circle",c)
	
	# Adding a method, which is use to calculate the length an arc
	def length_of_arc(self):
		a = self.arc
		r = self.radius
		length = (a/360) * 2 * pi * r
		print("The length of the arc",length)

	# A method to calculate the area of a circle
	def area_of_a_circle(self):
		
		r = self.radius
		# a is representing the area of a circle
		a = pi * r ** 2
		print("The area of the circle",a)

	# A method to calculate the area of the sector
	
	def area_of_a_sector(self):
		r = self.radius
		ac = self.sector
		# area is representing the area of the sector 
		area = (ac/360) * pi * r ** 2
		print("The area of the sector",area)

my_circle = Circle(6,45,34)
print(my_circle.circumference_of_circle())
print(my_circle.length_of_arc())
print(my_circle.area_of_a_circle())
print(my_circle.area_of_a_sector())


