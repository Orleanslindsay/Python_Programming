"""The values G,m1,m2,f and d stands for Gravitational constant, 
   initial mass,final mass,force and distance respectively"""

G = 6.67 * 10 ** -11
m1 = float(input("The value of the initial mass: "))
m2 = float(input("The value of the final mass: "))
d = float(input("The distance between the bodies: "))
F = (G * m1 * m2)/(d ** 2)
print("The magnitude of the attractive force: " ,F)