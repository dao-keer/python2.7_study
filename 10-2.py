name = raw_input("please enter you name: ")
with open('./test.txt', 'w') as fileObj:
	fileObj.write(name + '\n')

name = raw_input("please enter you name: ")
while name != 'quit':
	print "hello, " + name.title()
	with open('test.txt', 'a') as fileObj:
		fileObj.write('my name is ' + name + '\n')
        name = raw_input("please enter you name: ")


