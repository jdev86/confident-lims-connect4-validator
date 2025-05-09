def valid_piece_placement(board):
    for col in range(len(board[0])):
        empty_found = False
        for row in range(len(board)):
            if board[row][col] == 0:
                empty_found = True
            elif empty_found and board[row][col] != 0:
                return False, f"Invalid piece at ({row}, {col}): placed on top of an empty slot"
    return True, ""