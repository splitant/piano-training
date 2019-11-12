#!/usr/bin/python

class ChoresMode:

    def __init__(self, chores):
      self._chores = chores

    @property
    def chores(self):
      return self._chores

    @chores.setter
    def chores(self, chores):
      self._chores = chores
