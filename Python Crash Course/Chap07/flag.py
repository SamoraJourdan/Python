active = True
while active:
	number = input('Enter a number, ill tell you if its odd or even or type quit to exit')
	if number == "quit":
		active = False
				
	elif int(number) % 2 ==0:
		print(f"The number {number} is even")
	elif int(number) % 2 ==1:
		print(f"The number {number} is odd")
	