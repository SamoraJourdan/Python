known_users = ["Sam", "Faith", "Shayn", "Tumi", "Nadine", "Bob", "Charlie", "Stan"]

while True:
	print("Hi, my name is Travis")
	name = input("What is your name?: ").strip().title()

	if name in known_users:
		print(f"Hello {name}!")
		remove = input("Would you like to be removed from the system? (y/n) ").lower()
		if remove == 'y':
			known_users.remove(name)
		elif remove == 'n':
			print("No worries, we would have hated to see you leave")	
	else:
		print(f"Hmm i havent met you {name}.")
		add_me = input("Would you like to be added to the system? (y/n) ").lower()
		if add_me == 'y':
			known_users.append(name)
		elif add_me == 'n':
			print("No worries, see you around")
				