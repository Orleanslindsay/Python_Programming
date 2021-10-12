students = {
	"Males":['Joseph','Stephen','Theophilus'],
	"Females":['kara','Sharon','Lois']
}
print(students["Males"])
#For Numbers

numbers = {"Integers": (0,1,2,3,4,5,),
"Decimals":[0.1, 0.2, 0.3, 0.4, 0.5]
}
print(numbers.get("Integers"))
#get is used to retreave a values in a key
number_2 = {1 : [1, 2, 3,0.5,3.8,4.73],
2 : (0, 1000,38.785, 2, 5, 6)	
}
print(number_2)

users = {"Joseph":{"fullname": "Joseph Lindsay",
"age": 75,
"height": 6},
"Theophilus":{"fullname": "Theophilus Owus",
"age":19,
"height":7}
}
print(users)


people = {"Jen":"c",
"Perry": "Python",
"Hill":"R"}
print(people.keys())#keys is used to get only the keys in the dictionary
print(people.values())#.values is used to get only values
print(people.items())#.item is used to get the keys and it corresponding pairs
people["Sharon"] = "javascript"
print(people)