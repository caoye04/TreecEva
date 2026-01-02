def analyze_trends(sequence):
    trend_data = []
    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i-1]:
            trend_data.append(1)
        elif sequence[i] < sequence[i-1]:
            trend_data.append(-1)
        else:
            trend_data.append(0)
    return trend_data

# Extraneous helper function with misleading relevance
def calculate_variance(values):
    mean_val = sum(values) / len(values)
    squared_diffs = [(v - mean_val) ** 2 for v in values]
    return sum(squared_diffs) / len(squared_diffs)

# Distractor: unused data structure
temp_log = {
    'process_id': 'TMR-789',
    'status': 'completed',
    'iterations': 0
}

def evaluate_performance(raw_data, limits):
    # Slice to focus on recent observations
    recent_data = raw_data[-7:]
    
    # Bitwise masking to simulate filtering (only some bits matter)
    masked_values = [x & 0b1111 for x in recent_data]  # Keep only last 4 bits
    
    # Tracking state across iterations
    count_up = 0
    count_down = 0
    flat_count = 0
    
    trends = analyze_trends(masked_values)
    
    for direction in trends:
        if direction == 1:
            count_up += 1
        elif direction == -1:
            count_down += 1
        else:
            flat_count += 1
    
    # Irrelevant intermediate calculation (distractor)
    avg_direction = (count_up - count_down) / len(trends) if trends else 0
    
    # Core logic: performance score based on upward trends and thresholds
    base_score = count_up * 13
    penalty = 0
    
    # Multiple threshold checks (modular arithmetic used here)
    for val in masked_values:
        if val % limits[0] == 0:
            penalty += 2
        if val % limits[1] == 0 and val > 5:
            penalty += 1

    # Secondary distractor: unused aggregation
    total_fluctuation = sum(abs(recent_data[i] - recent_data[i-1]) for i in range(1, len(recent_data)))
    
    # Final computation chain
    adjusted_score = base_score - penalty
    bonus = 7 if count_up >= 4 else 0
    final_score = adjusted_score + bonus
    
    # Dead code path (never executed due to logic above)
    if flat_count > 100:
        final_score *= 2
        
    return final_score

# Input data with domain-specific meaning (sensor readings)
sensor_readings = [23, 45, 12, 8, 16, 15, 18, 21, 7, 14]
threshold_config = [3, 7]

# Key execution point
final_score = evaluate_performance(sensor_readings, threshold_config)

print(f"Result: {final_score}")