def analyze_pattern(sequence):
    count = 0
    trend = []
    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i-1]:
            trend.append(1)
        elif sequence[i] < sequence[i-1]:
            trend.append(-1)
        else:
            trend.append(0)
    
    # Distractor: Analyze trend reversals (not used later)
    reversals = 0
    for j in range(1, len(trend)):
        if trend[j] != trend[j-1] and trend[j-1] != 0:
            reversals += 1

    # Actual relevant logic: sum of positive movements
    upward_force = sum(1 for x in trend if x == 1)
    return upward_force


def extract_features(raw):
    # Convert string input to numeric sequence
    cleaned = ''.join([c for c in raw if c.isdigit() or c in ','])
    values = [int(x) for x in cleaned.split(',') if x]
    
    # Distractor: normalization (unused)
    max_val = max(values) if values else 1
    normalized = [round(v / max_val, 3) for v in values] if max_val > 0 else [0]*len(values)
    
    # Relevant: get magnitude sum
    total_magnitude = sum(values)
    return values, total_magnitude

def compute_weighted_index(base, factor=1.5):
    index_vals = []
    for i, val in enumerate(base):
        weight = (i + 1) * factor  # increasing weight over time
        index_vals.append(val * weight)
    
    # Distractor: peak detection
    peaks = []
    for i in range(1, len(index_vals)-1):
        if index_vals[i-1] < index_vals[i] > index_vals[i+1]:
            peaks.append(i)
    
    # Return only the sum (peaks unused)
    return sum(index_vals)

def process_metrics(data_str, weight_map):
    # Step 1: Extract numeric data
    seq_list, magnitude_sum = extract_features(data_str)
    
    # Step 2: Analyze pattern directionality
    directional_strength = analyze_pattern(seq_list)
    
    # Step 3: Compute weighted index using base values
    raw_index = compute_weighted_index(seq_list)
    
    # Step 4: Apply modular adjustment based on length
    mod_adjustment = len(seq_list) % 7 if len(seq_list) > 0 else 0
    adjusted_index = raw_index % (directional_strength + 5) if directional_strength + 5 != 0 else 0
    
    # Step 5: Combine components with weight_map influence
    w1 = weight_map.get('base', 1)
    w2 = weight_map.get('trend', 2)
    w3 = weight_map.get('mod', 0.5)
    
    # Intermediate distractor calculation (dead-end)
    hypothetical = (magnitude_sum * w1 * 0.8) + (len(seq_list) ** 1.5)
    temp_offset = abs(hypothetical - adjusted_index) // 10
    
    # Final score computation (key path)
    trend_contribution = directional_strength * w2
    base_contribution = magnitude_sum * w1
    mod_contribution = mod_adjustment * w3
    final_score = int(base_contribution + trend_contribution + mod_contribution - temp_offset)
    
    # Print result as required
    print(f"Result: {final_score}")
    return final_score

# Input data with embedded digits and noise
sensor_data = "ax3m9p2l8v1q5r7s4t6x"
weights = {'base': 2, 'trend': 3, 'mod': 1.2}

# Execute main function
final_score = process_metrics(sensor_data, weights)