from collections import Counter

def process_robot_commands():
    # Simulated command file content
    commands = [15, -10, 15, 25, -10, 15, 30, 25, -10, 15]
    
    # Track robot's position using modular arithmetic
    current_position = 0
    
    # Count frequency of each command
    command_frequency = Counter(commands)
    
    # Process each command
    for cmd in commands:
        current_position = (current_position + cmd) % 360
        if current_position < 0:
            current_position += 360
    
    # Calculate final move based on most frequent command
    most_frequent_cmd = command_frequency.most_common(1)[0][0]
    total_displacement = sum(commands) % 360
    
    # Final move calculation
    final_move = (most_frequent_cmd * (total_displacement // 90)) % 360
    
    # Apply final move
    final_position = (current_position + final_move) % 360
    
    return final_position

# Execute the robot command processing
final_segment = process_robot_commands()
print(f"Result: {final_segment}")