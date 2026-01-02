def analyze_efficiency(record):
    if record['cycles'] > 0:
        efficiency = record['output'] / record['cycles']
        penalty = 0.1 * record['errors']
        return efficiency - penalty
    return 0

# Simulate system diagnostics with mixed metrics
def process_performance(log, thresholds):
    temp_buffer = []
    total_weight = 0
    cumulative = 0
    adjustment_factor = 1.5

    for entry in log:
        raw_value = entry['value']
        category = entry['type']
        
        # Irrelevant preprocessing (distractor)
        normalized = raw_value / (sum([1 for _ in log]) or 1)
        temp_buffer.append(normalized)
        
        # Real computation begins
        base_score = raw_value * 0.8
        
        if category in thresholds:
            if base_score >= thresholds[category]:
                multiplier = 1.2
            else:
                multiplier = 0.9
        else:
            multiplier = 1.0
            
        adjusted = base_score * multiplier
        
        # Conditional boost for high-frequency entries (real logic)
        if entry.get('freq', 0) > 5:
            adjusted *= 1.1
            
        # Track only specific types (semi-relevant)
        if category in ['A', 'C']:
            cumulative += adjusted
            total_weight += 1

    # Dead code path (distractor)
    if len(temp_buffer) > 100:
        fallback = sum(temp_buffer) * adjustment_factor
    else:
        fallback = None
    
    # Final aggregation using auxiliary data
    helper_data = {'offset': 5, 'decay': 0.95}
    decayed_cumulative = cumulative * helper_data['decay']
    final_score = int(decayed_cumulative + helper_data['offset'])
    
    # Unused intermediate variables (red herrings)
    avg_temp = sum(temp_buffer) / len(temp_buffer) if temp_buffer else 0
    peak = max([x for x in temp_buffer], default=0)
    
    return final_score

# Input data setup
metrics_log = [
    {'type': 'A', 'value': 10, 'freq': 3},
    {'type': 'B', 'value': 15, 'freq': 6},
    {'type': 'C', 'value': 20, 'freq': 7},
    {'type': 'A', 'value': 12, 'freq': 2},
    {'type': 'D', 'value': 18, 'freq': 8}
]

threshold_map = {'A': 9, 'C': 18}

# Execution point of interest
final_score = process_performance(metrics_log, threshold_map)

# Output result
print(f"Result: {final_score}")