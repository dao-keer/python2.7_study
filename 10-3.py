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

def read_file(file_name):
	try:
		with open(file_name) as file_object:
			print file_object.read()
	except:
		print 'sorry, the file named ' + file_name + 'is not found!'
	
read_file('./test1.txt')
read_file('./test.txt')
