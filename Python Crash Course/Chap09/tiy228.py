class Restaurant:
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print(f"{self.restaurant_name.title()} serves {self.cuisine_type.title()}.")	

	def open_restaurant(self):
		print(f"{self.restaurant_name.title()} is open for buisness!")	

del_forno = Restaurant("del forno", "pizza  & pasta")
turn_and_tender = Restaurant("turn and tender", "steak")
chicken_licken = Restaurant("chicken licken", "hotwings")
turn_and_tender.describe_restaurant()
chicken_licken.describe_restaurant()
del_forno.describe_restaurant()
del_forno.open_restaurant()

class Users:
	def __init__(self, first_name, last_name, email, password):
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.password = password

	def describe_user(self):
		print(f"{self.first_name.title()} {self.last_name.title()} has the email: {self.email} and the password: {self.password}.")

sam = Users('Sam', 'Jourdan', "sj@gmail.com", 'ello')	
tumi = Users('Tumi', 'Jourdan', "tj@gmail.com", '1234')			
paul = Users('Paul', 'Jourdan', "ppj@gmail.com", 'zzz')	

sam.describe_user()
tumi.describe_user()
paul.describe_user()
