users = ["Admin", "Sam", "Faith", "Bob", "Paul"]

for user in users:
	if user == "Admin":
		print("Welcome Admin, do as you will")
	else:
		print(f"Welcome {user}")

users = []
if users:
	for user in users:
		if user == "Admin":
			print("Welcome Admin, do as you will")
		else:
			print(f"Welcome {user}")
else:
	print("No users found")

new_users = ["admin", "sam", "faith", "bob", "paul"]
current_users = ["Admin", "Steve", "Bob", "Jane", "Sally"]
current_usersUpper = ["ADMIN", "STEVE", "BOB", "JANE", "SALLY"]

for user in new_users:
	if user.title() in current_users or user in current_users:
		print(f"Username: {user} unavailable!")
	else:
		print(f"Username: {user} Available!")	

nums = list(range(1,11))

for num in nums:
	if num < 3:
		print(f"{num}nd")
	elif num == 3:
		print(f"{num}rd")	
	else:
		print(f"{num}th")	