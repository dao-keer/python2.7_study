class Employee(object):
	def __init__(self, name, age, salary):
		self.name = name
		self.age = age
		self.salary = salary
	
	def give_raise(self, increment=5000):
		self.salary += increment

		
