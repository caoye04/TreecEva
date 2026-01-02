def analyze_performance(metrics):
    baseline = 1.0
    adjustment_factor = 0.95
    temp_result = 0
    efficiency_scores = []

    for idx, val in enumerate(metrics['readings']):
        if idx % 2 == 0:
            adjusted_val = val * adjustment_factor
            efficiency_scores.append(adjusted_val)
        else:
            # Distractor: irrelevant computation
            temp_result += val ** 0.5

    # Irrelevant list comprehension with side-effect-free operation
    squared_deltas = [round((x - baseline) ** 2, 3) for x in efficiency_scores]

    # Real logic hidden among distractions
    avg_efficiency = sum(efficiency_scores) / len(efficiency_scores)
    return avg_efficiency


def calculate_thermal_rating(log_data):
    base_rating = 150
    multiplier = 1.75
    penalty = 0

    # Misleading dictionary operations
    stats = {k: len(v) if isinstance(v, list) else v for k, v in log_data.items()}
    stats['offset'] = 5

    # Actual key calculation
    if 'avg' in log_data and log_data['avg'] > 0.7:
        bonus = 25
    else:
        bonus = 5

    # Distractor loop: no impact on result
    cumulative = 0
    for i in range(3):
        for j in range(2):
            cumulative += i * j * stats.get('offset', 0)

    # Final formula
    rating = base_rating + (log_data['avg'] * multiplier * 10) + bonus
    return int(rating)

# Main execution
sensor_data = {
    'readings': [0.85, 0.72, 0.93, 0.68, 0.77],
    'device_id': 'THM-7X',
    'version': '2.1'
}

# Step 1: Analyze performance readings
efficiency_log = {}
efficiency_log['avg'] = analyze_performance(sensor_data)
efficiency_log['timestamp'] = '2024-05-17'
efficiency_log['readings_count'] = len(sensor_data['readings'])

# Step 2: Calculate thermal capacity based on efficiency
thermal_capacity = calculate_thermal_rating(efficiency_log)

# Output result as required
print(f"Result: {thermal_capacity}")