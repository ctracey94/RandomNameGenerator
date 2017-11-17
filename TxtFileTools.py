
APPROVED = ['firstNames.txt', 'lastNames.txt']

def getEntries(file):
	# returns a list of entries from filename

	file.seek(0)
	file.readline()				#skip past entry count

	entries = []

	for line in file:
		entries.append(line.rstrip())

	return entries


def deleteContent(file):
	file.seek(0)
	file.truncate()



def retotal(filename):
	#totals number of entries
	#prints result

	if filename not in APPROVED:
		return

	F = open(filename, 'r')
	F.readline()

	total = 0

	while F.readline() != '':
		total+=1

	F.close()

	print(total)


def alphabetize(filename):
	# alphabetizes file entries

	if filename not in APPROVED:
		return

	F = open(filename, 'r+')

	entries = getEntries(F)
	entries.sort()

	F.seek(0)		#delete file content
	F.truncate()	#

	for i in range(len(entries)-1):
		F.write(entries[i] + '\n')			#return newline characters
	F.write(entries[-1])					#except for final entry

	F.close()


def find(target, filename):
	# return True if target is entry in filename, False if not

	F = open(filename, 'r')

	entries = getEntries(F)

	F.close()

	return target in entries










