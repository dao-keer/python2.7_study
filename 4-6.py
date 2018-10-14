age = 20
print 'are you 20 years old?'
if (age == 20):
	print "yes, I'm 20 years old"
else:
	print "no"

name = 'Dao Keer'
if name == 'dao keer':
	print 'yes'
else:
	print 'no'
if name.lower() == 'dao keer':
	print 'yes'
else:
	print 'no'


if age > 18 and age < 25:
	print 'you are young'
else:
	print 'you are little'

if age < 12 or age > 80:
	print 'you are protected'
else:
	print 'not'

if age in [1, 2, 3, 18, 91]:
	print 'yes'
else:
	print 'no'
