message = input("What car would you like?: ")
print(f"I can get you a {message}")

num_guests = input("Please enter the number of guests in your party: ")
if int(num_guests) > 8:
	print("Sorry you'll have to wait for a table")
else:
	print("Your table is ready")	

number = input("Enter a number: ")
if int(number) % 10 == 0:
	print("Your number is a multiple of 10")
else:
	print("Your number is not a multiple of 10")	