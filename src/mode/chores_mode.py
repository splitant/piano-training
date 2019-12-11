#!/usr/bin/python

import random

class ChoresMode:

    def __init__(self, chores, settings):
        self._chores = chores
        self._settings = settings

    @property
    def chores(self):
        return self._chores

    @chores.setter
    def chores(self, chores):
        self._chores = chores
    
    @property
    def settings(self):
        return self._settings

    @settings.setter
    def settings(self, settings):
        self._settings = settings
    
    def sortChores(self):
        if not self._settings.ordered:
            random.shuffle(self._chores)
