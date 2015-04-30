#!/usr/bin/python
# -*- coding: utf-8 -*-
from workshopShips import *


class Player(object):

    def __init__(self, name):
        self.__name = name
        self.__turn = False
        self.__mainboard = [[0 for i in range(10)] for j in range(10)]
        self.__fireboard = [[0 for i in range(10)] for j in range(10)]

    # Checks if x and y are valid
    def validadesCoordinates(self, x, y):
        # Checks if position is valid
        if(x < 10 and x >= 0 and y < 10 and y >= 0):
            return True
        else:
            return False

    def getName(self):
        return self.__name

    def getTurn(self):
        return self.__turn

    def getMainBoard(self):
        return self.__mainboard

    def getFireBoard(self):
        return self.__fireboard

    def SetFireBoard(self, x, y, type):
        if self.validadesCoordinates(x, y):
            self.__fireboard[y][x] = type
            return True
        else:
            return False

    def SetMainBoard(self, x, y, type):
        if self.validadesCoordinates(x, y):
            self.__mainboard[y][x] = type
            return True
        else:
            return False

    def setName(self, name):
        self.__name = name

    def setTurn(self):
        if(self.__turn):
            self.__turn = False
        else:
            self.__turn = True
