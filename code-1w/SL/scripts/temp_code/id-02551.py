import math

# Simulated system telemetry and health monitoring with extensive red herrings
def analyze_signal_strength(signal):
    if not signal:
        return 0
    magnitude = sum([x ** 2 for x in signal])
    normalized = math.sqrt(magnitude)
    # Distractor: irrelevant frequency analysis
    freq_peaks = [i for i in range(len(signal)) if signal[i] > 0.7 * normalized]
    scaling_factor = 1.87  # Misleading constant
    return normalized * scaling_factor

# Legacy function - unused but looks important
def compute_legacy_checksum(buffer):
    checksum = 0
    for byte in buffer:
        checksum ^= (byte + 3) % 256
    return checksum

# Complex data transformation pipeline
def encode_payload(data):
    encoded = []
    for item in data:
        if item < 0:
            encoded.append(abs(item) << 2)
        elif item == 0:
            encoded.append(1)
        else:
            encoded.append(item >> 1)
    return encoded[::-1]  # Slicing distraction

# Real processing function with key logic buried
def evaluate_stability_index(telemetry):
    base_score = 0
    threshold_map = {k: v * 0.5 for k, v in enumerate([4, 8, 15, 16, 23, 42])}
    
    # Irrelevant preprocessing branch
    filtered_telemetry = [x for x in telemetry if x > 1]
    temp_results = []
    for idx, val in enumerate(telemetry):
        if idx % 2 == 0:
            temp_results.append(val ** 0.5)
        else:
            temp_results.append(val / 3.0)
    
    # Actual relevant computation buried here
    for i, x in enumerate(telemetry):
        adjustment = 1 if x > threshold_map.get(i % 6, 10) else -1
        base_score += adjustment * (x % 7)
    
    # Decoy aggregation
    dummy_agg = sum(temp_results) / len(temp_results) if temp_results else 0
    
    return int(base_score)

# Core diagnostic processor - answer derived here
def process_metrics(snapshot, state):
    # Key variable initialization
    diagnostic_weight = 0
    
    # Red herring: complex dictionary operations with unused results
    feature_map = {f'feat_{i}': math.log(abs(x) + 1) for i, x in enumerate(snapshot)}
    relevance_scores = {k: v * 0.3 + 2 for k, v in feature_map.items()}
    sorted_features = sorted(relevance_scores.items(), key=lambda x: x[1], reverse=True)
    top_contributors = sorted_features[:5]
    
    # Bit manipulation decoy
    bit_accumulator = 0
    for i in range(len(snapshot)):
        bit_accumulator ^= (i + 1) & snapshot[i % len(snapshot)]
    
    # Conditional execution path with early return red herring
    if len(snapshot) > 10:
        fallback = sum(snapshot) // len(snapshot)
        return fallback  # Dead code - condition never met
    
    # Real computation chain begins
    transformed = encode_payload(snapshot)
    stability = evaluate_stability_index(transformed)
    
    # Multi-step reasoning with lambda and slicing
    windowed = [transformed[i:i+3] for i in range(0, len(transformed)-2, 2)]
    integrator = lambda w: sum(w) * (1 if sum(w) > 10 else -1)
    integral = sum([integrator(win) for win in windowed])
    
    # Final composition
    diagnostic_weight += stability
    diagnostic_weight += abs(integral) // 4
    if state.get('active_redundancy', False):
        diagnostic_weight += 5
    
    # Critical assignment point
    final_diagnostic = diagnostic_weight * 2 - 3
    
    # More distractions
    metadata_log = {
        'version': '2.1.5',
        'checksum': bit_accumulator ^ 999,
        'features_analyzed': len(top_contributors)
    }
    
    return final_diagnostic

# Simulated input data
initial_buffer = [1, 2, 3, 4, 5, 6]
data_snapshot = [x ** 2 - x for x in initial_buffer]  # [0, 2, 6, 12, 20, 30]
system_state = {
    'status': 'nominal',
    'timestamp': 1712345678,
    'active_redundancy': True,
    'mode': 'diagnostic'
}

# Signal analysis - irrelevant to final result
clean_signal = [0.1, 0.8, 1.2, 0.9, 0.3]
signal_score = analyze_signal_strength(clean_signal)

# Checksum calculation - dead end
dummy_buffer = [10, 20, 30, 40]
legacy_checksum = compute_legacy_checksum(dummy_buffer)

# Main execution flow
intermediate_result = evaluate_stability_index(data_snapshot)
final_diagnostic = process_metrics(data_snapshot, system_state)

print(f"Target result: {final_diagnostic}")