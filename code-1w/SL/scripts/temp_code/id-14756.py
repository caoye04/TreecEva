import itertools

# Simulated system performance metrics from distributed sensors
def collect_metrics():
    raw_data = [18, 23, 14, 17, 26, 21, 13, 19]
    filtered = [x for x in raw_data if x > 15]  # Only consider values above threshold
    normalized = [round(x / max(raw_data), 3) for x in filtered]
    return {
        'readings': raw_data,
        'filtered_norm': normalized,
        'outliers': [x for x in raw_data if x < 15],
        'checksum': sum(raw_data) ^ 0xAB  # Bitwise red herring
    }

# Legacy function - not used but looks important
def deprecated_analysis(data):
    cumulative = 0
    for i in range(len(data)):
        cumulative += data[i] * (i % 4 + 1)
    return cumulative >> 2

# Baseline calibration with decoy operations
def generate_baseline():
    sequence = list(range(5, 25, 3))
    shift_key = sum(sequence) % 7
    transformed = [((x << 1) ^ 5) % 30 for x in sequence]  # Complex-looking transformation
    history = {k: v for k, v in enumerate(transformed)}  # Unused dictionary
    return {
        'window': sequence[::2],
        'shift': shift_key,
        'mask': 0xF0 | shift_key,
        'average': sum(sequence) / len(sequence)
    }

# Core evaluation logic with distractors
def evaluate_performance(metrics, base):
    readings = metrics['filtered_norm']
    window = base['window']
    
    # Irrelevant accumulation path
    temp_accum = 0
    for val in window:
        temp_accum += (val * 0.1) ** 2
    dummy_check = int(temp_accum * 100) & 0xFF
    
    # Real computation begins here
    weighted_sum = sum(readings) * 100  # Scale to percentage-like metric
    adjustment = base['average'] / 10
    
    # Apply conditional boost based on pattern match
    patterns = list(itertools.combinations([1, 2, 3, 4], 3))
    pattern_influence = len(patterns) % 5  # Always 4, but looks dynamic
    
    # Distractor: complex slicing that leads nowhere
    critical_slice = readings[1:6:2]
    shadow_value = sum(critical_slice) / len(critical_slice) if critical_slice else 0
    shadow_value = round(shadow_value, 2) ^ 100  # Misleading bit op
    
    # Actual score calculation
    base_score = weighted_sum - adjustment
    if len(metrics['outliers']) < 4:
        base_score += pattern_influence * 2
    
    # Final adjustment using bitwise (relevant only in masking low bits)
    final_score = int(base_score) & 0xFFFF  # Clamp to 16-bit range
    return final_score

# Orchestration with dead code branches
if __name__ == "__main__":
    # Initialize components
    metrics = collect_metrics()
    baseline = generate_baseline()

    # Simulate diagnostic mode (unused)
    debug_mode = False
    if debug_mode:
        print("Diagnostic:", deprecated_analysis(metrics['readings']))

    # Key execution point
    final_score = evaluate_performance(metrics, baseline)

    # Dead branch with plausible-looking correction
    if final_score < 0:
        final_score = abs(final_score) ^ 0xFF
    
    # Output result
    print(f"Result: {final_score}")