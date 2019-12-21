#q1
print("q1")
print("Object-oriented programming (OOP) is a programming paradigm based on the concept of (objects), which can contain data, in the form of fields (often known as attributes or properties), and code, in the form of procedures (often known as methods). A feature of objects is an object's procedures that can access and often modify the data fields of the object with which they are associated (objects have a notion of 'this' or 'self').  ")
print("")
#q2
print("q2")
print("A feature of objects is an object's procedures that can access and often modify the data fields of the object with which they are associated (objects have a notion of 'this' or 'self'). In OOP, computer programs are designed by making them out of objects that interact with one another.[1][2] OOP languages are diverse, but the most popular ones are class-based, meaning that objects are instances of classes, which also determine their types.  ")
print("")

#q3
print("q3")
print("'function'")
print("A function is a block of code to carry out a specific task, will contain its own scope and is called by name. All functions may contain zero(no) arguments or more than one arguments. On exit, a function can or can not return one or more values.  ")
print("'method'")
print("A method in python is somewhat similar to a function, except it is associated with object/classes. Methods in python are very similar to functions except for two major differences.  ")
print("")
 #q4
print("q4")
print(" Classes – the definitions for the data format and available procedures for a given type or class of object; may also contain data and procedures (known as class methods) themselves, i.e. classes contain the data members and member functions  ")
print("Objects – instances of classes . Objects sometimes correspond to things found in the real world. For example, a graphics program may have objects such as circle, square, menu. ")
print("  ")


#q5
print("q5")
class car:
	pass
	
	
	def __init__(self, model,colour,name):
		self.model =model
		self.colour = colour
		self.name=name
		self.orign ="pakistan"
		
	def printdetail(self):
		return f"the model is {self.model} and colour is {self.colour} ,name is {self.name} "
		
				
car1 = car("1988","black","alto")
car2 = car("1989","white","cultus")
car3 =car("1998","gray","mehran")
car4 = car("2000","red","toyota crola")
car5=car("2017","silver","honda civic")

print(car1.name)
print("")
print(car2.model)
print("")
print(car3.colour)
print("")
print(car4.__dict__)
print("")
print(car5.printdetail())

		
		
