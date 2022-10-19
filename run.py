#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Battleship game"""
import random

BOARD_MAX_X = 8
BOARD_MAX_Y = 8
MAX_SHIPS = 4

FIRE_MISSED = 0
FIRE_DOUBLE = -1
FIRE_HIT = 1

class BoardCell():
    """Board cell parent class"""
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.is_empty = True

    def get_val(self):
        """Get cell value"""
        return '.'

    def get_x(self):
        """Get X value"""
        return self.x_pos

    def set_x(self, x_pos):
        """Set X value"""
        self.x_pos = x_pos

    def get_y(self):
        """Get Y value"""
        return self.y_pos

    def set_y(self, y_pos):
        """Set Y value"""
        self.y_pos = y_pos

    def get_is_empty(self):
        """Get Empty value"""
        return self.is_empty

    def set_empty(self, value):
        """Set Empty value"""
        self.is_empty = value

class Ship(BoardCell):
    """Ship subclass"""
    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)
        self.is_hit = False
        self.is_empty = False

    def get_val(self):
        """Get cell value, return hit or ship symbol"""
        if self.is_hit:
            return '@'
        return 'X'

class Boom(BoardCell):
    """Boom subclass of board cell"""
    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)
        self.is_hit = True
        self.is_empty = False

    def get_val(self):
        """Get cell value, return boom symbol"""
        return 'b'

class Board():
    """Game Board plan"""
    def __init__(self, name):
        self.board = []
        self.name = name
        self.ship_count = 0
        self.is_computer = False

        # Setup board
        for y_pos in range(BOARD_MAX_Y):
            for x_pos in range(BOARD_MAX_X):
                self.board.append(BoardCell(x_pos, y_pos))

        if name == "Computer":
            self.is_computer = True
            # Random Board for computer, get array of positions
            i = random.sample(range(0, ((BOARD_MAX_X*BOARD_MAX_Y)-1)), MAX_SHIPS)
            for j in range(MAX_SHIPS):
                x_pos = i[j] % BOARD_MAX_Y
                y_pos = i[j] // BOARD_MAX_Y
                self.board[i[j]] = Ship(x_pos, y_pos)
                self.ship_count += 1

    def add_ship(self, x_pos, y_pos):
        """Add ship to game board"""
        i = x_pos + (y_pos * BOARD_MAX_Y)
        if self.board[i].is_empty:
            self.board[i] = Ship(x_pos, y_pos)
            self.ship_count += 1
            return True
        return False

    def get_pos(self, x_pos, y_pos):
        """Get Array position from x and y"""
        return self.board[y_pos * BOARD_MAX_X + x_pos].get_val()

    def fire(self, x_pos, y_pos):
        """Fire shot on board for position X and Y"""
        i = x_pos + (y_pos * BOARD_MAX_Y)
        if self.board[i].is_empty:
            self.board[i] = Boom(x_pos, y_pos)
            return FIRE_MISSED

        if self.board[i].is_hit:
            return FIRE_DOUBLE

        self.board[i].is_hit = True
        self.ship_count -= 1
        return FIRE_HIT

    def show(self):
        """Display play field"""
        print("  0 1 2 3 4 5 6 7")
        for y_pos in range(BOARD_MAX_Y):
            line = str(y_pos) + " "
            for x_pos in range(BOARD_MAX_X):
                val = self.get_pos(x_pos, y_pos)
                if (self.is_computer and val == 'X'):
                    val = '.'
                line += val + " "
            print(line)

class Game():
    """Main game class"""
    def __init__(self):
        name = input("Enter your name: \n")
        self.plyer_board = Board(name)
        self.computer_board = Board('Computer')

    def show(self):
        """Display both computer and players play field"""
        print(f"{self.plyer_board.name} Board:")
        self.plyer_board.show()
        print(f"{self.computer_board.name} Board:")
        self.computer_board.show()

    def player_ship_placement(self):
        """Player setup playfield"""
        i = 0
        while True:
            print("Please place your ships: ")
            self.plyer_board.show()
            print(f"Ship {i+1} of {MAX_SHIPS}")
            try:
                x_pos = int(input("X = \n"))
                if (x_pos >= BOARD_MAX_X or x_pos < 0):
                    print("Out of range value")
                    continue
                y_pos = int(input("Y = \n"))
                if (y_pos >= BOARD_MAX_Y or y_pos < 0):
                    print("Out of range value")
                    continue
            except ValueError:
                print("Incorrect value should be a number")
                continue
            ret = self.plyer_board.add_ship(x_pos, y_pos)
            if not ret:
                print("Ship already there")
                continue
            i += 1
            if i >= MAX_SHIPS:
                break

    def player_fire(self):
        """Player fire"""
        while True:
            print("Fire your cannon: ")
            try:
                x_pos = int(input("X = \n"))
                if (x_pos >= BOARD_MAX_X or x_pos < 0):
                    print("Out of range value")
                    continue
                y_pos = int(input("Y = \n"))
                if (y_pos >= BOARD_MAX_Y or y_pos < 0):
                    print("Out of range value")
                    continue
            except ValueError:
                print("Incorrect value should be a number")
                continue

            ret = self.computer_board.fire(x_pos, y_pos)

            if ret == FIRE_MISSED:
                print(f"{self.plyer_board.name} Missed BOOM")
                return
            if ret == FIRE_HIT:
                print(f"{self.plyer_board.name} Hit Bang")
                return
            print("Double hit.....")

    def computer_fire(self):
        """Computer fire"""
        while True:
            i = random.randint(0, ((BOARD_MAX_X*BOARD_MAX_Y)-1))
            x_pos = i % BOARD_MAX_Y
            y_pos = i // BOARD_MAX_Y
            ret = self.plyer_board.fire(x_pos, y_pos)
            if ret == FIRE_MISSED:
                print("Computer Missed BOOM")
                return
            if ret == FIRE_HIT:
                print("Computer Hit Bang")
                return
            print("Double hit.....")


def main():
    """Main function"""

    print("=================================")
    print("- = *       Battleship      * = -")
    print("=================================")

    my_game = Game()
    my_game.player_ship_placement()
    while True:
        print("------------------------------------------------")
        my_game.show()
        my_game.player_fire()
        if my_game.computer_board.ship_count <= 0:
            print("Player Wins!!!!")
            break
        my_game.computer_fire()
        if my_game.plyer_board.ship_count <= 0:
            print("Computer Wins!!!!")
            break

if __name__ == "__main__":
    main()
