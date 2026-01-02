import itertools

# Simulated sensor array diagnostics with noise filtering and pattern analysis
def collect_sensor_readings():
    raw_readings = [18, 22, 15, 30, 25, 40, 35, 50, 45]
    noise_mask = [i % 3 == 0 for i in range(len(raw_readings))]
    filtered = [r for i, r in enumerate(raw_readings) if not noise_mask[i]]
    baseline = sum(filtered[:3]) / len(filtered[:3])
    adjusted = [r - baseline + 5 for r in filtered]
    return adjusted

# Irrelevant auxiliary function - dead code path
def deprecated_normalization(x):
    return [val / max(x) for val in x]

# Signal transformation with bit manipulation red herring
def transform_signal(data):
    shifted = [val << 1 for val in data]  # Bit shift - looks important but unused
    wrapped = [val % 25 for val in data]
    return wrapped

# Misleading statistical summary (decoy)
def compute_misleading_stats(seq):
    mean = sum(seq) / len(seq)
    variance = sum((x - mean) ** 2 for x in seq) / len(seq)
    magic_offset = int(variance % 7)
    return mean * magic_offset

# Core pattern analyzer with conditional logic and set operations
def analyze_pattern(values, cfg):
    threshold = cfg['threshold']
    critical_set = {x for x in values if x > threshold}
    backup_list = [x for x in values if x <= threshold]
    
    if len(critical_set) >= cfg['min_critical']:
        attempt = list(itertools.combinations(critical_set, 2))
        if attempt:
            first_pair = attempt[0]
            score = abs(first_pair[0] - first_pair[1]) * len(attempt)
        else:
            score = len(critical_set)
    else:
        secondary_check = set(backup_list)
        score = sum(secondary_check) // (len(secondary_check) or 1)
    
    # Red herring: complex-looking but unused bitwise computation
    decoy_analysis = 0
    for i in range(len(values)):
        decoy_analysis ^= (values[i] & (i + 5)) | (score % 8)
    
    return score

# Unused recursive variant (distractor)
def recursive_peak_detect(arr, idx=0):
    if idx == len(arr) - 1:
        return [arr[idx]]
    rest = recursive_peak_detect(arr, idx + 1)
    return [arr[idx]] + rest if arr[idx] > arr[idx+1] else rest

# Configuration with misleading extra fields
def get_config():
    return {
        'threshold': 20,
        'min_critical': 3,
        'scaling_factor': 1.75,
        'debug_mode': False,
        'legacy_flag': 0xABC
    }

# Main execution flow with key intervention point
if __name__ == '__main__':
    readings = collect_sensor_readings()
    processed = transform_signal(readings)
    config = get_config()
    
    # Dead code assignment - irrelevant transformation
    normalized_readings = [round(x * config['scaling_factor'], 2) for x in readings]
    
    # Decoy statistical output
    fake_metric = compute_misleading_stats(processed)
    
    # Key statement containing answer
    final_diagnostic = analyze_pattern(processed, config)
    
    # Final result printing
    print(f"Result: {final_diagnostic}")