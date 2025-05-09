def is_full(board):
    # Check if the board is full (no empty spaces)
    return all(cell != 0 for row in board for cell in row)