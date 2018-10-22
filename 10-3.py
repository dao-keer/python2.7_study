def numAdd():
	num1 = raw_input('please enter a numnber: ')
	flag = True
	sumRes = 0
	while flag:
		try:
			num1 = int(num1)
		except:
			if num1 == 'quit':
				flag = False
				break
			print 'please enter number, not text.'
		else:
			sumRes += num1
		num1 = raw_input('please enter a numnber: ')
	return sumRes

print numAdd()
