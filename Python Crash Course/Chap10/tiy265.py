filename = 'guest.txt'

name = input("What is your name?")

with open(filename, 'w') as file_object:
	file_object.write(name)

filename = 'guest_book.txt'
while name != 'q':
	name = input("Please enter your name to start or 'q' to quit")
	if name != 'q':
		with open(filename, 'a') as file_object:
			file_object.write(f"{name}\n")

filename = 'reasons.txt'
reason = ''
while reason != 'q':
	reason = input("Please enter why you love programming to start or 'q' to quit")
	if reason != 'q':
		with open(filename, 'a') as file_object:
			file_object.write(f"{reason}\n")			