import random
alien_color = ('red', 'yellow', 'green')
now_color = alien_color[random.randint(0, 2)]
print now_color

if now_color == 'red':
	print 'you scored 5 points'
elif now_color == 'yellow':
	print 'you scored 10 points'
else:
	print 'you scored 15 points'
