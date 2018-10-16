sandwich_orders = ['a', 'b', 'c', 'd', 'c', 'b', 'a']
finished_sandwich = []
while sandwich_orders:
	finished_sandwich.append(sandwich_orders.pop())

for v in finished_sandwich:
	print v + ' is finished!'

while 'a' in finished_sandwich:
	finished_sandwich.remove('a')

for v in finished_sandwich:
	print v
