import math

def analyze_signal_strength(raw_data, bias_factor):
    adjusted = [x * 0.87 + bias_factor for x in raw_data]
    return [val for val in adjusted if val > 0]

def compute_entropy(values):
    total = sum(values)
    if total == 0:
        return 0.0
    probabilities = [v / total for v in values]
    entropy = -sum(p * math.log(p) for p in probabilities if p > 0)
    return round(entropy, 6)

def validate_checksum(record):
    # Irrelevant validation logic (dead path)
    checksum = sum(ord(c) for c in record) % 256
    return checksum < 200

def transform_dataset(data, mode='fast'):
    # Distractor transformation with no impact on final result
    if mode == 'legacy':
        return [d ** 0.5 for d in data if d > 5]
    elif mode == 'debug':
        return [d for d in data if d % 2 == 0]
    else:
        return [d for d in data]  # No-op effectively

def evaluate_stability(readings):
    mean_val = sum(readings) / len(readings)
    variance = sum((x - mean_val) ** 2 for x in readings) / len(readings)
    return variance < 15

def process_metrics(log_entries, threshold):
    # Core relevant logic begins
    base_values = [entry['value'] for entry in log_entries]
    
    # Irrelevant filtering based on unused condition
    filtered_by_type = [e for e in log_entries if e.get('type') != 'deprecated']
    type_filtered_vals = [e['value'] for e in filtered_by_type]
    
    # Red herring: signal analysis that doesn't affect output
    signal_analysis = analyze_signal_strength(base_values, bias_factor=2.1)
    entropy_metric = compute_entropy(signal_analysis)  # Computed but unused later
    
    # Real processing chain
    active_entries = [v for v in base_values if v >= threshold]
    suppressed_noise = [v for v in active_entries if v < 300]  # Filter outliers
    
    # Count valid segments
    segment_count = 0
    temp_sum = 0
    for val in suppressed_noise:
        if val > threshold * 1.5:
            segment_count += 1
        temp_sum += val
    
    # Key intermediate: average after noise suppression
    avg_post_filter = temp_sum / len(suppressed_noise) if suppressed_noise else 0
    
    # Conditional expression determining control flow (Python-specific feature)
    adjustment = 1.25 if avg_post_filter > 40 else 0.9
    
    # Simulated hardware efficiency model
    efficiency_score = 0
    level = 'low'
    if avg_post_filter > 50:
        efficiency_score = int(avg_post_filter * adjustment * 1.8)
        level = 'high'
    elif avg_post_filter > 30:
        efficiency_score = int(avg_post_filter * adjustment * 1.4)
        level = 'medium'
    else:
        efficiency_score = int(avg_post_filter * adjustment)
        level = 'low'
    
    # Dead code branch - never executed due to prior logic
    if level == 'unknown':
        efficiency_score = -1
    
    # Decoy assignment with misleading name
    final_integrity_check = evaluate_stability(base_values)
    
    # Return key variable
    return efficiency_score

data_log = [
    {'value': 25, 'type': 'primary'},
    {'value': 67, 'type': 'primary'},
    {'value': 12, 'type': 'backup'},
    {'value': 88, 'type': 'primary'},
    {'value': 45, 'type': 'primary'},
    {'value': 34, 'type': 'backup'},
    {'value': 91, 'type': 'primary'},
    {'value': 52, 'type': 'primary'},
    {'value': 29, 'type': 'primary'},
    {'value': 73, 'type': 'primary'}
]

threshold = 30

# Unused transformations (distractors)
decoy_data_a = transform_dataset([item['value'] for item in data_log], mode='debug')
decoy_data_b = transform_dataset([item['value'] for item in data_log], mode='legacy')

# Critical execution point
final_output = process_metrics(data_log, threshold)

# Print result as required
print(f"Result: {final_output}")