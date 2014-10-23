import sudoku

board = []
board.append([0,3,5,2,9,0,8,6,4])
board.append([0,8,2,4,1,0,7,0,3])
board.append([7,6,4,3,8,0,0,9,0])
board.append([2,1,8,7,3,9,0,4,0])
board.append([0,0,0,8,0,4,2,3,0])
board.append([0,4,3,0,5,2,9,7,0])
board.append([4,0,6,5,7,1,0,0,9])
board.append([3,5,9,0,2,8,4,1,7])
board.append([8,0,0,9,0,0,5,2,6])

sudoku.printBoard(board)

def test():
    row = sudoku.boardRow(board, 0)
    assert [0,3,5,2,9,0,8,6,4] == row
    print "boardRow PASSED"

    col = sudoku.boardCol(board, 0)
    assert [0,0,7,2,0,0,4,3,8] == col
    print "boardCol PASSED"

    region = sudoku.boardRegion(board, 0, 0)
    assert [0,3,5,0,8,2,7,6,4] == region
    region = sudoku.boardRegion(board, 1, 2)
    assert [0,3,5,0,8,2,7,6,4] == region
    region = sudoku.boardRegion(board, 3, 3)
    assert [7,3,9,8,0,4,0,5,2] == region
    region = sudoku.boardRegion(board, 8, 6)
    assert [0,0,9,4,1,7,5,2,6] == region
    print "boardRegion PASSED"

    assert sudoku.isSafeToAssign(board, 0, 0, 1) == True
    assert sudoku.isSafeToAssign(board, 1, 0, 7) == False
    print "isSafeToAssign PASSED"

    assert sudoku.findNextUnassignedBlock(board) == (0, 0)
    board[0][0] = 1
    assert sudoku.findNextUnassignedBlock(board) == (0, 5)
    print "findNextUnassignedBlock PASSED"




if __name__ == "__main__":
    test()
