import math

# Simulated quantum sensor array diagnostics with signal transformation and noise filtering
def collect_readings():
    raw_values = [0.7, 1.2, -0.3, 4.5, 2.1, -1.0, 3.3]
    baseline = 1.5
    adjusted = [round(v * 1.05 - baseline, 3) for v in raw_values]
    return adjusted

# Irrelevant auxiliary function – dead code path (distractor)
def legacy_calibrate(x):
    return (x + 0.5) ** 2 if x < 0 else x * 0.9

# Signal classification based on amplitude bands (unused in final logic)
def classify_band(value):
    if value < -1.0:
        return 'LOW_NOISE'
    elif value < 0:
        return 'BACKGROUND'
    elif value < 1.0:
        return 'NORMAL'
    else:
        return 'HIGH_SIGNAL'

# Unused transformation chain (misleading intermediate steps)
def apply_filter(signal_list):
    filtered = []
    for s in signal_list:
        temp = s * s
        if temp > 2.0:
            temp = math.sqrt(temp)
        filtered.append(round(temp, 3))
    return filtered

# Complex multi-step transformation with decoy operations
def transform_signal(readings):
    # Step 1: Amplify and phase-shift relevant signals
    amplified = [r * 2.1 for r in readings]
    
    # Step 2: Apply conditional inversion based on parity index
    processed = []
    for i, val in enumerate(amplified):
        if i % 2 == 0:
            processed.append(-val if val > 0 else abs(val))
        else:
            processed.append(val)
    
    # Step 3: Normalize using moving average (distractor computation)
    window_size = 3
    moving_avg = []
    for j in range(len(processed) - window_size + 1):
        avg = sum(processed[j:j+window_size]) / window_size
        moving_avg.append(round(avg, 3))
    
    # Step 4: Extract oscillation pattern via sign transitions (ACTUAL critical logic)
    signs = [1 if x >= 0 else -1 for x in processed]
    transitions = 0
    for k in range(1, len(signs)):
        if signs[k] != signs[k-1]:
            transitions += 1
    
    # Return both transformed data AND transition count (latter is key)
    return processed, transitions

# Higher-order analysis with red herring parameters
def evaluate_stability(metrics, threshold=0.85, tolerance=0.1, mode='strict'):
    # This function is called but its result ignored (distractor)
    valid_count = sum(1 for m in metrics if abs(m) > threshold)
    ratio = valid_count / len(metrics)
    stable = ratio > (1 - tolerance) if mode == 'strict' else ratio >= 0.7
    return stable, ratio

# Core diagnostic engine - combines multiple concepts
def analyze_pattern(data_packet):
    # Unpack transformed data and transition metric
    transformed_readings, flip_count = data_packet
    
    # Decoy list comprehension - computes magnitude clusters (unused)
    magnitude_groups = {
        'high': [x for x in transformed_readings if abs(x) > 2.0],
        'medium': [x for x in transformed_readings if 1.0 <= abs(x) <= 2.0],
        'low': [x for x in transformed_readings if abs(x) < 1.0]
    }
    
    # Secondary decoy: bit manipulation on indices (irrelevant)
    index_fingerprint = 0
    for idx in range(len(transformed_readings)):
        index_fingerprint ^= (idx << 1) | (idx & 1)
    
    # ACTUAL decision logic: depends only on flip_count from transform_signal
    if flip_count > 4:
        diagnostic_score = 867
    elif flip_count == 4:
        diagnostic_score = 442
    else:
        diagnostic_score = 123 + flip_count * 15
    
    # Additional misleading calculation (never used)
    entropy_approx = 0.0
    for x in transformed_readings:
        if x != 0:
            entropy_approx += abs(math.log(abs(x)))
    
    return diagnostic_score

# Main execution flow
if __name__ == "__main__":
    # Step 1: Collect raw sensor data
    readings = collect_readings()
    
    # Step 2: Transform signal with multiple side computations
    transformation_output = transform_signal(readings)
    
    # Step 3: Apply legacy calibration (result discarded - red herring)
    _ = [legacy_calibrate(x) for x in readings]
    
    # Step 4: Perform stability evaluation (result ignored - distractor call)
    _ = evaluate_stability(transformation_output[0], mode='relaxed')
    
    # Step 5: Analyze pattern to produce final diagnostic
    final_diagnostic = analyze_pattern(transformation_output)
    
    # Output target result
    print(f"Target result: {final_diagnostic}")