animals = ['Cat', 'Dog', 'Fish', 'Mouse', ' Rat']
print(f"The first three animals are: {animals[:3]}.")
print(f"The middle three animals are: {animals[1:4]}.")
print(f"The last three animals are: {animals[2:]}.")

pizzas = ['Hawaian', 'Mexican', 'Margarita']
friend_pizzas = pizzas[:]
pizzas.append('Formaggi')
friend_pizzas.append('Anchovies')
print(f"{pizzas}")
print(f"{friend_pizzas}")

my_foods = ['pizza', 'falafel', 'carrot cake'] 
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for food in my_foods:
	print(food)

print("\nMy friend's favorite foods are:")
for food in friend_foods:
	print(food)