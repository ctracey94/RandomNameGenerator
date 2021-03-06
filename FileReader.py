#
# The purpose of this class is to read the name files (firstNames.txt, lastNames.txt)
# into memory
#

class FileReader:

	def __init__(self):
		self._first_names = []
		self._first_names_total = 0
		self._last_names = []
		self._last_names_total = 0

	def read(self):
		# this function will read both name txt files into memory in their entirety

		# starting with firstNames.txt
		FN = open('firstNames.txt', 'r')
		self._first_names_total = int(FN.readline())		#the first entry should be the number of entries

		for line in FN:
			self._first_names.append(line.rstrip())		# remove \n, and add to list
		FN.close()

		# then lastNames.txt
		LN = open('lastNames.txt', 'r')
		self._last_names_total = int(LN.readline())

		for line in LN:
			self._last_names.append(line.rstrip())
		LN.close()

	def getFirstNames(self):
		return self._first_names

	def getLastNames(self):
		return self._last_names

	def getFirstNamesTotal(self):
		return self._first_names_total

	def getLastNamesTotal(self):
		return self._last_names_total









