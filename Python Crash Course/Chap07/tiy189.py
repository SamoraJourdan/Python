sandwich_orders = ["Tuna", "BLT", "Pastrami", "Bacon", "Pastrami", "Peanut Butter", "Marmite", "Pastrami"]
finished_sandwiches = [] 
while sandwich_orders:
	sandwich = sandwich_orders.pop()
	if sandwich != "Pastrami":
		finished_sandwiches.append(sandwich)
		print(f"Making a {sandwich} sandwich")
	else:
		print("We are out of Pastrami")			

print(finished_sandwiches)
print(sandwich_orders)

responses = {}
polling_active = True
while polling_active:
	name = input("\nWhat is your name?")
	response = input("What is your dream vacation?")
	responses[name] = response
	repeat = input("Would you like to let another person respond? (yes/ no) ")
	if repeat == 'no':
		polling_active = False
print("\n--- Poll Results ---")
for name, response in responses.items():
	print(f"{name}'s dream vacation is:' {response}.")