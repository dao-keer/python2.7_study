def makeCake(name, *fruit):
	print 'hello ' + name.title() + ', you have choose these fruits:'
	for v in fruit:
		print '-' + v.title()

makeCake('xiaoming', 'apple', 'orange', 'banana')
makeCake('dao-keer', 'pear', 'apple')
makeCake('zz', 'banana')

def userInfo(name, age, **info):
	_info = {}
	_info['name'] = name
	_info['age'] = age
	for key, value in info.items():
		_info[key] = value
	return _info

print userInfo('dao-keer', 20, sex ='male')

def makeCar(name, color, **info):
	car = {}
	car['name'] = name
	car['color'] = color
	for key, value in info.items():
		car[key] = value
	return car

print makeCar('bmw', 'red', size=4, isOne=True)
