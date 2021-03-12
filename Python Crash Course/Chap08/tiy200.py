def make_shirt(size="large" , message="I love python!"):
	print(f"Printing a size {size} shirt that says: {message}.")
make_shirt("large", "WOLLOOOWLOO")	
make_shirt(message="WWWWW", size="medium")
make_shirt()
def describe_city(city, country="South Africa"):
	print(f"{city.title()} is in {country}.")
describe_city("Johannesburg")
describe_city("Durban")
describe_city("Monrovia", "Liberia")