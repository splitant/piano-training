#!/usr/bin/python

import random

class ChoresMode:
    MODE = 'Normal'

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

class MinorMajorChoresMode(ChoresMode):
    MODE = 'Minor - Major'

    def __init__(self, chores, settings):
        super(MinorMajorChoresMode, self).__init__(chores, settings)

    def is_minor(self, chore):
        return len(chore) == 1 and chore.isupper()

    def is_major(self, chore):
        return len(chore) == 2 and chore[len(chore) - 1] == 'm'

    def sortChores(self):
        super(MinorMajorChoresMode, self).sortChores()
        self._chores = list(filter(lambda chore: self.is_major(
            chore) or self.is_minor(chore), self._chores))

class SimpleChoresMode(ChoresMode):
    MODE = 'Single'

    def __init__(self, chores, settings):
        super(SimpleChoresMode, self).__init__(chores, settings)

    def is_simple(self, chore):
        return len(chore) == 1 and chore.islower()

    def sortChores(self):
        super(SimpleChoresMode, self).sortChores()
        self._chores = filter(lambda chore: self.is_simple(chore), self._chores)
