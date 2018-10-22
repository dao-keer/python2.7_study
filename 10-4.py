import json

def get_favorite_num(file_name):
	try:
		with open(file_name) as file_object:
			num = json.load(file_object)
	except:
		print 'load from file error!'
		return None
	else:
		return num

def set_favorite_num(file_name):
	num = raw_input('please enter your favorite number: ')
	try:
		with open(file_name, 'w') as file_object:
			json.dump(num, file_object)
	except: 
		print 'open file error!'
	else:
		print 'set your favorite number successful!'

file_name = 'favorite_num.json'
set_favorite_num(file_name)
print get_favorite_num(file_name)
