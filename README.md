sudoku
======

This is a simple text-based Sudoku (http://www.sudoku.name/rules/en) solver, written in Python. This project was developed for the Insight Data Engineering Fellows Program application for the January 2015 session.

# Usage
This Sudoku solver takes in a Sudoku board in CSV format as its input: the CSV file should be a 9x9 comma separated integer grid, with each integer between 0-9 (0 represents blanks), e.g.,

sample_input.csv:
```
0,3,5,2,9,0,8,6,4
0,8,2,4,1,0,7,0,3
7,6,4,3,8,0,0,9,0
2,1,8,7,3,9,0,4,0
0,0,0,8,0,4,2,3,0
0,4,3,0,5,2,9,7,0
4,0,6,5,7,1,0,0,9
3,5,9,0,2,8,4,1,7
8,0,0,9,0,0,5,2,6
```

```
$ python sudoku.py
Enter csv file to load: sample_input.csv
________________________
| 0 3 5 | 2 9 0 | 8 6 4 |
| 0 8 2 | 4 1 0 | 7 0 3 |
| 7 6 4 | 3 8 0 | 0 9 0 |
________________________
| 2 1 8 | 7 3 9 | 0 4 0 |
| 0 0 0 | 8 0 4 | 2 3 0 |
| 0 4 3 | 0 5 2 | 9 7 0 |
________________________
| 4 0 6 | 5 7 1 | 0 0 9 |
| 3 5 9 | 0 2 8 | 4 1 7 |
| 8 0 0 | 9 0 0 | 5 2 6 |
________________________

Sudoku!
________________________
| 1 3 5 | 2 9 7 | 8 6 4 |
| 9 8 2 | 4 1 6 | 7 5 3 |
| 7 6 4 | 3 8 5 | 1 9 2 |
________________________
| 2 1 8 | 7 3 9 | 6 4 5 |
| 5 9 7 | 8 6 4 | 2 3 1 |
| 6 4 3 | 1 5 2 | 9 7 8 |
________________________
| 4 2 6 | 5 7 1 | 3 8 9 |
| 3 5 9 | 6 2 8 | 4 1 7 |
| 8 7 1 | 9 4 3 | 5 2 6 |
________________________
```

# How it works
The algorithm behind this Sudoku solver is a simple recursive backtrack strategy.

The board is loaded from the CSV file as a 2 Dimensional array. Cells that contain a '0' are cells that need to be assigned.

The solver recursively searches cells that need to be assigned and assigns them until they are all assigned. Before the cell is assigned a value, the solver first determines if that value is valid. **A value is valid if it is an integer between 0 and 9 such that the value is not already in the same row, column, or 3x3 region.**

# Output
This solver will spew up a solution to its given input as a CSV file and saves it as `solution.csv`.

# Unit Testing
The module `tests.py` contains various testing statements to assert the correctness of the different methods of the `sudoku.py` module.

Running the `tests.py` requires a couple sample inputs for testing: `sample_input.csv` and `bad_input.csv`, both of which are supplied by this repository.

# Future
I am currently working on turning this small program into its own web app. This repository will be updated when it is finished.
