def makeCake(name, *fruit):
	print 'hello ' + name.title() + ', you have choose these fruits:'
	for v in fruit:
		print '-' + v.title()

makeCake('xiaoming', 'apple', 'orange', 'banana')
makeCake('dao-keer', 'pear', 'apple')
makeCake('zz', 'banana')
