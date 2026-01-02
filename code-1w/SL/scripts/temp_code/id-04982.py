def transform_signal(raw_values, scale_factor):
    """Apply non-linear transformation to sensor signal (distractor function)."""
    return [round((x ** 1.5) / scale_factor + 2) for x in raw_values if x > 0]


def validate_checksum(entry):
    """Validate data entry checksum (dead code path)."""
    total = sum(int(digit) for digit in str(entry))
    return total % 7 == 0


def recursive_filter(items, limit):
    """Recursively filter items below limit (irrelevant logic)."""
    if not items:
        return []
    head, tail = items[0], items[1:]
    filtered_tail = recursive_filter(tail, limit)
    return [head] + filtered_tail if head < limit else filtered_tail + [limit * 2]


def decode_sequence(seq):
    """Decode binary-like sequence into status codes (decoy)."""
    result = 0
    for bit in seq:
        result = (result << 1) | bit
    return result ^ 0b1010


def aggregate_metrics(records):
    """Compute statistical summary of records (partially relevant)."""
    count = len(records)
    avg = sum(records) / count if count else 0
    variance = sum((x - avg) ** 2 for x in records) / count if count else 0
    peak = max(records) if records else 0
    return {'count': count, 'avg': round(avg, 3), 'variance': round(variance, 4), 'peak': peak}


def process_readings(raw_data, config):
    """Main processing pipeline for sensor array data."""
    # Irrelevant preprocessing steps
    temp_store = {f'idx_{i}': val * config['gain'] for i, val in enumerate(raw_data)}
    masked_data = [val for i, val in enumerate(raw_data) if i % 3 != 2]  # Skip every third

    # Core transformation
    adjusted = [(val * 1.8 + 32) for val in raw_data]  # Convert to pseudo-Fahrenheit

    # Red herring computation
    entropy = 0.0
    for v in adjusted:
        if v > 0:
            entropy -= (v / 100) * ((v / 100) ** 0.5)

    # Actual relevant logic starts here
    clipped = [min(max(v, 55), 95) for v in adjusted]  # Clamp to operational range
    baseline = sum(clipped) // len(clipped)  # Integer division for reference

    # Build threshold map using dictionary operations
    threshold_map = {
        'low_warning': baseline - 15,
        'high_warning': baseline + 20,
        'critical': baseline + 35 if baseline > 70 else baseline + 25
    }

    # Simulate secondary system sync (distractor)
    sync_pattern = tuple((baseline * i) % 17 for i in range(1, 5))

    # Generate processed output
    processed = [abs(c - baseline) * 2 for c in clipped]

    # Inject decoy conditional
    if len(processed) > 5 and threshold_map['high_warning'] < 85:
        processed[-1] = processed[0]  # Misleading mutation

    return processed, threshold_map, baseline


def analyze_readings(data, thresholds):
    """Final diagnostic analyzer based on processed data."""
    score = 0
    
    # Logical evaluation chain with multiple steps
    for val in data:
        if val < thresholds['low_warning']:
            score += 3
        elif val < thresholds['high_warning']:
            score += 7
        elif val < thresholds['critical']:
            score += 12
        else:
            score += 18
    
    # Secondary adjustment based on distribution
    above_median = len([v for v in data if v > sum(data)/len(data)])
    if above_median > len(data) // 2:
        score = int(score * 1.1)

    # Tertiary rule: penalize uniformity
    unique_vals = len(set(round(v, 1) for v in data))
    if unique_vals < len(data) // 3:
        score -= 15

    # Final nonlinear scaling
    final_score = int((score ** 1.05))

    # Decoy post-processing
    debug_trace = {f'step_{i}': final_score >> i for i in range(3)}

    return final_score

# Main execution block
if __name__ == '__main__':
    # Input data (simulated sensor readings)
    sensor_input = [23, 25, 24, 26, 28, 30, 29, 31, 33, 35, 34, 36]
    
    # Configuration map with red herrings
    config_params = {
        'gain': 1.05,
        'offset': -4,
        'sampling_rate': 100,
        'channel_mask': [1, 0, 1, 1],
        'timeout_ms': 500
    }
    
    # Trigger irrelevant functions (distractors)
    dummy_signal = transform_signal(sensor_input, 2.5)
    filtered_recursive = recursive_filter(sensor_input, 30)
    checksum_valid = validate_checksum(12345)
    decoded = decode_sequence([1, 0, 1, 1])
    
    # Execute core processing
    processed_data, threshold_map, base_ref = process_readings(sensor_input, config_params)
    
    # Critical statement
    final_diagnostic = analyze_readings(processed_data, threshold_map)
    
    # Additional noise
    metrics = aggregate_metrics(processed_data)
    anomaly_flag = metrics['variance'] > 50 or decoded == 12
    
    print(f"Result: {final_diagnostic}")