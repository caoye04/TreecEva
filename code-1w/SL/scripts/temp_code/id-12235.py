import itertools

# Simulated sensor data preprocessing with red herrings
def acquire_signals():
    raw_stream = [128, 64, 32, 16, 8, 4, 2, 1]
    scaling_factor = 3.7  # unused distraction
    filtered = [x for x in raw_stream if x > 10]
    return filtered

# Irrelevant transformation chain
def legacy_normalization(data):
    shift_offset = -5  # decoy constant
    normalized = []
    for val in data:
        temp = val >> 2
        normalized.append(temp ^ 7)  # misleading bit manipulation
    return normalized

# Unused but plausible diagnostic
def compute_robustness_index(seq):
    return sum(x * x for x in seq if x % 2 == 0)

# Core processing function
def transform_readings(signal_group):
    # Real operation: apply logarithmic compression and accumulate
    compressed = list(map(lambda x: int(x ** 0.5), signal_group))
    reversed_seq = compressed[::-1]
    shifted = [reversed_seq[i] + i for i in range(len(reversed_seq))]
    return shifted

# Configuration with multiple decoys
baseline_config = {
    'threshold': 999,  # unused
    'active_mode': False,  # red herring
    'weighting': [1, 1, 1],  # irrelevant
    'version': 'legacy_v2'  # misleading
}

# Real metric processor
def process_metrics(dataset, config):
    # Accumulate with offset based on length
    base_accum = sum(dataset)
    
    # Decoy control flow (never executed due to hard-coded flag)
    debug_mode = False
    if debug_mode and config['active_mode']:
        return -999  # dead path
    
    # Real logic: add positional bonus
    bonus = 0
    for idx, val in enumerate(dataset):
        if (val + idx) % 3 == 0:
            bonus += 5
    
    # Additional real computation: pair product correction
    pairs = list(itertools.combinations(dataset, 2))
    product_correction = 0
    for a, b in pairs:
        if a == b:
            product_correction += a
    
    # Final result built from multiple steps
    intermediate = base_accum + bonus
    final_score = intermediate - product_correction  # correction subtracts
    return final_score

# Dead utility function (looks important)
def validate_calibration(reference):
    return any(x < 0 for x in reference), len(reference)

# Main execution flow
if __name__ == '__main__':
    # Step 1: Acquire real data
    signals = acquire_signals()  # [128, 64, 32, 16]
    
    # Step 2: Apply actual transformation
    transformed_data = transform_readings(signals)  # sqrt + reverse + shift
    
    # Step 3: Compute decoy index (unused)
    robustness = compute_robustness_index(transformed_data)
    
    # Step 4: Process with real logic
    final_diagnostic = process_metrics(transformed_data, baseline_config)
    
    # Output target result
    print(f"Result: {final_diagnostic}")