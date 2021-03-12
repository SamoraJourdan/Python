class Restaurant:
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print(f"{self.restaurant_name.title()} serves {self.cuisine_type.title()}.")	

	def open_restaurant(self):
		print(f"{self.restaurant_name.title()} is open for buisness!")	

class Users:
	def __init__(self, first_name, last_name, email, password):
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.password = password

	def describe_user(self):
		print(f"{self.first_name.title()} {self.last_name.title()} has the email: {self.email} and the password: {self.password}.")

