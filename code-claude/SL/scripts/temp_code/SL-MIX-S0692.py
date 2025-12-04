def calculate_position(inventory, moves):
    # Initialize coordinates
    x, y = 0, 0
    direction = 0  # 0: North, 1: East, 2: South, 3: West
    
    # Process special items in inventory
    compass_bonus = 0
    if 'compass' in inventory:
        compass_value = inventory['compass']
        if compass_value > 0:
            compass_bonus = min(compass_value, 2)
    
    # Terrain difficulty factors
    terrain_factors = {
        'forest': 0.8,
        'mountain': 0.5,
        'plains': 1.2,
        'desert': 1.0
    }
    
    # Default terrain if not specified
    current_terrain = 'plains'
    
    # Weather condition (not directly used)
    weather_penalty = 0
    if 'rainy' in inventory.get('weather', []):
        weather_penalty = 1
    
    # Process movement instructions
    for move in moves:
        command = move[0]
        value = move[1]
        
        if command == 'forward':
            # Apply terrain factor to movement
            terrain_factor = terrain_factors.get(current_terrain, 1.0)
            effective_value = int(value * terrain_factor)
            
            if direction == 0:  # North
                y += effective_value
            elif direction == 1:  # East
                x += effective_value
            elif direction == 2:  # South
                y -= effective_value
            else:  # West
                x -= effective_value
                
        elif command == 'turn':
            # Change direction (0-3)
            direction = (direction + value) % 4
            
        elif command == 'terrain':
            # Update current terrain
            current_terrain = value
    
    # Apply compass bonus to final position calculation
    position_value = abs(x) + abs(y) + compass_bonus
    
    # Calculate checksum (not used in final result)
    checksum = (x * y) % 100
    
    return position_value

# Inventory with items and their values
inventory = {
    'compass': 3,
    'map': 1,
    'food': 5,
    'weather': ['sunny', 'clear']
}

# List of movement commands: (command, value)
moves = [
    ('forward', 5),
    ('turn', 1),
    ('forward', 3),
    ('terrain', 'forest'),
    ('forward', 5),
    ('turn', 2),
    ('forward', 2)
]

# Calculate final position
target_position = calculate_position(inventory, moves)
print(f"Result: {target_position}")