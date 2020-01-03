#!/usr/bin/python

import settings as s
import extract as e
import importlib as i

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
			self._settings = s.SettingsChores()
			self._settings.loadSettings()
		
		def initChoresData(self):
			choresExtractCSV = e.ExtractChoresFromCSV(self._settings.sourceFile)
			choresExtractCSV.importChores()

			self._choreData = choresExtractCSV.chores

			module = i.import_module('mode.chores_mode')
			class_ = getattr(module, self._settings.mode)

			self._choreMode = class_(self._choreData.keys(), self._settings)
			self._choreMode.sortChores()





