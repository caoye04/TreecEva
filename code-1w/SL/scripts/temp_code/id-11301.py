def analyze_performance(metrics, thresholds):
    high_performers = []
    temp_scores = []
    noise_counter = 0

    for key, values in metrics.items():
        avg = sum(values) / len(values)
        if avg > thresholds.get(key, 0):
            high_performers.append(key)
        temp_scores.append(avg * 0.85)  # Distractor: scaled but unused later

        # Simulate noise detection (irrelevant to final result)
        for v in values:
            if v < 0:
                noise_counter += 1

    return high_performers


def transform_data(raw):
    # Split and restructure data
    lines = raw.strip().split('\n')
    records = [line.split(',') for line in lines]
    
    # Extract numeric values and ignore headers
    parsed = []
    for r in records:
        if r[0] == 'id':
            continue
        parsed.append({
            'id': int(r[0]),
            'values': [float(x) for x in r[1:]]
        })
    
    # Irrelevant transformation
    stats_summary = {
        'count': len(parsed),
        'meta_flag': True
    }
    
    return parsed, stats_summary


def calculate_final_score(data_list):
    base_scores = []
    penalty_log = []
    
    for entry in data_list:
        raw_sum = sum(entry['values'])
        count = len(entry['values'])
        
        # Apply conditional adjustment
        adjustment = 1.0
        if count > 3:
            adjustment = 0.95
        elif count == 2:
            adjustment = 1.05
            
        adjusted = raw_sum * adjustment
        
        # Red herring computation
        outlier_count = 0
        for v in entry['values']:
            if v > 100:
                outlier_count += 1
        if outlier_count > 0:
            penalty_log.append(outlier_count * 0.1)

        base_scores.append(adjusted)
    
    # Real calculation path
    total_base = sum(base_scores)
    modifier = len(penalty_log) * 0.05  # Minor influence, but mostly irrelevant
    final = total_base * (0.9 + modifier)
    
    # Key distractor: complex but unused list comprehension
    ignored_diagnostics = [{'item': s, 'flag': s > 200} for s in base_scores if s < 0]
    
    return int(final)  # Deterministic integer output

# Main execution
raw_input = '''id,val1,val2,val3,val4\n1,10,20,30,40\n2,15,25\n3,8,12,18'''  

parsed_data, metadata = transform_data(raw_input)

criteria = {
    'val1': 12,
    'val2': 18,
    'val3': 25,
    'val4': 35
}

qualified = analyze_performance({
    'val1': [10,15,8], 'val2': [20,25,12], 'val3': [30,0,18], 'val4': [40,0,0]
}, criteria)

# Additional irrelevant state tracking
tracking_states = {i: 'processed' for i in range(len(parsed_data))}
dummy_aggregate = sum([len(entry['values']) for entry in parsed_data])

final_score = calculate_final_score(parsed_data)
print(f"Result: {final_score}")