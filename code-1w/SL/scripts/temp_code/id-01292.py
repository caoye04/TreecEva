def analyze_readings(readings):
    filtered = [r for r in readings if r > 0]
    squared = [x * x for x in filtered if x % 2 == 1]
    sum_squares = sum(squared)
    count_filtered = len(filtered)
    
    # Distractor: irrelevant statistical computation
    mean_val = sum(readings) / len(readings) if readings else 0
    variance_proxy = sum((x - mean_val) ** 2 for x in readings) / len(readings) if readings else 0
    
    # Semi-relevant transformation
    normalized = [s / sum_squares for s in squared] if sum_squares != 0 else [0]
    return {'sum_squares': sum_squares, 'count': count_filtered, 'norm_peak': max(normalized)}


def adjust_threshold(base, factor=1.5):
    # Irrelevant helper with dead-end logic
    temp = base * factor
    temp -= 0.5
    if temp < 10:
        temp = 10
    return int(temp)  # Not actually used later


def calculate_final_score(data_map):
    values = list(data_map.values())
    total_impact = 0
    
    for entry in values:
        # Core logic step 1: weight by count
        contribution = entry['sum_squares'] * entry['count']
        
        # Core logic step 2: boost by norm_peak if above threshold
        if entry['norm_peak'] > 0.1:
            contribution *= 1.2
        
        total_impact += contribution
    
    # Distractor: unused intermediate aggregations
    all_peaks = [e['norm_peak'] for e in values]
    peak_average = sum(all_peaks) / len(all_peaks)
    adjusted_peaks = [p * 0.9 for p in all_peaks if p > peak_average]
    
    # Final scoring with modular adjustment
    modifier = len(values) % 7
    total_impact += modifier * 3
    
    return int(total_impact)

# Main execution flow
sensor_inputs = {
    'zone_a': [-5, 0, 3, 4, 5, -2, 7],
    'zone_b': [1, -1, 2, 3, 6, 8],
    'zone_c': [0, -3, -4, 5, 5, 1]
}

processed_data = {}
for zone, readings in sensor_inputs.items():
    result = analyze_readings(readings)
    processed_data[zone] = result

# Secondary distractor loop: computes but doesn't affect final result
aggregated_metrics = []
for k, v in processed_data.items():
    snapshot = {
        'zone': k,
        'density': v['count'] / (v['sum_squares'] + 1),
        'scaled_peak': v['norm_peak'] * 100
    }
    aggregated_metrics.append(snapshot)

final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")