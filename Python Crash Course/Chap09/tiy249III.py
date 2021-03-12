from tiy249 import Users

class Admin(Users):		
	def __init__(self, first_name, last_name, email, password):
		super().__init__(first_name, last_name, email, password)
		self.privileges = Privileges()

	

class Privileges:
	def __init__(self):
		self.privileges = ["can add post", "can delete post", "can ban user"]

	def show_privileges(self):
		print(self.privileges)			