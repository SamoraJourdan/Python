message = ""
while message != 'quit':
	message = input("Please enter a topping for your pizza")
	print(f"adding {message} to your pizza")

message2 = ""
active = 0
while active < 5 :
	message2 = input("Please enter your age")
	if message2 == 'quit':
		break
	elif int(message2) < 3:
		print("your ticket is free")
		active += 1	
	elif int(message2) > 3 and int(message2) <= 12:
	 	print("your ticket is $10")
	 	active += 1	
	else: 	
		print("your ticket is $15")
		active += 1	

