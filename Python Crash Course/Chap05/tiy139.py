alien_colour = 'red'
if alien_colour == 'red':
	print("You get 5 points")
if alien_colour == 'green':
	print("You get 5 points")

if alien_colour == 'green':
	print("You get 5 points")
else:
	print("You get 10 points")

if alien_colour == 'green':
	print("You get 5 points")
elif alien_colour != 'green':
	print("You get 10 points")

alien_colour = 'yellow'
if alien_colour == 'green':
	print("You get 5 points")
elif alien_colour == 'yellow':
	print("You get 10 points")
elif alien_colour == 'red':
	print("You get 15 points")

alien_colour = 'red'
if alien_colour == 'green':
	print("You get 5 points")
elif alien_colour == 'yellow':
	print("You get 10 points")
elif alien_colour == 'red':
	print("You get 15 points")

alien_colour = 'green'
if alien_colour == 'green':
	print("You get 5 points")
elif alien_colour == 'yellow':
	print("You get 10 points")
elif alien_colour == 'red':
	print("You get 15 points")

age = 45

if age < 2:
	print("Youre a Baby")
elif age >= 2 and age < 4:
	print("Youre a Toddler")
elif age >= 4 and age < 13:
	print("Youre a Kid")
elif age >= 13 and age < 20:
	print("Youre a Teenager")	
elif age >= 20 and age < 65:
	print("Youre an Adult")
elif age > 65:
	print("Youre an Eldar")		

fruits = ['Apple', 'Banana']	
if 'Kiwi' in fruits:
	print('MMMM Kiwis')
if 'Banana' in fruits:
	print('MMMM Bananas')
if 'Mango' in fruits:
	print('MMMM Mangos')
if 'Apple' in fruits:
	print('MMMM Apples')
if 'Leechee' in fruits:
	print('MMMM Leechees')
