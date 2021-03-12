Gods = {
	'Hammer': {
	'god_of':'thunder',
	'name': 'Thor',
	'culture' : 'Norse',
	},
	'Styx': {
	'god_of':'Death',
	'name': 'Hades',
	'culture' : 'Greek',
	},
}

for godname, god_info in Gods.items():
	print(f"\nGod: {godname}")
	FullName = f"{god_info['name']} god of {god_info['god_of']}!"
	culture = god_info['culture']

	print(f"\t Full Name: {FullName.title()}")
	print(f"\t Culture: {culture.title()}")	

