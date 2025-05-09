def check_winner(board, player):
    # Check if the player has four consecutive pieces (horizontal, vertical, diagonal)
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == player:
                # Check horizontal
                if col + 3 < len(board[0]) and all(board[row][col + i] == player for i in range(4)):
                    return True, [(row, col + i) for i in range(4)]
                # Check vertical
                if row + 3 < len(board) and all(board[row + i][col] == player for i in range(4)):
                    return True, [(row + i, col) for i in range(4)]
                # Check diagonal (top-left to bottom-right)
                if row + 3 < len(board) and col + 3 < len(board[0]) and all(board[row + i][col + i] == player for i in range(4)):
                    return True, [(row + i, col + i) for i in range(4)]
                # Check diagonal (bottom-left to top-right)
                if row - 3 >= 0 and col + 3 < len(board[0]) and all(board[row - i][col + i] == player for i in range(4)):
                    return True, [(row - i, col + i) for i in range(4)]
    return False, []