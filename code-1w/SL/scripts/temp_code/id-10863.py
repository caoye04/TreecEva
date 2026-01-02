from collections import defaultdict, Counter

# Simulated sensor array data with calibration routines
def calibrate_sensor(node_id, threshold=0.75):
    return (node_id * 1.87) % 1.0 > threshold

def generate_calibration_sequence(base_nodes):
    sequence = []
    for i in range(len(base_nodes)):
        if base_nodes[i] % 3 == 0:
            sequence.append((base_nodes[i] * 2) + 1)
        elif base_nodes[i] % 7 == 0:
            sequence.append(base_nodes[i] // 2)
        else:
            sequence.append(base_nodes[i] + (i % 4))
    return [x for x in sequence if x % 2 == 1]  # Only odd values retained

def compute_entropy(signal):
    total = sum(signal)
    if total == 0:
        return 0.0
    probabilities = [s / total for s in signal]
    entropy = -sum(p * (p ** 0.5) for p in probabilities if p > 0)
    return round(entropy, 6)

def validate_checksum(structure):
    checksum = 0
    for idx, val in enumerate(structure):
        checksum += val * (idx + 1)
    return checksum % 1007

def decoy_analysis_layer(data_stream):
    # Irrelevant recursive function - red herring
    if len(data_stream) <= 1:
        return data_stream
    mid = len(data_stream) // 2
    left = decoy_analysis_layer(data_stream[:mid])
    right = decoy_analysis_layer(data_stream[mid:])
    return left + [x * 0.9 for x in right]

def misdirection_transform(x):
    # Unused transformation - dead code path
    return (x ** 2 + 3 * x + 1) % 101

def auxiliary_debug_routine(log_entries):
    # Distractor: builds unused statistics
    stats = defaultdict(int)
    for entry in log_entries:
        stats['total'] += 1
        if entry > 50:
            stats['high'] += 1
        else:
            stats['low'] += 1
    return {k: v for k, v in stats.items() if v > 10}  # Unreachable condition

def extract_signatures(dataset):
    # Another distractor - no impact on final result
    signatures = []
    for item in dataset:
        sig = (item * 7 + 13) % 97
        if sig % 3 == 0:
            signatures.append(sig)
    return sorted(signatures, reverse=True)[:10]

def process_metrics(sequence, logs):
    # Core logic begins here
    temp_buffer = []
    for val in sequence:
        if val > 15:
            temp_buffer.append(val % 13)
        else:
            temp_buffer.append(val * 2)
    
    # Intermediate transformation
    transformed = [x for x in temp_buffer if x != 0]
    offset = len(transformed) // 4
    key_segment = transformed[offset:offset*3] if offset > 0 else transformed[:5]
    
    # Real computation: count frequency of certain patterns
    freq = Counter(key_segment)
    mode_value = max(freq, key=freq.get)
    
    # Secondary filter based on position
    indexed = list(enumerate(key_segment))
    filtered_pairs = [(i, v) for i, v in indexed if v % 2 == i % 2]
    
    # Accumulate diagnostic value
    accumulator = 0
    for pos, val in filtered_pairs:
        accumulator += (pos + 1) * val  # Weighted sum
    
    # Final adjustment using deterministic hash
    adjustment = 0
    for ch in 'diagnostics_active':
        adjustment += ord(ch)
    adjustment = (adjustment * 7) % 19
    
    final_diagnostic = accumulator - adjustment
    
    # Begin irrelevant operations (red herrings below)
    dummy_logs = [x * 0.5 for x in logs if x % 2 == 1]
    dummy_logs = [x for x in dummy_logs if calibrate_sensor(int(x))]
    entropy_score = compute_entropy(dummy_logs) if dummy_logs else 0.0
    
    decoy_result = decoy_analysis_layer([100, 200, 300, 400])
    debug_stats = auxiliary_debug_routine(logs)
    signatures = extract_signatures(sequence)
    validation = validate_checksum(sequence)
    
    # These variables are computed but never used in final_diagnostic
    phantom_threshold = sum(signatures) / len(signatures) if signatures else 0
    fallback_mode = any(v > 50 for v in debug_stats.values())
    noise_floor = entropy_score * validation / (phantom_threshold + 1)
    
    return final_diagnostic

# Main execution
if __name__ == '__main__':
    node_array = [12, 18, 21, 24, 33, 35, 42, 44, 51, 56, 63]
    telemetry_log = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
    
    calibration_sequence = generate_calibration_sequence(node_array)
    diagnostics_log = [x for x in telemetry_log if x % 5 == 0 and x > 20]
    
    final_diagnostic = process_metrics(calibration_sequence, diagnostics_log)
    
    print(f"Result: {final_diagnostic}")