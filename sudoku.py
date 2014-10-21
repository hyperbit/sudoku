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

file = 'sample_input.csv'

board = []

with open(file, 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        board.append(row)

for i in range(len(board)):
    for j in range(len(board)):
        print board[i][j],
    print
