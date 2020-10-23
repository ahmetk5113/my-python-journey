
# classes define functions called methods, classes are like blueprints
# lets create one:
class Dog:
	species = 'Golden Retriever'
	def __init__(self, name, age , types): # __init__() states the initial state of the object
	# it assigns the values of objects properties
	# initialises each new instance of a class 
	# the first parameter always has to be self
	# so that new attributes can be defined on the object
	# class atributes must be defined under the class elemnt  before __init__()
		self.name = name
		self.age = age
		self.types = types
		print(name)

Dog('Whisky', 12, 'Golden retriever')


# Instance Methods:
class Cat:
	species1 = 'Cyprus cat'
	def __init__(self, name):
		self.name = name

	def say(self, sound):
		print(f'{self.name} says {sound}')

smth = Cat("Maisy")
smth.say('woof woof')
print(smth)


# Inheritance:
# lets use the class we first defined
# soo basically there are parent and child classes
# in here the parent class is Cat
# and the child class is the AnkaraCat
# we can use whats defined in the mother when using inheritance
# and we can add more stuff to our child class
class AnkaraCat(Cat):
	pass

smth2 = AnkaraCat('molly')
smth2.say("meow")