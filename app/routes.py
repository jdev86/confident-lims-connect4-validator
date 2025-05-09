from flask import Blueprint, request, jsonify
from .services.check_winner import check_winner
from .services.determine_turn import get_turn
from .services.check_stalemate import check_stalemate
from .services.board_validator import validate_board
from .services.validate_piece_placement import valid_piece_placement

api_routes = Blueprint('api_routes', __name__)

@api_routes.route('/evaluate_board_state', methods=['POST'])
def evaluate_board_state():
    data = request.get_json()
    board = data.get('board', [])

    # Validate board
    valid, message = validate_board(board)
    if not valid:
        return jsonify({"error": message}), 400
    validPlacement, message = valid_piece_placement(board)
    if not validPlacement:
        return jsonify({"error": message}), 400

    # Check for winner
    blue_wins, blue_positions = check_winner(board, 1)
    red_wins, red_positions = check_winner(board, 2)

    # If both players win (which is invalid)
    if blue_wins and red_wins:
        return {
            "status": "invalid",
            "message": "Both players cannot win simultaneously."
        }

    # If there is a winner
    if blue_wins:
        return {
            "status": "blue wins",
            "winning_positions": blue_positions
        }
    elif red_wins:
        return {
            "status": "red wins",
            "winning_positions": red_positions
        }

    # Check for stalemate
    if check_stalemate(board):
        return jsonify({"result": "stalemate"})

    # Determine whose turn it is
    turn = get_turn(board)
    return jsonify({"turn": turn})