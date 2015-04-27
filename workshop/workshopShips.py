#!/usr/bin/python
# -*- coding: utf-8 -*-
from workshopPoint import *


class Ship(object):

    #__shipType = ""
    __shipList = []
    __shipTypeList = {
        "Aircraft": 5,
        "Battleship": 4,
        "Submarine": 3,
        "Cruiser": 3,
        "Patrol": 2,
    }

    # Adds one of the 5 types of ship
    def addShip(self, typeOfShip):
        # Checks for the max number of ships
        if (len(self.__shipList) < 5):
            # Checks if the type if ship is already in use
            sameShip = False
            for ship in self.__shipList:
                if ship["type"] == self.__shipTypeList[typeOfShip]:
                    sameShip = True
            if (sameShip == False):
                # Adds a new Ship to the Ship List
                shipToAdd = {
                    "type": typeOfShip,
                    "maxSegments": self.__shipTypeList[typeOfShip],
                    "segments": [],
                }
                self.__shipList.append(shipToAdd)
                return True
            else:
                return False
        else:
            return False

    # Adds the ship's segments
    def addSegment(self, shipIndex, shipType, startx, starty, finishx, finishy):
        # Validade new position
        if (startx == finishx or starty == finishy):
            # Determinates the fixed values
            valueStill = 0
            valueChangeInitial = 0
            valueChangeFinal = 0
            isXFix = False
            if (startx == finishx):
                valueStill = startx
                isXFix = True
                valueChangeInitial = starty
                valueChangeFinal = finishy
            else:
                valueStill = starty
                isXFix = False
                valueChangeInitial = startx
                valueChangeFinal = finishx
            # Checks if the length is correct
            if (self.__shipTypeList[shipType] != (valueChangeFinal-valueChangeInitial + 1)):
                return False
            # Checks if new position overlaps other ships
            samePosition = False
            for ship in self.__shipList:
                for segment in ship["segments"]:
                    for i in range(valueChangeInitial, valueChangeFinal):
                        if (isXFix):
                            if(segment["Position"].getY() == i and segment["Position"].getX() == valueStill):
                                samePosition = True
                        else:
                            if(segment["Position"].getX() == i and segment["Position"].getY() == valueStill):
                                samePosition = True
            # Adds the ship segments if do not overlap
            if (samePosition == False):
                for i in range(valueChangeInitial, valueChangeFinal):
                    partsToAdd = {
                        "isSunked": False,
                        "Position": Point(),
                    }
                    if (isXFix):
                        partsToAdd["Position"].setX(valueStill)
                        partsToAdd["Position"].setY(i)
                    else:
                        partsToAdd["Position"].setX(i)
                        partsToAdd["Position"].setY(valueStill)
                    (self.__shipList[shipIndex])["segments"].append(partsToAdd)

                return True
        return False

    # Get the ship part when given the ship and the part
    def getSegmentPositionX(self, shipIndex, shipPart):
        return (((self.__shipList[shipIndex])["segments"])[shipPart])["Position"].getX()

    # Get the ship part when given the ship and the part
    def getSegmentPositionY(self, shipIndex, shipPart):
        return (((self.__shipList[shipIndex])["segments"])[shipPart])["Position"].getY()

    def getNumberOfShips(self):
        return len(self.__shipList)

    def getMaxNumberOfSegments(self, indexNumber):

        if(len(self.__shipList) == 0):
            return 0
        else:
            return self.__shipList[indexNumber].getMaxNumberOfSegments()

    def showsAllShips(self):
        return self.__shipList

    def showsAllSegmentsOfAShip(self, position):
        return (self.__shipList[position])["segments"]
