from random import randint, choice

class Die:
	def __init__(self, sides):
		self.sides = sides

	def roll(self):
		return randint(1, self.sides)

six = Die(6)		
print(six.roll())
print(six.roll())
print(six.roll())
print(six.roll())
print(six.roll())
print(six.roll())
print(six.roll())
print(six.roll())
print(six.roll())
print(six.roll())
six = Die(10)		
print(six.roll())
print(six.roll())
print(six.roll())
print(six.roll())
print(six.roll())
print(six.roll())
print(six.roll())
print(six.roll())
print(six.roll())
print(six.roll())
six = Die(20)		
print(six.roll())
print(six.roll())
print(six.roll())
print(six.roll())
print(six.roll())
print(six.roll())
print(six.roll())
print(six.roll())
print(six.roll())
print(six.roll())

lotto = ['a', 'b', 'c', 'd', 'e', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10' ]
num = 0
string = [] 
my_ticket = ['d', '4', 'a', '6', 'e']
while string != my_ticket:
	string = []
	string.append(choice(lotto))
	string.append(choice(lotto))
	string.append(choice(lotto))
	string.append(choice(lotto))
	string.append(choice(lotto))

	num += 1	
	print(string)
print("You Won!")
print(num)
