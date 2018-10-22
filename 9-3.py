class Restaurant(object):
	def __init__(self, name, typed, serveNum):
		self.name = name
		self.typed = typed
		self.serveNum = serveNum
	
	def describe(self):
		print 'the restaurant name is ' + self.name.title()
		print 'the restaurant type is ' + self.typed
		print 'the restaurant servedNum is ' + str(self.serveNum)
	
	def openRestaurant(self):
		print 'the reataurant ' + self.name + ' is open'

	def updateServedNum(self, serveNum):
		self.serveNum = serveNum

	def incrementServedNum(self, incrementNum):
		self.serveNum += incrementNum

	def resetServedNum(self):
		self.serveNum = 0

class IceCreamStand(Restaurant):
	def __init__(self, name, typed, serveNum, favours):
		super(IceCreamStand, self).__init__(name, typed, serveNum)
		self.favours = favours
	
	def printFavors(self):
		for i in self.favours:
			print i

myIcecream = IceCreamStand('loveRoom', 'Chinese', 30, ['iceCreamA', 'iceCreamB', 'iceCreamC'])
myIcecream.printFavors()

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

class Adminuser(User):
	def __init__(self, name, age, sex):
		super(Adminuser, self).__init__(name, age, sex)
		self.ctrList = ["can add post", "can delete post", "can ban user"]
	
	def showPrivileges(self):
		for i in self.ctrList:
			print i

adminU = Adminuser('dao-keer', 20, 'male')
adminU.showPrivileges()