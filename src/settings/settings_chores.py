#!/usr/bin/python

class SettingsChores:

   def __init__(self, ordered = True, timer = 500, sourceFile = '../../source/letter_schema_chores.csv'):
      self._ordered = ordered
      self._timer = timer
      self._sourceFile = sourceFile
   
   @property
	def ordered(self):
		return self._ordered

	@ordered.setter
	def ordered(self, ordered):
		self._ordered = ordered
   
   @property
	def timer(self):
		return self._timer

	@timer.setter
	def timer(self, timer):
		self._timer = timer

   @property
	def sourceFile(self):
		return self._sourceFile

	@sourceFile.setter
	def sourceFile(self, sourceFile):
		self._sourceFile = sourceFile
