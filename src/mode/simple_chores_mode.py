#!/usr/bin/python

from chores_mode import ChoresMode


class SimpleChoresMode(ChoresMode):

    def __init__(self, chores, settings):
        super(SimpleChoresMode, self).__init__(chores, settings)

    def is_simple(self, chore):
        return len(chore) == 1

    def sortChores(self):
        super(SimpleChoresMode, self).sortChores()
        self._chores = filter(lambda chore: self.is_simple(chore), self._chores)
    