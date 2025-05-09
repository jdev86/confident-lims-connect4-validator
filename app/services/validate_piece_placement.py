def valid_piece_placement(board):
    # Validate that no 1 or 2 is placed above a 0 in the board
    for row in range(len(board) - 1):  # Exclude the last row, because it has no piece below it
        for col in range(len(board[row])):
            if board[row][col] != 0 and board[row + 1][col] == 0:
                return False, "Invalid piece placement. Blue or Red should not exist on top of an empty space."  # Invalid placement
    return True