def analyze_readings(readings):
    # Irrelevant preprocessing: normalize values (not used in final result)
    normalized = [round(x / max(readings), 3) for x in readings]
    filtered = [x for x in readings if x > 50]
    stats = {
        'peak': max(readings),
        'base': min(readings),
        'span': len(readings)
    }
    # Distractor computation
    entropy = sum([x * x for x in normalized])
    return stats['span']

# Decoy function that looks important but is never called
def compute_robustness_score(data):
    score = 0
    for i in range(len(data)):
        if i % 2 == 0:
            score += data[i] // 3
        else:
            score -= data[i] % 7
    return score + 100

# Unused transformation
transform_table = {i: (i ** 2) % 19 for i in range(50)}

# Simulated sensor health data (core input)
raw_signals = [88, 53, 67, 91, 44, 76, 82, 59]

# Extraneous mapping
status_labels = {1: 'critical', 2: 'elevated', 3: 'normal'}

# Bitwise decoy calculation
checksum = 0
for val in raw_signals:
    checksum ^= (val << 2) | (val >> 1)

# Real data pipeline starts here
signal_matrix = [[x + 1 for x in raw_signals], [x - 1 for x in raw_signals]]

# Flatten and filter with list comprehension
flattened = [item for sublist in signal_matrix for item in sublist]
pruned = [x for x in flattened if x % 2 == 0]  # only even numbers

# Threshold logic setup
threshold_map = {
    'low': 60,
    'high': 85
}

# Auxiliary diagnostic flags (some are red herrings)
diag_flag_a = len(pruned) > 10
diag_flag_b = sum(pruned) < 500  # misleading intermediate
diag_flag_c = False

# Conditional expression with distractor
interim_state = 'active' if diag_flag_a or not diag_flag_b else 'standby'

# Core analysis function
def evaluate_segment(segment, limits):
    count_high = sum(1 for x in segment if x > limits['high'])
    count_low = sum(1 for x in segment if x < limits['low'])
    count_mid = len(segment) - count_high - count_low
    return {'high': count_high, 'mid': count_mid, 'low': count_low}

# Another irrelevant transformation
encoded_stream = ''.join([chr(97 + (x % 26)) for x in pruned[:10]])

# Real evaluation path
segment_analysis = evaluate_segment(pruned, threshold_map)

# Complex conditional expression using boolean logic and comparisons
alert_level = 2 if segment_analysis['high'] >= 3 else (1 if segment_analysis['low'] >= 5 else 0)

# Data structure manipulation
summary_stats = [
    segment_analysis['high'] * 2,
    segment_analysis['mid'],
    segment_analysis['low'] * 3
]

# Secondary processing chain
adjusted_scores = [x + alert_level for x in summary_stats]

# Final aggregation
aggregate_metric = sum(adjusted_scores) - alert_level

# Health data constructed from multiple sources
health_data = {
    'readings': raw_signals,
    'size': analyze_readings(raw_signals),
    'flags': [diag_flag_a, diag_flag_b],
    'encoded': encoded_stream  # unused in final function
}

# Main processing function
def process_metrics(data, thresholds):
    size_factor = data['size']
    raw_list = data['readings']
    
    # Re-filter using thresholds (redundant but relevant)
    above_high = [x for x in raw_list if x > thresholds['high']]
    below_low = [x for x in raw_list if x < thresholds['low']]
    
    # Intermediate derived values
    surge_count = len(above_high)
    deficit_count = len(below_low)
    
    # Nested conditional with distraction
    if surge_count > deficit_count:
        if surge_count >= 4:
            base_rating = 88
        else:
            base_rating = 77
    elif deficit_count > 0:
        base_rating = 66
    else:
        base_rating = 55
    
    # Final computation with distractor variables
    modifier = 0
    if 'flags' in data and len(data['flags']) > 1:
        if data['flags'][1]:
            modifier += 5
    
    # Critical line: what is the value of final_diagnostic?
    final_diagnostic = base_rating + modifier + size_factor
    
    # Dead code path (never reached due to return)
    if final_diagnostic < 0:
        final_diagnostic = 0
    
    return final_diagnostic

# Execution point
final_diagnostic = process_metrics(health_data, threshold_map)
print(f"Target result: {final_diagnostic}")