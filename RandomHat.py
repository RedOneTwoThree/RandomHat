import random

List = []


while True:

	while True:
		try:
			Number = int(input('Number of Players: '))
		except ValueError:
			print("Not an integer!")
			continue
		else:
			break

	for x in range(0, Number):
		Name = input('Enter the names?')
		List.append(Name)

	value = random.choice(List)

	print(value + " was selected!")

	check = input("Do you want to try again?(y/n)")
	if check == 'y':
		continue

	else: 
		break

