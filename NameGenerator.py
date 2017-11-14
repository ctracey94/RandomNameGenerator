from random import randint
from FileReader import FileReader

class NameGenerator:

	def __init__(self):
		FR = FileReader()
		FR.read()

		self._first_names = FR.getFirstNames()
		self._first_names_total = FR.getFirstNamesTotal()
		self._last_names = FR.getLastNames()
		self._last_names_total = FR.getLastNamesTotal()

		del FR

	def generateName(self):
		first_index = randint(0, self._first_names_total-1)
		last_index = randint(0, self._last_names_total-1)

		name = self._first_names[first_index] + ' ' + self._last_names[last_index]

		return name