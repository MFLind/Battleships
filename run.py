#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

BOARD_MAX_X = 8
BOARD_MAX_Y = 8
MAX_SHIPS = 4

FIRE_MISSED = 0
FIRE_DOUBLE = -1
FIRE_HIT = 1

class BoardCell():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.isEmpty = True

    def getVal(self):
        return ('.')

class Ship(BoardCell):
    def __init__(self, x, y):
        super().__init__(x, y)

class Boom(BoardCell):
    def __init__(self, x, y):
        super().__init__(x, y)

class Board():
    def __init__(self, name):
        self.board = []
        self.name = name

class Game():
    def __init__(self):
        name = input("Enter your name: ")
        self.playerBoard = Board(name)
        self.computerBoard = Board('Computer')

def main():

    print("=================================")
    print("- = *       Battleship      * = -")
    print("=================================")

     myGame = Game()

if __name__ == "__main__":
    main()
