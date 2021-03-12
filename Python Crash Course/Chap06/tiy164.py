python = {
	'rstrip': 'strip spaces to the right', 
	'if': 'execute statement if condition is true', 
	'lstrip': 'strip spaces to the left', 
	'strip': 'strip spaces to left and right',
	'elif': 'execute statement if previous if false and current condition true',
	'for': 'begin a for loop',
	'set': 'collection with only unique values'
	}

for k,v in python.items():
	print(f"{k}: {v}.")	

rivers = {'nile': 'egypt', 'amazon': 'brazil', 'limpopo': 'limpopo'}	
for k,v in rivers.items():
	print(f"The {k} runs through {v}.")	
for k in rivers:
	print(k)	
for v in rivers.values():
	print(v)	

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

people = ['jen', 'sam', 'bob', 'phil']

for person in people:
	if person not in favorite_languages.keys():
		print(f"Please take our poll {person.title()}")
	else:
		print(f"Thanks for taking the poll {person.title()}")	