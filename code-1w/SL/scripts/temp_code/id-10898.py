import math

def analyze_signal_strength(signal, baseline):
    # Irrelevant helper function (dead code path)
    return int(math.sqrt(signal) * baseline // 2)

def validate_readings(readings):
    # Distractor function: looks important but unused
    return all(r > 0 for r in readings)

def transform_sequence(seq):
    # Complex-looking transformation not used in main logic
    return [seq[i] ^ seq[-i-1] for i in range(len(seq)) if i % 2 == 0]

def compute_entropy(data):
    # Seemingly relevant but ultimately irrelevant computation
    total = sum(data)
    probs = [d / total for d in data if d > 0]
    return -sum(p * math.log2(p) for p in probs)

def filter_outliers(values, limit=3):
    # Dead branch with misleading statistical logic
    mean_val = sum(values) / len(values)
    std_dev = (sum((x - mean_val) ** 2 for x in values) / len(values)) ** 0.5
    return [v for v in values if abs(v - mean_val) <= limit * std_dev]

def aggregate_metrics(data, config):
    # Core logic buried among distractions
    
    # Step 1: Extract active sensors (non-zero readings)
    active_sensors = [s for s in data['readings'] if s != 0]
    
    # Step 2: Apply threshold mask using bitwise logic
    threshold_mask = config['mask']
    masked_values = [v & threshold_mask for v in active_sensors]
    
    # Step 3: Count how many pass dynamic threshold (value > index + offset)
    dynamic_pass = 0
    for idx, val in enumerate(masked_values):
        offset = config['base_offset']
        if val > idx + offset:
            dynamic_pass += 1
    
    # Step 4: Use set logic to detect anomalies
    expected_range = set(range(config['min_range'], config['max_range']))
    observed_set = set(masked_values)
    missing_in_observed = expected_range - observed_set
    anomaly_count = len(missing_in_observed)
    
    # Step 5: Apply correction factor based on config flags
    correction_factor = 1
    if config['flags']['adjust_phase']:
        correction_factor *= 2
    if config['flags']['invert_signal'] and not config['flags']['adjust_phase']:
        correction_factor *= -1
    
    # Step 6: Compute weighted diagnostic score
    raw_score = dynamic_pass * 17 - anomaly_count * 3
    adjusted_score = raw_score * correction_factor
    
    # Step 7: Final clamping with conditional rounding
    if adjusted_score > 0:
        final_value = math.ceil(adjusted_score / 4.0)
    else:
        final_value = math.floor(adjusted_score / 5.0)
    
    # Step 8: Inject secondary adjustment from auxiliary map
    aux_map = {k: v**2 for k, v in config['aux_weights'].items()}
    adjustment = aux_map.get('diagnosis', 0) - aux_map.get('fallback', 0)
    
    # Step 9: Final diagnostic calculation
    result = final_value + adjustment
    
    # Irrelevant debug prints (no effect)
    debug_trace = [result + i for i in range(3) if i > 5]  # Empty list
    
    return result

# Main execution block
if __name__ == '__main__':
    # Simulated sensor input (real data)
    sensor_data = {
        'source': 'array_7B',
        'timestamp': 1718923401,
        'readings': [12, 0, 15, 10, 7, 0, 4, 14],  # Zeros will be filtered
        'calibration': [1.1, 0.9, 1.0, 1.2]
    }

    # Configuration with multiple red herrings
    thresholds = {
        'mask': 15,                    # 4-bit mask (keeps low nibble)
        'base_offset': 5,
        'min_range': 3,
        'max_range': 12,
        'flags': {
            'adjust_phase': True,       # Affects correction factor
            'invert_signal': False,     # Not triggered due to adjust_phase=True
            'debug_mode': True          # Unused flag (distractor)
        },
        'aux_weights': {
            'diagnosis': 3,             # Contributes +9 to final result
            'fallback': 2,                # Contributes -4 (but squared!)
            'spare': 5                  # Unused weight (distractor)
        },
        'history_window': [0.8, 0.9]   # Unused
    }

    # Unused variables (distractors)
    baseline_ref = 2048
    signal_chain = [analyze_signal_strength(x, baseline_ref) for x in sensor_data['readings']]
    entropy_metric = compute_entropy(sensor_data['readings'])
    filtered_reads = filter_outliers(sensor_data['readings'], limit=2)
    transformed_seq = transform_sequence(sensor_data['readings'])

    # Key execution point
    final_diagnostic = aggregate_metrics(sensor_data, thresholds)
    print(f"Target result: {final_diagnostic}")