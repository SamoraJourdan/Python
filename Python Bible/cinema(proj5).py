films = {
	"Finding Dory": [3,5],
	"Rome": [4,1],
	"Star Wars": [15, 5],
	"Bloodsports": [20,6]

}

while True:
	choice = input("What movie would you like to watch?").strip().title()
	if choice in films:
		age = int(input("How old are you?:").strip())
		if age >= films[choice][0]:
			if films[choice][1] > 0:
				print("Enjoy the film")
				films[choice][1] -= 1
			else:
				print("Sorry, tickets have sold out")	
		else:
			print("You are too young to see that film.")	
	else:
		print("We dont have that film")	
