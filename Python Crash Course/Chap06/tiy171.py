people = {
	'fndlovu': {
	'first': 'Faith', 
	'last': 'Ndlovu', 
	'city': 'Joburg'
	},
	'sjourdan': {
	'first': 'Sam', 
	'last': 'Jourdan', 
	'city': 'Joburg'
	},
	'tjourdan': {
	'first': 'Tumi', 
	'last': 'Jourdan', 
	'city': 'Joburg'
	}
}

for v in people.values():
	full_name = f"{v['first']} {v['last']}"
	print(f"{full_name} lives in {v['city']}")

jaws = {'animal':'fish', 'owner': 'Jake'}
spud = {'animal':'dog', 'owner': 'Sam'}
fluffy = {'animal':'cat', 'owner': 'Faith'}

pets =[jaws, spud, fluffy]

for pet in pets:

	print(f"{pet.get('owner')} owns a {pet.get('animal')}")

fav_places = {
	'Sam': ["South Africa", "China"],
	'Faith': ["Malawi", "London"],
	'Tumi': ["The Abyss", "Disneyland"]
}

for k,v in fav_places.items():
	print(f"{k}'s favorite places are: ")
	for place in v:
		print(place) 

fav_nums = {
	'sam': [1,2,7], 
	'faith': [3,4,8], 
	'john': [5,6,9], 
	'bob': [7,8,99], 
	'sally': [9,10,323]}

for k,v in fav_nums.items():
	print(f"{k.title()}'s favorite numbers are: ")
	for num in v:
		print(num) 	

cities = {
	'Joburg': {
	'country': 'South Africa',
	'population': '5 million',
	'fact': 'has serious crime'
	},
	'London': {
	'country': 'Britain',
	'population': '10 million',
	'fact': 'has terrible weather'
	},
	'Rio': {
	'country': 'Brazil',
	'population': '11 million',
	'fact': 'has worse crime than Joburg'
	}
	
}		

for city, values in cities.items():
	print(f"Did you know that {city} in {values['country']} with a population of {values['population']} {values['fact']}." )