class User(object):
	def __init__(self, name, age, sex):
		self.name = name
		self.age = age
		self.sex = sex
	
	def describe(self):
		print 'name is ' + self.name.title()
		print 'age is ' + str(self.age)
		print 'sex is ' + self.sex
	
	def hello(self):
		print 'good morning, ' + self.name.title()
