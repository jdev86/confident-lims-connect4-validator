def validate_board(board):
    # Check board size
    if len(board) != 6 or len(board[0]) != 7:
        return False, "Board must be 6 rows by 7 columns"

    # Count pieces
    blue_count = sum(row.count(1) for row in board)
    red_count = sum(row.count(2) for row in board)

    # Invalid piece count
    if blue_count > red_count + 1 or red_count > blue_count:
        return False, "Invalid piece distribution. Blue must have one more piece than Red or both must have the same number."

    # Check for invalid pieces
    for row in board:
        for piece in row:
            if piece not in [0, 1, 2]:
                return False, "Invalid piece value detected."

    return True, ""