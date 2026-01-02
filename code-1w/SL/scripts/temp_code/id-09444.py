def calculate_final_score(data, weight_map):
    base_score = 0
    char_frequency = {}
    
    # Count character frequencies in the input string
    for char in data['input_string']:
        char_frequency[char] = char_frequency.get(char, 0) + 1
    
    # Apply weights to frequency counts
    weighted_values = [char_frequency.get(c, 0) * weight_map[c] for c in weight_map]
    
    # Compute base score as sum of weighted values
    base_score = sum(weighted_values)
    
    # Bonus logic: if any character appears exactly 3 times, add a bonus
    if 3 in char_frequency.values():
        base_score += 25
    
    # Penalty: if 'x' or 'z' are in the string and have non-zero weight, subtract 10
    rare_penalty_chars = ['x', 'z']
    for ch in rare_penalty_chars:
        if ch in data['input_string'] and ch in weight_map and weight_map[ch] > 0:
            base_score -= 10
            break
    
    return base_score

# Input data
char_data = {
    'input_string': 'extraordinary'
}

# Weight map for relevant characters
weights = {
    'a': 2,
    'r': 3,
    'd': 5,
    'i': 1,
    'n': 2,
    'x': 4
}

# Compute final score
final_score = calculate_final_score(char_data, weights)

print(f"Result: {final_score}")