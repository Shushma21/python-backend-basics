class User:
	def __init__(self,username,age):
		self.username = username
		self.age = age

	def is_adult(self):
		if self.age>=18:
			return True
		else:
			return False



class Admin(User):
	def has_permission(self):
		if self.username == 'admin':
			return True
		else :
			return False

	
user1 = User("shushma",14)
admin1 = Admin("admin",24)


print(user1.is_adult())
print(admin1.has_permission())
