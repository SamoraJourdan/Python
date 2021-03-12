nums = list(range(1, 21))
for num in nums:
	print(f"{num}")

#nums = list(range(1, 1000000))
#for num in nums:
#	print(f"{num}")

#print(f"{min(nums)}")
#print(f"{max(nums)}")
#print(f"{sum(nums)}")

odds = list(range(1, 20, 2))
for odd in odds:
	print(f"{odd}")

mults_of_three = [(value*3) for value in range(1, 11)]
for mult_of_three in mults_of_three:
	print(f"{mult_of_three}")

cubes = [(value**3 for value in range(1, 11))]
for cube in cubes:
	print(f"{cube}")

