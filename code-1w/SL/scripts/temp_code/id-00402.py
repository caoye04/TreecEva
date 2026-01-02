def analyze_metrics(log_entries, criteria):
    cumulative_score = 0
    penalty_adjustment = 0
    temp_buffer = []
    severity_map = {1: 'low', 2: 'medium', 3: 'high'}
    
    for idx, entry in enumerate(log_entries):
        raw_value = entry['value']
        timestamp = entry['time']
        category = entry['type']
        
        # Irrelevant time-based filtering (unused)
        if timestamp < 1000:
            continue
            unused_path = [x ** 2 for x in range(10)]

        # Distractor: complex but unused transformation
        transformed = 0
        for shift in range(3):
            transformed |= (raw_value >> shift) & (1 << (shift + 1))
        
        # Real logic begins
        base_metric = raw_value * 0.85
        if category == 'sensor':
            base_metric += 12
        elif category == 'network':
            base_metric -= 5

        # Use of zip to align with external weights (relevant)
        weights = [0.5, 1.2, 0.8, 1.0]
        flags = [entry['flag_a'], entry['flag_b'], entry['flag_c'], entry['flag_d']]
        for w, f in zip(weights, flags):
            if f:
                base_metric *= w

        # Conditional state tracking
        if base_metric > criteria['critical']:
            penalty_adjustment += 3
        elif base_metric > criteria['warning']:
            penalty_adjustment += 1

        # Only every even-indexed entry contributes to final score
        if idx % 2 == 0:
            cumulative_score += int(base_metric)

        # Dead code: buffer never used again
        temp_buffer.append({'index': idx, 'score': base_metric})
        if len(temp_buffer) > 5:
            temp_buffer.pop(0)

    # Final diagnostic based on aggregated score and adjustment
    final_diagnostic = cumulative_score - penalty_adjustment * 2
    return final_diagnostic


# Simulated system log data
system_log = [
    {'value': 40, 'time': 500, 'type': 'sensor', 'flag_a': True, 'flag_b': False, 'flag_c': True, 'flag_d': False},
    {'value': 60, 'time': 700, 'type': 'network', 'flag_a': False, 'flag_b': True, 'flag_c': False, 'flag_d': True},
    {'value': 35, 'time': 1200, 'type': 'sensor', 'flag_a': True, 'flag_b': True, 'flag_c': False, 'flag_d': False},
    {'value': 70, 'time': 1500, 'type': 'sensor', 'flag_a': False, 'flag_b': False, 'flag_c': False, 'flag_d': True},
    {'value': 25, 'time': 1800, 'type': 'network', 'flag_a': True, 'flag_b': True, 'flag_c': True, 'flag_d': True}
]

# Thresholds for analysis
thresholds = {
    'warning': 45,
    'critical': 60,
    'grace_period': 30
}

# Execution point of interest
final_diagnostic = analyze_metrics(system_log, thresholds)
print(f"Result: {final_diagnostic}")