def analyze_trends(data_map):
    trend_strength = 0
    temp_factor = 0
    for key, values in data_map.items():
        if len(values) > 3:
            avg_val = sum(values) / len(values)
            if avg_val > 50:
                trend_strength += 1
            temp_factor += avg_val % 7
    return trend_strength

def calculate_rating(metrics):
    base_score = 0
    adjustment = 0
    outlier_count = 0

    # Real logic starts here
    for category, readings in metrics.items():
        if 'sensor' in category:
            max_val = max(readings)
            min_val = min(readings)
            range_val = max_val - min_val
            if range_val > 30:
                base_score += 15
        else:
            avg = sum(readings) / len(readings)
            adjustment += avg // 10

    # Distractor block: complex but unused calculation
    noise_floor = 0
    for i in range(5):
        for j in range(3):
            noise_floor += (i * j) % 4

    # Another distractor: irrelevant state tracking
    status_log = {}
    for idx in range(len(metrics)):
        status_log[f'entry_{idx}'] = 'processed'

    # Core computation with dictionary lookup effect
    multiplier_map = {'A': 2, 'B': 3, 'C': 1}
    key_metric = list(metrics.keys())[0]
    modifier = multiplier_map.get('A', 1)

    final_score = base_score + adjustment * modifier

    # This variable is printed as result
    return final_score

# Input data
engagement_data = {
    'sensor_x': [45, 67, 89, 91],
    'sensor_y': [34, 78, 85],
    'network_a': [23, 45, 67, 89],
    'system_load': [56, 61, 66]
}

result = calculate_rating(engagement_data)
print(f"Result: {result}")