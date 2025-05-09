def get_turn(board):
    """
    Determines whose turn it is based on the current board state.
    - If Blue's count is less than or equal to Red's count, it's Blue's turn.
    - Otherwise, it's Red's turn.
    """
    blue_count = sum(row.count(1) for row in board)
    red_count = sum(row.count(2) for row in board)
    if blue_count <= red_count:
        return "blue"
    return "red"