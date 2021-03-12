import json

filename = 'num.json'
try:
	with open(filename) as f:
		num = json.load(f)
except FileNotFoundError:
	num = input("What is your favorite number?")
	with open(filename, 'w') as f:
		json.dump(num, f)
else:
	print(f"Your favorite number is: {num}")

def get_stored_username():
	"""Get stored username if available."""
	filename = 'username.json'
	try:
		with open(filename) as f:
			username = json.load(f)
	except FileNotFoundError:
		return None
	else:
		return username
def get_new_username():
	"""Prompt for a new username."""
	username = input("What is your name? ")
	filename = 'username.json'
	with open(filename, 'w') as f:
		json.dump(username, f)
		return username
def greet_user():
	"""Greet the user by name."""
	username = get_stored_username()
	if username:
		print(f"Welcome back, {username}!")
		answer = input("Is this you? enter y or n")
		if answer == 'y':
			print("Excellent")
		elif answer == 'n':
			username = get_new_username()
			print(f"We'll remember you when you come back, {username}!")	
		else:
			print("that is not a valid response")	
	else:
		username = get_new_username()
		print(f"We'll remember you when you come back, {username}!")
greet_user()	