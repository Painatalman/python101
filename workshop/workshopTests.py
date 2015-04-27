#!/usr/bin/python
# -*- coding: utf-8 -*-
from workshopPlayer import *
from workshopShips import *
from workshopPoint import *
from workshopPlayer import *
from workshopGame import *

def testsShip():
    print "Ship\n-----"
    ships = Ship()
    ships.addShip("Aircraft")
    print ships.showsAllShips()
    ships.addSegment(0, "Aircraft", 1, 1, 5, 1)
    print "Number of Ships: " + str(ships.getNumberOfShips())
    print "parts:"
    for x in range(0, 4):
        print ships.getSegmentPositionX(0, x)
        print ships.getSegmentPositionY(0, x)
    ships.addSegment(0, "Aircraft", 1, 1, 5, 1)
    print ships.showsAllShips()
    print "\n"


def testsPoint():
    print "Point\n-----"
    point = Point()
    point.setX(1)
    print point.getX()
    point.setY(2)
    print point.getY()
    print "\n"


def testsPlayer():
    print "Player\n-----"
    player1 = Player("João")
    print player1.getName()
    print player1.getVictories()
    print "Turn:\t" + str(player1.getTurn())
    player1.setTurn()
    print "Turn:\t" + str(player1.getTurn())
    player1.setTurn()
    print "Turn:\t" + str(player1.getTurn())
    player1.addVictory()
    player1.setName("Joana")
    print player1.getName()
    print player1.getVictories()
    print player1.getShips().getNumberOfShips()
    player1.getShips().addShip("Aircraft")
    print player1.getShips().getNumberOfShips()
    print "\n"

testsPlayer()
