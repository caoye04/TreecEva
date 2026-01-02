def analyze_growth_patterns(data, config):
    # Irrelevant transformation (distractor)
    normalized = [round(x * 1.07 + 3.2, 2) for x in data]
    offset_values = [n - 5 for n in normalized if n > 10]

    # Real computation begins: categorize growth intensity
    categories = []
    for val in data:
        if val < config['low_threshold']:
            categories.append('stunted')
        elif val < config['mid_threshold']:
            categories.append('moderate')
        else:
            categories.append('optimal')
    
    # Count distribution using enumerate (required feature)
    count_map = {key: 0 for key in set(categories)}
    for idx, cat in enumerate(categories):
        count_map[cat] += 1

    # Secondary irrelevant calculation (distractor)
    avg_normalized = sum(normalized) / len(normalized) if normalized else 0
    penalty_score = sum(1 for ov in offset_values if ov > avg_normalized)

    return count_map, avg_normalized


def calculate_harvest_efficiency(clusters, thresholds):
    efficiency_log = []
    total_yield = 0
    
    # Use of zip and lambda together (required features)
    paired_configs = zip(clusters['readings'], clusters['weights'])
    weighted_func = lambda r, w: r * (w + 0.5) if r >= thresholds['base'] else r * 0.3
    
    for reading, weight in paired_configs:
        # Core logic embedded within distraction
        adjusted = weighted_func(reading, weight)
        
        # Irrelevant conditional branch (distractor)
        if adjusted > 40:
            status_flag = 'overperforming'
            correction_factor = 0.9
        else:
            status_flag = 'baseline'
            correction_factor = 1.0  # unused

        # Actual yield contribution
        if adjusted >= thresholds['base']:
            bonus = 1.2 if adjusted > thresholds['bonus'] else 1.0
            total_yield += adjusted * bonus
        
        efficiency_log.append({'value': adjusted, 'flag': status_flag})
    
    # Additional distractor: set operation with no impact
    log_flags = set(entry['flag'] for entry in efficiency_log)
    if 'overperforming' in log_flags:
        dummy_metric = len(log_flags) * 15
    
    return int(total_yield)  # deterministic integer output

# Main execution context
if __name__ == '__main__':
    # Input data
    sensor_readings = [12, 18, 25, 30, 45, 52]
    weights = [0.8, 1.1, 0.9, 1.3, 1.0, 1.4]
    
    # Configuration map
    settings = {
        'low_threshold': 15,
        'mid_threshold': 30,
        'smoothing_factor': 0.05
    }
    
    # Trigger irrelevant analysis (distractor call)
    growth_stats, norm_avg = analyze_growth_patterns(sensor_readings, settings)
    
    # Prepare real input structure
    cluster_data = {
        'readings': sensor_readings,
        'weights': weights
    }
    
    threshold_map = {
        'base': 20,
        'bonus': 40
    }
    
    # Key statement
    final_yield = calculate_harvest_efficiency(cluster_data, threshold_map)
    
    print(f"Result: {final_yield}")