from user import User

class Privilege(object):
	def __init__(self):
		self.privileges = ["can add post", "can delete post", "can ban user"]

class Admin(User):
	def __init__(self, name, age, sex):
		super(Admin, self).__init__(name, age, sex)
		self.privilegeObj = Privilege()
	
	def showPrivileges(self):
		for i in self.privilegeObj.privileges:
			print i
