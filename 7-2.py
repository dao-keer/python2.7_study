flag = True
while(flag):
    age = raw_input('please tell me your age: ')
    age = int(age)
    if age > 0 and age < 3:
        print 'free'
    elif age >= 3 and age < 12:
        print '10 dollars'
    elif age >= 12:
        print '15 dollars'
    else:
        flag = False
        print 'age is illegal'