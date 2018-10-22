from collections import OrderedDict
from random import randint

wordDict = {}
wordDict['China'] = 'a beautiful country'
wordDict['Chinese'] = 'people in China'

for key in wordDict:
	print key + ': ' + wordDict[key]


class Die(object):
	def __init__(self, maxNum):
		self.maxNum = maxNum
	
	def rollNum(self):
		res = []
		for i in range(1, self.maxNum + 1):
			res.append(randint(1, self.maxNum))
		print res

die6 = Die(6)
die6.rollNum()
die10 = Die(10)
die10.rollNum()
die20 = Die(20)
die20.rollNum()