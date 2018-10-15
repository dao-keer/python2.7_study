personInfo = {
	'name': 'dao-keer',
	'age': 20,
	'sex': 'male',
	'city': 'wuhan',
	'firstName': 'dao',
	'lastName': 'keer'
}

for i, v in personInfo.items():
    print i + ': ' + str(v)

for i in personInfo.keys():
    print i

for v in personInfo.values():
    print v

keys = ['name', 'age', 'weight']
for i in personInfo.keys():
    if i not in keys:
        print 'please tell us your ' + i
    else:
        print 'now, we get your ' + i
