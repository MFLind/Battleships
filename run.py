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
        self.isHit = False
        self.isEmpty = False

    def getVal(self):
        if (self.isHit):
            return ('@')
        else:
            return ('X')

class Boom(BoardCell):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.isHit = True
        self.isEmpty = False

    def getVal(self):
        return ('b')

class Board():
    def __init__(self, name):
        self.board = []
        self.name = name
        self.shipCount = 0
        self.isComputer = False

        for y in range(BOARD_MAX_Y):
            for x in range(BOARD_MAX_X):
                self.board.append(BoardCell(x, y))

        if (name == "Computer"):
            self.isComputer = True
            # Random Board for computer
            ss = random.sample(range(0, ((BOARD_MAX_X*BOARD_MAX_Y)-1)), MAX_SHIPS)
            for i in range(MAX_SHIPS):
                x = ss[i] % BOARD_MAX_Y
                y = ss[i] // BOARD_MAX_Y
                self.board[ss[i]] = Ship(x, y)
                self.shipCount += 1

    def addShip(self, x, y):
        i = x + (y * BOARD_MAX_Y)
        if (self.board[i].isEmpty):
            self.board[i] = Ship(x, y)
            self.shipCount += 1
            return (True)
        return (False)

    def getPos(self, x, y):
        return (self.board[y * BOARD_MAX_X + x].getVal())

    def show(self):
        print("  0 1 2 3 4 5 6 7")
        for y in range(BOARD_MAX_Y):
            line = str(y) + " "
            for x in range(BOARD_MAX_X):
                val = self.getPos(x, y)
                if (self.isComputer and val == 'X'):
                    val = '.'
                line += val + " "
            print(line)
class Game():
    def __init__(self):
        name = input("Enter your name: ")
        self.playerBoard = Board(name)
        self.computerBoard = Board('Computer')

    def show(self):
        print(f"{self.playerBoard.name} Board:")
        self.playerBoard.show()
        print(f"{self.computerBoard.name} Board:")
        self.computerBoard.show()

    def playerShipPlacement(self):
        i = 0
        while(True):
            print("Please place your ships: ")
            self.playerBoard.show()
            print(f"Ship {i+1} of {MAX_SHIPS}")
            try:
                x = int(input("X = "))
                if (x >= BOARD_MAX_X or x < 0):
                    print("Out of range value")
                    continue
                y = int(input("Y = "))
                if (y >= BOARD_MAX_Y or y < 0):
                    print("Out of range value")
                    continue
            except ValueError:
                print("Incorrect value should be a number")
                continue
            ret = self.playerBoard.addShip(x, y)
            if (not ret):
                print("Ship already there")
                continue
            i += 1
            if (i >= MAX_SHIPS):
                break

def main():

    print("=================================")
    print("- = *       Battleship      * = -")
    print("=================================")

    myGame = Game()
    myGame.playerShipPlacement()


if __name__ == "__main__":
    main()
