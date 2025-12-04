# Function to find valid moves in a tic-tac-toe variant game
# Players can only place pieces adjacent to their existing pieces
# 0 represents empty cell, 1 for player one, 2 for player two

board = [0, 1, 0, 2, 0, 1, 0, 0, 0]  # 3x3 board representation
player = 1  # Current player

# Define adjacent positions for each cell in the 3x3 board
adjacent_positions = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7]
}

# Count cells with specific properties
empty_cells = sum(1 for cell in board if cell == 0)
player_cells = len([cell for cell in board if cell == player])
opponent_cells = len([cell for cell in board if cell != 0 and cell != player])

# Find valid moves - empty cells adjacent to current player's pieces
valid_moves = len([pos for pos, piece in enumerate(board) if piece == 0 and any(board[i] == player for i in adjacent_positions[pos])])

print(f"Empty cells: {empty_cells}")
print(f"Player {player} cells: {player_cells}")
print(f"Valid moves: {valid_moves}")
