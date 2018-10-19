class Restaurant(object):
	def __init__(self, name, typed):
		self.name = name
		self.typed = typed
	
	def describe(self):
		print 'the restaurant name is ' + self.name.title()
		print 'the restaurant type is ' + self.typed
	
	def openRestaurant(self):
		print 'the reataurant ' + self.name + ' is open'


myRestaurant = Restaurant('shaxian', 'ordinary')
myRestaurant.describe()
myRestaurant.openRestaurant()

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

me = User('dao-keer', 20, 'male')
me.describe()
me.hello()
