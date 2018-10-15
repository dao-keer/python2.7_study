car = raw_input('which car do you want to bug? ')
print 'ok, let me see if i can find you a ' + car

number = raw_input('how many people eat? ')
if int(number) > 8:
    print 'no more seats, sorry'
else:
    print 'please have a seat'

number = raw_input('please enter a number? ')
if int(number) % 10 == 0:
    print 'this number is a multiple of 10'
else:
    print 'this number is not a multiple of 10'