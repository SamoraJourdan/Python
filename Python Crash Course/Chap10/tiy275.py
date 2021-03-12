# num1 = ""
# num2 = ""
# while num1 != 'q':
# 	try:
# 		num1 = int(input("enter a number or q to quit: "))
# 		num2 = int(input("enter another number: "))
# 		result = num3 + num4
# 		print(result)
# 	except ValueError:
# 		print("Please enter a number not a string")	

filenames = ["cats.txt", 'dogs.txt']	

def read_files(filename):
	try:
		with open(filename, encoding='utf-8') as f:
			contents = f.read()
	except FileNotFoundError:
		pass
	else:
			print(contents)

for filename in filenames:
	read_files(filename)

filenames = ["Exceptions/alice.txt", 'Exceptions/moby_dick.txt']	

def read_files(filename):
	try:
		with open(filename, encoding='utf-8') as f:
			contents = f.read()
	except FileNotFoundError:
		pass
	else:
			count = contents.count('the ')
			print(count)

for filename in filenames:
	read_files(filename)