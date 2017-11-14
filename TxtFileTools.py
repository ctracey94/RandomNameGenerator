

def retotal(filename):
	#totals number of entries

	approved = ['firstNames.txt', 'lastNames.txt']
	if filename not in approved:
		return

	F = open(filename, 'r+')
	F.readline()

	total = 0

	while F.readline() != '':
		total+=1

	F.close()

	print(total)
