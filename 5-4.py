person = ['john', 'bob', 'smith', 'lily', 'tom', 'admin']
for p in person:
	if p == 'admin':
		print 'hello ' + p.title() + ', do you want to do some report?'
	else:
		print 'hello ' + p.title() + ', thank you for logging in again'

family = ['a', 'b', 'c', 'lily', 'd', 'bob', 'e', 'f']
for v in person:
	if v in family:
		print v.title() + " is already in our family"
	else:
		print v.title() + ' is not in our family'

number = range(1, 10)
for n in number:
	if n == 1:
		print '1st'
	elif n ==2:
		print '2nd'
	elif n ==3:
		print '3rd'
	else:
		print str(n) + 'th'
