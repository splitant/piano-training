#!/usr/bin/python

import sqlite3
import sys
import inspect

class SettingsChores:

	def __init__(self, loop=True, ordered=True, timer=500, sourceFile='../source/letter_schema_chores.csv', mode='ChoresMode'):
		self._loop = loop
		self._ordered = ordered
		self._timer = timer
		self._sourceFile = sourceFile
		self._mode = mode

		self._databaseName = 'settings_chore.db'

		conn = sqlite3.connect(self._databaseName)
		cursor = conn.cursor()

		cursor.execute("""
		CREATE TABLE IF NOT EXISTS settings_chore(
				id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
				loop BOOL,
				ordered BOOL,
				timer INTERGER,
				path_chores_source TEXT,
				mode TEXT
		)
		""")

		conn.commit()
		conn.close()

	@property
	def loop(self):
		return self._loop

	@loop.setter
	def loop(self, loop):
		self._loop = loop

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
	
	@property
	def mode(self):
		return self._mode

	@mode.setter
	def mode(self, mode):
		self._mode = mode
	
	def saveSettings(self):
		conn = sqlite3.connect(self._databaseName)
		cursor = conn.cursor()

		idSettings = self.settingsId()
		if not idSettings:
				cursor.execute("""INSERT INTO settings_chore (loop, ordered, timer, path_chores_source, mode) VALUES (?,?,?,?,?)""", 
				(self._loop, self._ordered, self._timer, self._sourceFile, self._mode))
		else:
				cursor.execute("""UPDATE settings_chore SET loop = ?, ordered = ?, timer = ?, path_chores_source = ?, mode = ? WHERE id = ? """,
				(self._loop, self._ordered, self._timer, self._sourceFile, self._mode, idSettings))

		conn.commit()
		conn.close()

	def loadSettings(self):
		conn = sqlite3.connect(self._databaseName)
		cursor = conn.cursor()

		cursor.execute("""SELECT id, loop, ordered, timer, path_chores_source, mode FROM settings_chore""")
		data = cursor.fetchone()

		id = 0
		if data is not None:
			id = data[0]
			self._loop = data[1]
			self._ordered = data[2]
			self._timer = data[3]
			self._sourceFile = data[4]
			self._mode = data[5]

		conn.commit()
		conn.close()

		return id

	def settingsId(self):
		conn = sqlite3.connect(self._databaseName)
		cursor = conn.cursor()

		cursor.execute("""SELECT id FROM settings_chore""")
		data = cursor.fetchone()

		conn.commit()
		conn.close()

		return data[0] if data is not None else 0
	
	def availableModes(self):
		return list(dict(inspect.getmembers(sys.modules["mode.chores_mode"], inspect.isclass)))


