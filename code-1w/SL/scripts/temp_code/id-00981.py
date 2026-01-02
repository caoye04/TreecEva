import itertools

# Simulated sensor data from a distributed monitoring system
def generate_sensor_readings():
    base_values = [18.5, 22.3, 19.0, 24.1, 20.8]
    variations = [0.1 * i for i in range(5)]
    return [round(base + var, 2) for base, var in zip(base_values, variations)]

# Irrelevant transformation - looks useful but not used in final computation
def encrypt_signal(data):
    return [int(x * 17) ^ 0xFF for x in data]

# Decoy function - never called but looks important
def compute_entropy(seq):
    from math import log
    freq = {}
    for item in seq:
        freq[item] = freq.get(item, 0) + 1
    total = len(seq)
    entropy = -sum((count / total) * log(count / total) for count in freq.values())
    return round(entropy, 4)

# Another red herring: checksum that's defined but unused
def calculate_checksum(arr):
    chk = 0
    for val in arr:
        chk = (chk + int(val * 10)) & 0xFFFF
    return chk ^ 0xAAAA

# Data normalization with distraction paths
def normalize_readings(raw_readings, mode='z-score'):
    if mode == 'min-max':
        min_val, max_val = min(raw_readings), max(raw_readings)
        return [(x - min_val) / (max_val - min_val) for x in raw_readings]
    elif mode == 'z-score':
        mean = sum(raw_readings) / len(raw_readings)
        variance = sum((x - mean) ** 2 for x in raw_readings) / len(raw_readings)
        std_dev = variance ** 0.5
        return [(x - mean) / std_dev for x in raw_readings]
    else:
        return raw_readings  # no-op fallback

# Complex transformation involving list comprehensions and itertools
def transform_readings(normalized):
    # Apply windowed differencing using itertools
    paired = list(itertools.pairwise(normalized))
    diffs = [round(b - a, 3) for a, b in paired]
    
    # Mirror extension (distraction operation)
    mirrored_diffs = diffs + diffs[::-1]
    
    # Use set operations to filter unique magnitudes (some distraction here)
    abs_diffs = [abs(d) for d in diffs]
    unique_abs = sorted(set(abs_diffs))
    threshold = 0.35
    significant_changes = [d for d in diffs if abs(d) > threshold]
    
    # This looks like it does something important but isn't used later
    change_clusters = []
    current_cluster = []
    for d in significant_changes:
        if not current_cluster or abs(d - current_cluster[-1]) < 0.5:
            current_cluster.append(d)
        else:
            if len(current_cluster) > 1:
                change_clusters.append(current_cluster)
            current_cluster = [d]
    if current_cluster:
        change_clusters.append(current_cluster)
    
    # Actual relevant output: sum of absolute differences above threshold
    magnitude_score = sum(abs(d) for d in significant_changes)
    
    # Return includes irrelevant components
    return {
        'raw_diffs': diffs,
        'magnitude_score': magnitude_score,
        'cluster_count': len(change_clusters),
        'mirror_length': len(mirrored_diffs)
    }

# Threshold logic with conditional expressions
threshold_map = {
    'critical': 2.5,
    'warning': 1.0,
    'info': 0.2
}

# Core processing function with multiple concepts
def process_metrics(metrics_dict, thresholds):
    score = metrics_dict['magnitude_score']
    
    # Unused diagnostic path
    diagnostics = {}
    diagnostics['peak'] = max(metrics_dict['raw_diffs'], default=0)
    diagnostics['stability'] = 'high' if len(metrics_dict['raw_diffs']) < 3 else 'variable'
    diagnostics['mirrored'] = metrics_dict['mirror_length'] > 10
    
    # Real logic path buried in distractions
    level = (
        'critical' if score > thresholds['critical'] else
        'warning' if score > thresholds['warning'] else
        'info'
    )
    
    # Bit manipulation decoy
    encoded_level = 0
    if level == 'critical':
        encoded_level = 0b1101
    elif level == 'warning':
        encoded_level = 0b1010
    else:
        encoded_level = 0b0001
    
    # Final result computed using correct path
    adjustment = 3 if metrics_dict['cluster_count'] > 2 else 2
    base_value = int(score * 100)
    final_diagnostic = base_value + adjustment  # Key result
    
    # Dead code branch - never executed but looks active
    debug_payload = []
    for k, v in diagnostics.items():
        if isinstance(v, bool):
            debug_payload.append(f"{k}:{'T' if v else 'F'}")
    
    return final_diagnostic

# Main execution flow
if __name__ == '__main__':
    # Generate initial data
    raw_sensor_data = generate_sensor_readings()
    
    # Normalize using z-score (relevant)
    processed_readings = normalize_readings(raw_sensor_data, mode='z-score')
    
    # Transform readings - produces dict with several fields
    transformed_data = transform_readings(processed_readings)
    
    # These variables look important but are unused in final calculation
    encrypted_stream = encrypt_signal(raw_sensor_data)
    data_checksum = calculate_checksum([int(x * 100) for x in raw_sensor_data])
    
    # The key statement that determines the answer
    final_diagnostic = process_metrics(transformed_data, threshold_map)
    
    # Print result as required
    print(f"Target result: {final_diagnostic}")