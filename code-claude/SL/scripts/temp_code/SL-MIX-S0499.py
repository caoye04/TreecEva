def calculate_final_treasure(treasure_map, path):
    current_position = (0, 0)
    total_value = 0
    collected_gems = {}
    
    # Initialize gem collection tracking
    for gem_type in ['ruby', 'emerald', 'sapphire']:
        collected_gems[gem_type] = 0
    
    # Track visited locations to avoid double-counting
    visited = set([current_position])
    
    # Process each move in the path
    for direction in path:
        # Calculate new position
        if direction == 'N':
            current_position = (current_position[0], current_position[1] + 1)
        elif direction == 'S':
            current_position = (current_position[0], current_position[1] - 1)
        elif direction == 'E':
            current_position = (current_position[0] + 1, current_position[1])
        elif direction == 'W':
            current_position = (current_position[0] - 1, current_position[1])
        
        # Skip if we've been here before
        if current_position in visited:
            continue
        
        visited.add(current_position)
        
        # Check if there's treasure at this position
        if current_position in treasure_map:
            gem_type, value = treasure_map[current_position]
            collected_gems[gem_type] += 1
            total_value += value
    
    # Apply special combination rules
    combination_bonus = 0
    if collected_gems['ruby'] > 0 and collected_gems['emerald'] > 0 and collected_gems['sapphire'] > 0:
        # XOR the counts for a special bonus
        combination_bonus = collected_gems['ruby'] ^ collected_gems['emerald'] ^ collected_gems['sapphire']
    
    # Calculate weather impact (irrelevant to final result)
    weather_conditions = ['sunny', 'rainy', 'foggy']
    weather_index = (len(path) % 3)
    weather = weather_conditions[weather_index]
    
    # Apply gem type multipliers
    ruby_multiplier = 3
    emerald_multiplier = 5
    sapphire_multiplier = 2
    
    # Final calculation includes combination bonus and gem values
    final_value = total_value + combination_bonus
    
    # Additional calculations that don't affect the result
    potential_max = sum([ruby_multiplier * collected_gems['ruby'],
                        emerald_multiplier * collected_gems['emerald'],
                        sapphire_multiplier * collected_gems['sapphire']])
    efficiency_ratio = (total_value / potential_max) if potential_max > 0 else 0
    
    return final_value

# Define the treasure map: position -> (gem_type, value)
temporal_anomaly = {'past': -5, 'present': 0, 'future': 5}  # Unused distraction
treasure_map = {
    (1, 0): ('ruby', 10),
    (2, 1): ('emerald', 15),
    (0, 2): ('sapphire', 12),
    (3, 1): ('ruby', 8),
    (2, 2): ('emerald', 20),
    (1, 3): ('sapphire', 6),
    (3, 3): ('ruby', 14)
}

# Define the chosen path
all_possible_paths = {
    'A': 'NEESSWNE',
    'B': 'EENWNESE',
    'C': 'NNEESEEN'
}
chosen_path = all_possible_paths['B']

# Calculate the treasure value
treasure_value = calculate_final_treasure(treasure_map, chosen_path)

# Some additional calculations (distractors)
path_length = len(chosen_path)
path_complexity = sum(ord(c) - ord('A') for c in chosen_path) & 0x3F
distraction_factor = (path_length * path_complexity) % 100

print(f"Result: {treasure_value}")