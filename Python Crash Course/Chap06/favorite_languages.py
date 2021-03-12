peeps = {
	'shayn': 'bro',
	'dylan': 'fam',
	'sophie': 'dude',
	'faith': 'fam',
	}

for peep, relation in peeps.items():
	print(f"{peep.title()}'s is my {relation.title()}.")	

for peep in peeps.keys():
	print(peep.title())

for relation in peeps.values():
	print(relation.title())

for peep in sorted(peeps.keys()):
	print(f"{peep.title()}, wazzuuuuup?")

for relation in set(peeps.values()):
	print(relation.title())