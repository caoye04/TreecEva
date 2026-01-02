import itertools

def analyze_sequence(values):
    filtered = [v for v in values if v > 0]
    running_total = 0
    peak_magnitude = 0
    temp_results = []
    
    for i, val in enumerate(filtered):
        if i % 2 == 0:
            running_total += val ** 2
        else:
            running_total -= val
        
        if val > peak_magnitude:
            peak_magnitude = val
            
        temp_results.append(running_total * 0.1)
    
    return running_total, peak_magnitude, temp_results

def compute_baseline(reference_set):
    base = sum(reference_set) / len(reference_set)
    adjusted = [x - base for x in reference_set]
    return base, set(adjusted)

def process_metrics(log_data, limit):
    # Extract numeric sequences
    raw_sequences = [entry['metrics'] for entry in log_data if entry['active']]
    flattened = list(itertools.chain.from_iterable(raw_sequences))
    
    # Irrelevant aggregation
    outlier_count = 0
    for x in flattened:
        if x > 100 or x < -10:
            outlier_count += 1  # distractor: not used later
    
    # Compute baseline from auxiliary data
    aux_data = [4, 8, 12, 16, 20]
    base_val, deviation_set = compute_baseline(aux_data)
    
    # Analyze main sequence
    total, peak, history = analyze_sequence(flattened)
    
    # Simulate correction factor (only partially used)
    corrections = []
    for h in history:
        if h > 5:
            corrections.append(h * 0.05)
        else:
            corrections.append(h * 0.02)
    net_correction = sum(corrections)  # semi-relevant but diminished impact
    
    # Core logic path
    valid_points = [f for f in flattened if f <= limit]
    aggregate = sum(valid_points)
    efficiency_score = int((aggregate / (peak + 1)) + net_correction)
    
    # Dead code branch (never executed under normal inputs)
    if False and len(deviation_set) > 10:
        efficiency_score *= 2
    
    # Final output construction
    diagnostics = {
        'count': len(valid_points),
        'sum': aggregate,
        'correction': net_correction,
        'efficiency': efficiency_score
    }
    
    final_output = efficiency_score
    return final_output

data_log = [
    {'metrics': [3, -5, 12, 8, 20], 'active': True},
    {'metrics': [7, 15, -3, 4], 'active': True},
    {'metrics': [1000, 2000], 'active': False},  # inactive, so ignored
    {'metrics': [5, 9, 1], 'active': True}
]
threshold = 100

result = process_metrics(data_log, threshold)
print(f"Result: {result}")