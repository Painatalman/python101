#!/usr/bin/python
# -*- coding: utf-8 -*-
from workshopPlayer import *
from workshopShips import *
from workshopPoint import *
from random import random


class Game(object):

    def __init__(self):
        self.__name = "Battleship"
        self.__player = []
        self.__board = [[0 for i in range(10)] for j in range(10)]

    def getPlayer(self, numberOfPlayer):
        return self.__player[numberOfPlayer-1]

    def coinToss(self):
        if(random() > 0.5):
            return 2
        else:
            return 1

    def showBoard(self):
        rowNumber = 0
        print "Board:\n  |",
        # Column Numbers
        for i in range(0, 10):
            print i,
        print "|"
        # Line Top
        print "-" * 25,
        print
        for row in self.__board:
            # Row Numbers
            print str(rowNumber) + " |",
            # Print Board
            for col in row:
                print col,
            print "|"
            rowNumber += 1

    def start(self):
        print "Insert First Player Name:"
        # DEBUG
        #player = Player(raw_input())
        player = Player("Fonseca")
        self.__player.append(player)
        print "Insert Second Player Name:"
        # DEBUG
        #player = Player(raw_input())
        player = Player("Meireles")
        self.__player.append(player)
        # Determinates who goes first
        toss = self.coinToss()
        self.getPlayer(toss).setTurn()
        print "Player " + self.getPlayer(toss).getName() + " starts"
        # First player fills the board
        self.showBoard()
        # Second player fills the board


        self.mainLoop()

    def mainLoop(self):
        # Checks if all the ships are sunked
            # if one of the players have all the ships sunked, loses
        # Checks what turn is it
            # Chose a new position to attack
                # Checks if the other player has any ships in that position
                    # if a ship is hitted, the ship's segment is destroyed
                        # if all segments are destroyed, shunk ship
        # Change turns
        pass
