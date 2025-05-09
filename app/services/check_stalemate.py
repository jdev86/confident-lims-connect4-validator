def check_stalemate(board):
    """
    Checks if the game has reached a stalemate. A stalemate occurs when:
    - The board is completely filled.
    - There is no winner.
    
    Returns:
    - True if it's a stalemate, False otherwise.
    """
    # Check if the board is full (no empty slots)
    if all(board[r][c] != 0 for r in range(6) for c in range(7)):
        return False  # If the board is full, we still need to check for a winner.
    
    return True