def citify(city, country, population = 0):
	if population > 0:
		string = f"{city}, {country} - population {population}"
	else:
		string = f"{city}, {country}"
	return string.title()