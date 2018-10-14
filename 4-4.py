places = ['zhongguo', 'riben', 'meiguo', 'faguo', 'yingguo', 'hanguo', 'deguo']
print places
print places[:3]
print places[2:5]
print places[-3:]

places1 = places[:]
places.append('jianada')
places1.append('moxige')
print places
for place in places1:
	print place
