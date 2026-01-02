import itertools

# Simulated sensor array diagnostics with noise filtering and pattern analysis
def collect_sensor_readings():
    raw_readings = [18, 23, 15, 47, 29, 31, 22, 44, 36, 28]
    noise_floor = 10
    filtered = [x for x in raw_readings if x > noise_floor]
    baseline = sum(filtered[:5]) / 5
    return {'data': filtered, 'baseline': baseline, 'version': '2.1'}

def apply_calibration(signal, factor=1.05):
    calibrated = [round(x * factor, 2) for x in signal]
    # Dead code path - never used
    if len(calibrated) > 20:
        return [x for x in calibrated if x % 2 == 0]
    return calibrated

def generate_combinations(values):
    # Irrelevant combinatorial expansion
    combos = []
    for r in range(2, 4):
        combos.extend(itertools.combinations(values, r))
    combo_sum = sum(len(c) for c in combos[:100])  # Distractor computation
    return combo_sum

def mask_outliers(data, threshold_multiplier=1.8):
    median_val = sorted(data)[len(data)//2]
    cutoff = median_val * threshold_multiplier
    masked = [x if x <= cutoff else (x ^ 15) & 31 for x in data]  # Bit manipulation red herring
    stats = {
        'original_mean': sum(data) / len(data),
        'masked_mean': sum(masked) / len(masked),
        'distortion_index': abs(sum(masked) - sum(data))
    }
    return masked, stats

def compute_entropy(values):
    total = sum(values)
    if total == 0:
        return 0.0
    probabilities = [v / total for v in values]
    entropy = -sum(p * __import__('math').log2(p) for p in probabilities if p > 0)
    return round(entropy, 4)

def temporal_shift(sequence, steps=1):
    shifted = sequence[-steps:] + sequence[:-steps]
    reversal_test = shifted[::-1]
    # Unused transformed variant
    processed = [a ^ b for a, b in zip(shifted, reversal_test)]
    return shifted

def analyze_pattern(dataset, cfg):
    readings = dataset['data']
    base = dataset['baseline']
    
    # Multi-step transformation chain
    calibrated = apply_calibration(readings)
    adjusted = [int(x - base + cfg['offset']) for x in calibrated]
    
    # Bitwise manipulation layer (partially relevant)
    bit_encoded = [((x << 1) | 1) & 63 for x in adjusted]
    
    # Redundant statistical profiles
    profile_a = {
        'max': max(bit_encoded),
        'min': min(bit_encoded),
        'range': max(bit_encoded) - min(bit_encoded)
    }
    
    # Decoy structural analysis
    decoy_pairs = [(i, bit_encoded[i] & 7) for i in range(len(bit_encoded)) if i % 3 == 0]
    decoy_hash = sum(idx * val for idx, val in decoy_pairs) % 1000
    
    # Core logic: conditional masking based on config policy
    if cfg['policy'] == 'strict':
        screened = [x for x in bit_encoded if x > cfg['threshold']]
    else:
        screened = [x for x in bit_encoded if x >= cfg['threshold']]
    
    # Critical dependency: entropy influences final weight
    entropy = compute_entropy(screened)
    time_series = temporal_shift(screened, steps=cfg['shift'])
    
    # Final aggregation with weighted contribution
    raw_total = sum(time_series)
    adjustment_factor = 1 + (entropy / 10)
    final_score = int(raw_total * adjustment_factor)
    
    # Misleading secondary computation (dead end)
    phantom_chain = [final_score]
    for _ in range(3):
        phantom_chain.append((phantom_chain[-1] ^ 271) % 10000)
    
    # Key result
    final_diagnostic = final_score + cfg['bias']
    return final_diagnostic

# Orchestration block
if __name__ == '__main__':
    # Primary data ingestion
    sensor_package = collect_sensor_readings()
    
    # Configuration with plausible but partially unused parameters
    config = {
        'offset': 5,
        'threshold': 40,
        'shift': 1,
        'policy': 'relaxed',
        'bias': 17,
        'timeout': 300,
        'retries': 3
    }
    
    # Irrelevant pre-processing side task
    dummy_data = list(range(12, 24))
    combination_count = generate_combinations(dummy_data)
    scaled_combos = [x * 0.75 for x in [combination_count]]  # Unused
    
    # Signal transformation pipeline
    cleaned_signal, metrics = mask_outliers(sensor_package['data'], threshold_multiplier=1.9)
    enhanced = [x + 2 for x in cleaned_signal]
    
    # Structurally significant reformatting
    transformed_data = {
        'data': enhanced,
        'baseline': sensor_package['baseline'],
        'source': 'ARRAY_7B',
        'timestamp': '2023-10-05T14:22:00Z'
    }
    
    # Critical execution point
    final_diagnostic = analyze_pattern(transformed_data, config)
    
    # Output requirement
    print(f"Result: {final_diagnostic}")