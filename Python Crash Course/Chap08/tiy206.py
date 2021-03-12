def city_country(city, country):
	message = f"{city}, {country}"
	return message
string = city_country("Joburg", "South Africa")
print(string)
string = city_country("Durban", "South Africa")
print(string)
string = city_country("Cape Town", "South Africa")
print(string)


def make_album(artist, title, num_songs=""):
	if num_songs:
		album = {'artist' : artist, 'title' : title, 'song_num' : num_songs}
	else:
		album = {'artist' : artist, 'title' : title}
	return album
album = make_album('Gorillaz', 'Plastic Beach', "11") 
print(album)
album = make_album('Gorillaz', 'Feel good', "20") 
print(album)
album = make_album('Gorillaz', 'The Fall') 
print(album)	

while True:
	print("\nPlease tell me your albums artist and title:")
	print("(enter 'q' at any time to quit)")
	artist = input("Artist: ")
	if artist == 'q':
		break
	title = input("Album title: ")
	if title == 'q':
		break
	album = make_album(artist, title)
	print(album)
