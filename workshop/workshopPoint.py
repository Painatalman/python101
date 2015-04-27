#!/usr/bin/python
# -*- coding: utf-8 -*-


class Point(object):

    def __init__(self):
        self.__x = 0
        self.__y = 0

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y
