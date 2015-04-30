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
        self.__options = {
            "gridSizeX": 10,
            "gridSizeY": 10,
            "numberOfPlayers": 2,
        }

    def getPlayer(self, numberOfPlayer):
        if len(self.__player) > 0:
            return self.__player[numberOfPlayer-1]
        else:
            return False

    # Returns who is the player to play
    def getPlayerToPlay(self):
        if self.getPlayer(1).getTurn():
            return 1
        else:
            return 2

    # Returns who is the player to Attack
    def getPlayerToAttack(self):
        if self.getPlayer(1).getTurn():
            return 2
        else:
            return 1

    # Determinates who is the first player
    def coinToss(self):
        if(random() > 0.5):
            return 2
        else:
            return 1

    # Change player to play
    def setNewTurn(self):
        self.getPlayer(1).setTurn()
        self.getPlayer(2).setTurn()

    # Checks if x and y are valid
    def validadesCoordinates(self, x, y):
        # Checks if position is valid
        if(int(x) < 10 and int(x) >= 0 and int(y) < 10 and int(y) >= 0):
            return True
        else:
            return False

    # Set a new ship on the board
    def setShip(self, x, y, playerNumber):
        # Verifies if x and y are in the board
        if self.validadesCoordinates(x, y):
            # Verifies if there is a ship in the x and x position
            if self.getPlayer(playerNumber).getMainBoard()[x][y] == 1:
                print "Invalid position: There is a ship in that position"
                return False
            else:
                print "Ship inserted at position: (" + str(x) + ", " + str(y) + ")"
                self.getPlayer(playerNumber).getMainBoard()[x][y] = 1
                return True
        else:
            print "Invalid position: Out of bounds"
            return False

    # Set initial ships
    def setStartShips(self):
        for i in range(0, 5):

            while True:
                print "Insert the coordinates of ship " + str(i+1)
                print "X: ",
                x = int(raw_input())
                print "Y: ",
                y = int(raw_input())
                if self.setShip(x, y, self.getPlayerToPlay()):
                    break
    '''
    # Fires to the other player's board and register the current player action
    def mainboardFire(self, x, y):
        # Check who is the player to fire
        if getPlayer(1).getTurn():
            getPlayer(1).SetFireBoard(x, y, 1)
            getPlayer(2).SetMainBoard(x, y, 0)
        else:
            getPlayer(2).SetFireBoard(x, y, 1)
            getPlayer(1).SetMainBoard(x, y, 0)
    '''
    # Checks if all of player's ships are sunked
    def mainboardCheck(self, playerNumber):
        gameOver = True
        for row in self.getPlayer(playerNumber).getMainBoard():
            for col in row:
                if col != 0:
                    gameOver = False
        return gameOver

    # Show fire board
    def fireBoardShow(self, playerNumber):
        rowNumber = 0
        print "Board:\n  |",
        # Column Numbers
        for i in range(0, 10):
            print i,
        print "|"
        # Line Top
        print "-" * 25,
        print
        for row in self.getPlayer(playerNumber).getFireBoard():
            # Row Numbers
            print str(rowNumber) + " |",
            # Print Board
            for col in row:
                print col,
            print "|"
            rowNumber += 1

    # Show main board
    def mainBoardShow(self, playerNumber):
        rowNumber = 0
        print "Board:\n  |",
        # Column Numbers
        for i in range(0, 10):
            print i,
        print "|"
        # Line Top
        print "-" * 25,
        print
        for row in self.getPlayer(playerNumber).getMainBoard():
            # Row Numbers
            print str(rowNumber) + " |",
            # Print Board
            for col in row:
                print col,
            print "|"
            rowNumber += 1

    # Adds a new player
    def addPlayer(self):
        print "Insert Player Name: ",
        player = Player(raw_input())
        self.__player.append(player)
        print "Added Player " + player.getName()

    # Runs the game
    def start(self):
        # Greeting
        print "Welcome to " + self.__name
        # Add Players
        self.addPlayer()
        self.addPlayer()
        # Determinates who is the first Player
        toss = self.coinToss()
        self.getPlayer(toss).setTurn()
        print self.getPlayer(self.getPlayerToPlay()).getName() + " starts"
        # First player fills the board
        self.mainBoardShow(self.getPlayerToPlay())
        self.setStartShips()
        self.setNewTurn()
        # Second player fills the board
        print self.getPlayer(self.getPlayerToPlay()).getName() + " starts"
        self.mainBoardShow(self.getPlayerToPlay())
        self.setStartShips()
        # Start Game
        self.setNewTurn()
        self.mainLoop()

    # Main loop of the game
    def mainLoop(self):
        while True:
            # Checks if all the ships are sunked
            if self.mainboardCheck(self.getPlayerToPlay()):
                # if the current player have all the ships sunked, loses
                print "Game Over: Player " + str(self.getPlayerToAttack()) + " wins!"
                break
            else:
                # Input Command
                print "Player " + self.getPlayer(self.getPlayerToPlay()).getName() + " Turn! Chose what to do:"
                print "1: Show Ship Board"
                print "2: Show Fire Board"
                print "3: Shoot a Ship!"
                command = raw_input()

                if int(command) == 1:
                    print "Option 1 selected"
                    self.mainBoardShow(self.getPlayerToPlay())
                elif int(command) == 2:
                    print "Option 2 selected"
                    self.fireBoardShow(self.getPlayerToPlay())
                elif int(command) == 3:
                    "Fire to other player board!\nInsert coordinates:"
                    print "X: ",
                    x = int(raw_input())
                    print "Y: ",
                    y = int(raw_input())
                    # TODO - IMPROVE CODE HERE TO A METHOD
                    # Set Player's Fire Board
                    self.getPlayer(self.getPlayerToPlay()).SetFireBoard(x, y, 1)
                    # Set Other Player's Main Board
                    self.getPlayer(self.getPlayerToAttack()).SetMainBoard(x, y, 0)
                    print "Shoot player " + self.getPlayer(self.getPlayerToAttack()).getName() + " at position (" + str(x) + ", " + str(y) + ")"
                    # Change turns
                    self.setNewTurn()
                else:
                    print "Invalid command: Insert a valid number (1, 2 or 3)"

            # Chose a new position to attack
                # Checks if the other player has any ships in that position
                    # if a ship is hitted, the ship's segment is destroyed
                        # if all segments are destroyed, shunk ship
        # Change turns
