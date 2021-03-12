person = {'first': 'Faith', 'last': 'Ndlovu', 'city': 'Joburg'}
print(person)
	
fav_nums = {'sam': 1, 'faith': 2, 'john': 3, 'bob': 4, 'sally': 5}
fav_num = fav_nums.get('faith')
print(f"Faiths Favorite num is: {fav_num}.")
fav_num = fav_nums.get('john')
print(f"Johns Favorite num is: {fav_num}.")
fav_num = fav_nums.get('bob')
print(f"Bobs Favorite num is: {fav_num}.")
fav_num = fav_nums.get('sally')
print(f"Sallys Favorite num is: {fav_num}.")
fav_num = fav_nums.get('sam')
print(f"Sams Favorite num is: {fav_num}.")

python = {
	'rstrip': 'strip spaces to the right', 
	'if': 'execute statement if condition is true', 
	'lstrip': 'strip spaces to the left', 
	'strip': 'strip spaces to left and right',
	'elif': 'execute statement if previous if false and current condition true'
	}
print(f"rstrip: {python.get('rstrip')}\n")	
print(f"if: {python.get('if')}\n")	
print(f"lstrip: {python.get('lstrip')}\n")	
print(f"strip: {python.get('strip')}\n")	
print(f"elif: {python.get('elif')}\n")	