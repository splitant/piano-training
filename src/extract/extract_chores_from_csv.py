#!/usr/bin/python

import csv

class ExtractChoresFromCSV:

		def __init__(self, sourceFile, fieldNames = ['chore_label', 'chore_picture']):
			self._sourceFile = sourceFile
			self._fieldNames = fieldNames
			self._chores = dict()

		@property
		def sourceFile(self):
			return self._sourceFile

		@sourceFile.setter
		def sourceFile(self, sourceFile):
			self._sourceFile = sourceFile
  
		@property
		def chores(self):
			return self._chores

		@chores.setter
		def chores(self, chores):
			self._chores = chores
		
		@property
		def fieldNames(self):
			return self._fieldNames

		@fieldNames.setter
		def fieldNames(self, fieldNames):
			self._fieldNames = fieldNames

		def importChores(self):
			csvFile = open(self._sourceFile, 'r')
			reader = csv.DictReader(csvFile, self._fieldNames)
			for row in reader:
				self._chores[row[self._fieldNames[0]]] = row[self._fieldNames[1]]

