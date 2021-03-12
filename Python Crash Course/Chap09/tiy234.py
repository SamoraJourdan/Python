class Restaurant:
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.num_served = 0

	def describe_restaurant(self):
		print(f"{self.restaurant_name.title()} serves {self.cuisine_type.title()}.")	

	def open_restaurant(self):
		print(f"{self.restaurant_name.title()} is open for buisness!")

	def set_num_served(self, num):
		self.num_served = num

	def inc_num_served(self, inc):
		self.num_served += inc
	

del_forno = Restaurant("del forno", "pizza  & pasta")
print(del_forno.num_served)
del_forno.num_served = 23
print(del_forno.num_served)
del_forno.set_num_served(66)
print(del_forno.num_served)
del_forno.inc_num_served(4)
print(del_forno.num_served)

class Users:
	def __init__(self, first_name, last_name, email, password):
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.password = password
		self.login_attempts = 0

	def describe_user(self):
		print(f"{self.first_name.title()} {self.last_name.title()} has the email: {self.email} and the password: {self.password}.")

	def inc_login_attempts(self):
		self.login_attempts +=1	

	def reset_login_attempts(self):
		self.login_attempts = 0	

sam = Users('Sam', 'Jourdan', "sj@gmail.com", 'ello')
sam.inc_login_attempts()	
print(sam.login_attempts)
sam.inc_login_attempts()	
print(sam.login_attempts)
sam.inc_login_attempts()	
print(sam.login_attempts)
sam.inc_login_attempts()	
print(sam.login_attempts)
sam.inc_login_attempts()	
print(sam.login_attempts)
sam.inc_login_attempts()	
print(sam.login_attempts)
sam.reset_login_attempts()	
print(sam.login_attempts)