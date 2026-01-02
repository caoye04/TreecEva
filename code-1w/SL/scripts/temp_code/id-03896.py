import math

# Simulated sensor data with noise and irrelevant entries
data_stream = [
    {'id': 'A7', 'val': 12.5, 'type': 'temp', 'seq': 1},
    {'id': 'B3', 'val': -3.2, 'type': 'pressure', 'seq': 2},
    {'id': 'C9', 'val': 8.7, 'type': 'temp', 'seq': 3},
    {'id': 'D2', 'val': 15.1, 'type': 'humidity', 'seq': 4},
    {'id': 'E5', 'val': 6.3, 'type': 'temp', 'seq': 5},
    {'id': 'F1', 'val': 0.0, 'type': 'pressure', 'seq': 6},
    {'id': 'G8', 'val': -5.4, 'type': 'temp', 'seq': 7},
    {'id': 'H4', 'val': 9.8, 'type': 'temp', 'seq': 8}
]

# Irrelevant lookup table for unused device calibration
calibration_map = {
    'A7': lambda x: x * 1.02,
    'B3': lambda x: x + 0.5,
    'X9': lambda x: x ** 0.5,  # Unused device
    'Z1': lambda x: x - 1.1   # Dead entry
}

# Misleading transformation chain (partially unused)
def transform_value(v, mode='raw'):
    if mode == 'corrected':
        return v * 1.1
    elif mode == 'filtered':
        return abs(v) ** 0.5
    else:
        return v  # Default passthrough

# Decoy function that looks important but isn't used
def analyze_trend(sequence):
    trend_score = 0
    for i in range(1, len(sequence)):
        trend_score += (sequence[i] - sequence[i-1]) * i
    return trend_score / len(sequence) if sequence else 0

# Auxiliary function to extract relevant entries
def filter_by_type(data, target_type='temp'):
    result = []
    for entry in data:
        if entry['type'] == target_type:
            result.append(entry)
    return result

# Complex signal processor with red herring logic
def process_signals(entries, settings):
    values = [e['val'] for e in entries]
    
    # Real computation begins here
    base_sum = sum(values)
    
    # Distractor: unused statistical measures
    mean_val = base_sum / len(values) if values else 0
    variance = sum((x - mean_val) ** 2 for x in values) / len(values) if values else 0
    stdev = math.sqrt(variance)
    
    # Red herring normalization (not applied)
    normalized = [(v - mean_val) / stdev for v in values] if stdev != 0 else values
    
    # Actual path: apply threshold filtering based on config
    threshold = settings.get('threshold', 0)
    filtered_values = [v for v in values if v > threshold]
    
    # Secondary processing: map through conditional expression
    processed = []
    for v in filtered_values:
        # Conditional expression usage (python idiom)
        adjusted = v * 1.5 if v < 10 else v * 0.9
        processed.append(adjusted)
    
    # Summation and accumulation pattern
    accumulator = 0
    for idx, val in enumerate(processed):
        # Recursive-like weighting without actual recursion
        weight = 1 + (idx * 0.1)
        accumulator += val * weight
    
    # Final nonlinear transformation
    final = int(accumulator + 0.5) if accumulator >= 0 else int(accumulator - 0.5)
    
    # Dead code branch (never reached due to structure)
    if False:
        fallback = 0
        for v in normalized:
            fallback += math.log(abs(v) + 1)
        final = fallback
    
    return final

# Configuration with misleading extra keys
config = {
    'mode': 'aggressive',
    'threshold': 5.0,  # Critical parameter
    'window': 3,
    'calibrate': True,
    'debug_level': 99,  # Unused
    'timeout': 1500     # Unused
}

# Main execution flow
filtered_data = filter_by_type(data_stream, 'temp')

# Irrelevant preprocessing step (looks important)
sorted_data = sorted(filtered_data, key=lambda x: x['seq'])
reversed_ids = [entry['id'][::-1] for entry in sorted_data]  # String manipulation red herring

# Key statement
final_output = process_signals(filtered_data, config)

# Output result
print(f"Result: {final_output}")