dinnerPerson = ['a', 'b', 'c']
for v in dinnerPerson:
	print v

notCome = 'b'
print notCome
dinnerPerson[1] = 'd'
print dinnerPerson

print 'find a bigger desk'
dinnerPerson.insert(0, '0')
dinnerPerson.insert(2, '2')
dinnerPerson.append('e')
print dinnerPerson

while(len(dinnerPerson) > 2):
	dinnerPerson.pop()
print dinnerPerson

while(len(dinnerPerson)):
	dinnerPerson.pop()
print dinnerPerson

dinnerPerson = ['a', 'b', 'c']
temp = dinnerPerson.remove('a')
print temp
print dinnerPerson
temp = dinnerPerson.pop(1)
print temp
print dinnerPerson
