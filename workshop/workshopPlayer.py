#!/usr/bin/python
# -*- coding: utf-8 -*-
from workshopShips import *


class Player(object):

    def __init__(self, name):
        self.__name = name
        self.__turn = False
        self.__wins = 0
        self.__ships = Ship()

    def addVictory(self):
        self.__wins += 1

    def getVictories(self):
        return self.__wins

    def getName(self):
        return self.__name

    def getTurn(self):
        return self.__turn

    def getShips(self):
        return self.__ships

    def setName(self, name):
        self.__name = name

    def setTurn(self):
        if(self.__turn):
            self.__turn = False
        else:
            self.__turn = True
