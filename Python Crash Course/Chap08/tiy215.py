def make_sandwich(*toppings):
	print("Your sandwich will contain:")
	for topping in toppings:
		print(topping)

make_sandwich('Tomato')	
make_sandwich('Tomato', 'Bacon')	
make_sandwich('Tomato', 'Bacon', 'Lettuce')			

def build_profile(first, last, **user_info):
	user_info['first_name'] = first
	user_info['last_name'] = last
	return user_info
user_profile = build_profile('sam', 'jourdan', location='code college', field='programming', interest= 'reading')
print(user_profile)

def make_car(manufacturer, model, **car_info):
	car_info['manufacturer'] = manufacturer
	car_info['model'] = model
	return car_info
car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)