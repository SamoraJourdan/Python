class Restaurant:
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print(f"{self.restaurant_name.title()} serves {self.cuisine_type.title()}.")	

	def open_restaurant(self):
		print(f"{self.restaurant_name.title()} is open for buisness!")	

class IceCreamStand(Restaurant):
	def __init__(self, restaurant_name, cuisine_type):
		super().__init__(restaurant_name, cuisine_type)
		self.ice_cream_flavours = ["Chocolate", "Vanilla", "Bubblegum"]

	def display_flavours(self):
		print(self.ice_cream_flavours)	

jojo = IceCreamStand('JoJo', 'Ice Cream')	
jojo.display_flavours()	

class Users:
	def __init__(self, first_name, last_name, email, password):
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.password = password

	def describe_user(self):
		print(f"{self.first_name.title()} {self.last_name.title()} has the email: {self.email} and the password: {self.password}.")

class Admin(Users):		
	def __init__(self, first_name, last_name, email, password):
		super().__init__(first_name, last_name, email, password)
		self.privileges = Privileges()

	

class Privileges:
	def __init__(self):
		self.privileges = ["can add post", "can delete post", "can ban user"]

	def show_privileges(self):
		print(self.privileges)	


sam = Admin('Sam', 'Jourdan', "sj@gmail.com", 'ello')
sam.privileges.show_privileges()			

class Car:
	"""A simple attempt to represent a car."""
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
	def get_descriptive_name(self):
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()
	def read_odometer(self):
		print(f"This car has {self.odometer_reading} miles on it.")
	def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")
	def increment_odometer(self, miles):
		self.odometer_reading += miles

class Battery:
	"""A simple attempt to model a battery for an electric car."""
	def __init__(self, battery_size=75):
		"""Initialize the battery's attributes."""
		self.battery_size = battery_size
	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print(f"This car has a {self.battery_size}-kWh battery.")
	def get_range(self):
		"""Print a statement about the range this battery provides."""
		if self.battery_size == 75:
			range = 260
		elif self.battery_size == 100:
			range = 315
		print(f"This car can go about {range} miles on a full charge.")	
	def upgrade_battery(self):
		if self.battery_size	!= 100:
			self.battery_size = 100		

class ElectricCar(Car):
	"""Represent aspects of a car, specific to electric vehicles."""
	def __init__(self, make, model, year):
		"""Initialize attributes of the parent class."""
		super().__init__(make, model, year)
		self.battery = Battery()
	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print(f"This car has a {self.battery_size}-kWh battery.")	




my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()