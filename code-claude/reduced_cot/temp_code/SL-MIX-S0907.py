def calculate_chess_moves(moves_list, board_size=8):
    # Initialize tracking variables
    start_position = 64
    current_position = start_position
    valid_moves = []
    invalid_count = 0
    
    # Dictionary for special positions and their effects
    positions_map = {
        17: 42,
        23: 8,
        42: 15,
        56: 8,
        64: 1,
        37: 99,  # Trap position
        99: 0    # Out of bounds
    }
    
    # Track visited positions for cycle detection
    visited = {}
    move_history = []
    
    # Process movement calculations
    for idx, move in enumerate(moves_list):
        # Apply various transformations based on move type
        transformed_move = (move * 2) % board_size
        
        # Calculate potential next position
        potential_position = current_position
        
        # Apply different movement rules based on move value
        if move % 3 == 0:
            potential_position = (current_position + transformed_move) % (board_size * board_size)
        elif move % 3 == 1:
            potential_position = (current_position - transformed_move) % (board_size * board_size)
        else:
            potential_position = (current_position ^ transformed_move) % (board_size * board_size)
            
        # Check if potential position is valid
        if 0 <= potential_position < board_size * board_size:
            # Track position for cycle detection
            position_key = (potential_position, move % 3)
            
            # Check for cycles in movement pattern
            if position_key in visited and len(valid_moves) > 3:
                # Extract cycle and process it
                cycle_start = visited[position_key]
                cycle_length = len(valid_moves) - cycle_start
                
                # This branch is actually never executed due to the break below
                if cycle_length > 0:
                    remaining = (len(moves_list) - idx) % cycle_length
                    current_position = valid_moves[cycle_start + remaining - 1]
                    break
            
            # Update tracking information
            visited[position_key] = len(valid_moves)
            current_position = potential_position
            valid_moves.append(current_position)
            move_history.append(move)
        else:
            invalid_count += 1
            # This branch actually has no effect on the final result
            if invalid_count > len(moves_list) // 2:
                current_position = start_position
    
    # Process results using bitwise operations
    result_sum = sum(valid_moves)
    result_xor = 0
    for val in valid_moves:
        result_xor ^= val
    
    # Create a dictionary of move frequencies - unused but distracting
    move_freq = {}
    for m in move_history:
        if m in move_freq:
            move_freq[m] += 1
        else:
            move_freq[m] = 1
    
    # Calculate average move - unused
    avg_move = sum(move_history) / len(move_history) if move_history else 0
    
    # Find the position with the highest frequency - unused
    position_freq = {}
    for pos in valid_moves:
        position_freq[pos] = position_freq.get(pos, 0) + 1
    
    max_freq = 0
    max_pos = 0
    for pos, freq in position_freq.items():
        if freq > max_freq:
            max_freq = freq
            max_pos = pos
    
    # Slice operations to extract pattern information
    pattern = valid_moves[-5:] if len(valid_moves) >= 5 else valid_moves
    pattern_sum = sum(pattern)
    
    # Final position calculation - this is what we're looking for
    final_position = positions_map.get(valid_moves[-1], start_position)
    
    print(f"Result: {final_position}")
    return final_position

# Test with specific moves
moves = [5, 2, 7, 1, 3, 8, 4]
calculate_chess_moves(moves)