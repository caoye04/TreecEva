def process_signals(data, thresholds):
    cumulative_score = 0
    adjustment_factor = 1.5
    temp_results = []

    for entry in data:
        signal_id = entry['id']
        raw_value = entry['value']
        category = entry['category']

        # Irrelevant intermediate computation (distractor)
        normalized = raw_value / (sum([1 for _ in data]) + 1e-5)
        
        if category in thresholds:
            if raw_value > thresholds[category]:
                flagged = True
                penalty = len([c for c in category if c.isupper()])  # Useless penalty calc
                cumulative_score += int(raw_value * 0.1)
            else:
                flagged = False
            
            # Actual logic contribution
            if raw_value % 2 == 1:
                temp_results.append(raw_value * adjustment_factor)
    
    # Dead code path (misleading - never alters final outcome)
    if len(temp_results) > 100:
        temp_results = temp_results[::-2]

    # Core contribution: XOR-based aggregation
    aggregated = 0
    for val in temp_results:
        aggregated ^= int(val)

    final_output = aggregated + cumulative_score
    return final_output

# Simulated sensor input
sensor_data = [
    {'id': 'S1', 'value': 23, 'category': 'TEMP'},
    {'id': 'S2', 'value': 44, 'category': 'PRESS'},
    {'id': 'S3', 'value': 17, 'category': 'TEMP'},
    {'id': 'S4', 'value': 39, 'category': 'FLOW'},
    {'id': 'S5', 'value': 51, 'category': 'TEMP'},
    {'id': 'S6', 'value': 28, 'category': 'PRESS'}
]

# Threshold configuration map (real control logic)
threshold_map = {
    'TEMP': 20,
    'PRESS': 40,
    'FLOW': 35
}

# Filtering step - only some entries qualify (reduces cognitive clarity)
filtered_data = [s for s in sensor_data if s['value'] > 15 and s['category'] != 'DEBUG']

# Auxiliary variable (unused, distraction)
baseline_metrics = {k: 0 for k in threshold_map.keys()}
scaling_coefficients = [1.1, 2.3, 0.9, 1.4]  # Unused list comprehension red herring

# Key execution point
final_output = process_signals(filtered_data, threshold_map)

# Print result as required
print(f"Target result: {final_output}")