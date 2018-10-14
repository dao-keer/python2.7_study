number1_20 = range(1, 21)
print number1_20

number1000000 = range(1, 1000001)
print "mix: " + str(min(number1000000))
print "max: " + str(max(number1000000))
print "sum: " + str(sum(number1000000))

number1 = range(1, 21, 2)
for num in number1:
	print num

number2 = range(3, 31, 3)
for num in number2:
	print num

number3 = [x ** 3 for x in range(1, 11)]
for num in number3:
	print num

number4 = []
for num in range(1, 11):
	number4.append(num ** 3)
print number4
