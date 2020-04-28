#!/usr/bin/python

from settings import settings_chores
from extract import extract_chores_from_csv

import importlib

class ControllerChores:

		def __init__(self):
			self.initChoresSettings()
			self.initChoresData()

		@property
		def settings(self):
			return self._settings

		@settings.setter
		def settings(self, settings):
			self._settings = settings

		@property
		def choreData(self):
			return self._choreData

		@choreData.setter
		def choreData(self, choreData):
			self._choreData = choreData

		@property
		def choreMode(self):
			return self._choreMode

		@choreMode.setter
		def choreMode(self, choreMode):
			self._choreMode = choreMode

		def initChoresSettings(self):
			self._settings = settings_chores.SettingsChores()
			self._settings.loadSettings()
		
		def initChoresData(self):
			choresExtractCSV = extract_chores_from_csv.ExtractChoresFromCSV(self._settings.sourceFile)
			choresExtractCSV.importChores()

			self._choreData = choresExtractCSV.chores

			module = importlib.import_module('mode.chores_mode')
			class_ = getattr(module, self._settings.mode)
			self._choreMode = class_(list(self._choreData), self._settings)
			self._choreMode.sortChores()





