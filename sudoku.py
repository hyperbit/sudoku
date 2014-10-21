#!/usr/bin/python

# Copyright 2014 Justin Cano
#
# This is a simple Python program of the game Sudoku
# (http://www.sudoku.name/rules/en), developed for
# a coding challenge from the Insight Data Engineering
# Fellows Program application for the January 2015
# session.
#
# Licensed under the GNU General Public License, version 2.0
# (the "License"), this program is free software; you can
# redistribute it and/or modify it under the terms of the
# License.
#
# You should have received a copy of the License along with this
# program in the file "LICENSE". If not, you may obtain a copy of
# the License at
#	http://www.gnu.org/licenses/gpl-2.0.html
#
import csv

filename = 'bad_input.csv'#'sample_input.csv'

def loadBoard(filename):
    '''
    Loads the game board with the values contained
    in the csv file designated by filename
    Params: filename - the filename of the corresponding
            csv file to be read
    Return: board - a game board loaded with the elements
            from the csv file
    '''
    board = []
    try:
        with open(filename) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                board.append(map(int, row))
    except ValueError:
        print "ValueError: invalid literal for int()"
        print "Make sure csv file is comma separated and contains only integers between 0-9!"
    except IOError:
        print "IOError: no such file '%s'" % filename

    return board

def validateBoard(board):
    '''
    Checks for validity of the game board loaded from the input
    csv file. Game board must be a 9x9 element array with each
    element value between 0-9
    Params: board - the game board to be validated
    Return: True if board is valid (9x9 with elements between 0-9)
            False if board is invalid
    '''
    if board == None:
        return False
    if len(board) != 9:
        return False
    for i in range(9):
        if len(board[i]) != 9:
            return False
        for j in range(9):
            if board[i][j] < 0 or board[i][j] > 9:
                return False


    return True


def printBoard(board):
    '''
    Prints the contents of the game board in a human readable
    format
    Params: board - the game board to be printed
    '''
    print '_' * (len(board)-1) * 3
    for i in range(len(board)):
        print '|',
        for j in range(len(board)):
            print board[i][j],
            if (j+1) % 3 == 0:
                print '|',
        print
        if (i+1) % 3 == 0:
            print '_' * (len(board)-1) * 3


def main():
    board = []
    while not validateBoard(board):
        filename = raw_input('Enter csv file to load: ')
        board = loadBoard(filename)
        printBoard(board)





if __name__ == "__main__":
    main()
