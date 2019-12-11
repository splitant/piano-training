#!/usr/bin/python

from chores_mode import ChoresMode


class MinorMajorChoresMode(ChoresMode):

    def __init__(self, chores, settings):
        super(MinorMajorChoresMode, self).__init__(chores, settings)

    def is_minor(self, chore):
        return len(chore) == 1
    
    def is_major(self, chore):
        return len(chore) == 2 and chore[len(chore) - 1] == 'm'

    def sortChores(self):
        super(MinorMajorChoresMode, self).sortChores()
        self._chores = filter(lambda chore: self.is_major(chore) or self.is_minor(chore), self._chores)
    