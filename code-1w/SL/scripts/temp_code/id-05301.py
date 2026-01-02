def analyze_trend(sequence):
    trend_value = 0
    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i-1]:
            trend_value += 1
        elif sequence[i] < sequence[i-1]:
            trend_value -= 1
    return trend_value

# Simulate sensor data buffer
data_stream = [23.1, 24.5, 24.3, 25.8, 26.1, 25.9, 27.2, 28.0, 27.8, 28.3]

# Irrelevant processing: normalize values (not used later)
normalized_data = [round((x - min(data_stream)) / (max(data_stream) - min(data_stream)), 3) for x in data_stream]

# Extract recent activity window using slicing
data_window = data_stream[3:8]  # Focus on central segment

# Auxiliary calculation: volatility (distractor)
volatility = sum(abs(data_stream[i] - data_stream[i-1]) for i in range(1, len(data_stream)))

# Bitwise flag setup for mode selection (semi-relevant)
processing_mode = 0b101
flag_a = processing_mode & 0b001
flag_b = processing_mode & 0b010
flag_c = processing_mode & 0b100

# Dictionary-based weight map (used in final score)
weight_map = {
    'low': 0.8,
    'medium': 1.2,
    'high': 1.5
}

# Helper function with multiple concepts
def calculate_final_score(segment):
    base_trend = analyze_trend(segment)
    
    # Destructuring assignment
    first, *middle, last = segment
    
    # Compute statistical properties
    avg_val = sum(segment) / len(segment)
    peak = max(segment)
    
    # Determine category (uses dictionary lookup)
    if avg_val < 25.0:
        level = 'low'
    elif avg_val < 27.0:
        level = 'medium'
    else:
        level = 'high'
    
    # Apply weight based on level
    weighted_trend = base_trend * weight_map[level]
    
    # Additional adjustment using bitwise logic
    adjustment = (len(middle) << 1) ^ 2  # Left shift and XOR
    
    # Final computation
    score = weighted_trend + adjustment
    
    # Dead code path (distractor)
    if False:
        score *= 1.1
    
    return int(score)

# Execute main logic
final_score = calculate_final_score(data_window)

# Print result as required
print(f"Result: {final_score}")