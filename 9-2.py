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


myRestaurant = Restaurant('shaxian', 'ordinary', 0)
myRestaurant.describe()
myRestaurant.updateServedNum(10)
myRestaurant.describe()
myRestaurant.incrementServedNum(5)
myRestaurant.describe()
myRestaurant.resetServedNum()
myRestaurant.describe()