import math

def analyze_phase_coherence(readings):
    # Irrelevant signal processing function (dead code path)
    return sum(abs(r) for r in readings if r > 0.5)

def evaluate_stability_index(sequence):
    # Unused stability metric (distractor)
    return math.prod([s + 1 for s in sequence]) ** 0.3

def transform_sensor_input(raw):
    # Preprocess sensor values with normalization and filtering
    filtered = [max(0, x - 0.1) for x in raw]
    normalized = [x / (sum(filtered) + 1e-8) for x in filtered]
    return [round(x * 100) for x in normalized]

def compute_entropy(values):
    # Decoy entropy calculation (not used in final result)
    total = sum(values)
    if total == 0:
        return 0
    probs = [v / total for v in values]
    return -sum(p * math.log(p + 1e-9) for p in probs)

def validate_calibration(signal):
    # Red herring calibration check
    ref = sum(signal) % 7
    tolerance = 3.14159
    return ref > tolerance / 10

def aggregate_metrics(data, limits):
    # Core logic: multi-step reasoning across data transformations
    temp_series = []
    for i, entry in enumerate(data):
        scaled = []
        for j, val in enumerate(entry['readings']):
            if j % 2 == 0:
                scaled.append(val * 1.5)
            else:
                scaled.append(val * 0.8)
        
        # Apply transformation
        processed = transform_sensor_input(scaled)
        
        # Extract diagnostic features
        peak = max(processed)
        base = min(p for p in processed if p > 0)
        spread = peak - base
        
        # Hidden relevant computation: weighted index
        index = 0
        for k, p in enumerate(processed):
            weight = 1.1 if k % 3 == 0 else 0.9
            index += p * weight * (k + 1)
        
        temp_series.append(index)
    
    # Accumulate final metric using conditional weighting
    cumulative = 0
    for t_idx, measure in enumerate(temp_series):
        if measure > limits[t_idx % len(limits)]:
            cumulative += measure * 0.7
        else:
            cumulative += measure * 1.3
    
    # Final adjustment using bitwise manipulation (relevant step)
    raw_final = int(cumulative)
    masked = raw_final ^ 0xAA  # XOR with hex pattern
    shifted = (masked << 2) >> 1  # Left shift then right shift (asymmetric)
    adjusted = shifted + (shifted & 0xF)  # Add lower nibble
    
    # Key assignment - this is the answer
    final_diagnostic = adjusted - 500  # Offset to center result
    
    # Irrelevant post-processing (never executed due to return)
    if final_diagnostic < 0:
        final_diagnostic = abs(final_diagnostic)
    
    return final_diagnostic

# Simulated sensor input (real data driving computation)
sensor_data = [
    {'id': 'S1', 'readings': [0.4, 0.7, 0.3, 0.9, 0.6], 'type': 'primary'},
    {'id': 'S2', 'readings': [0.5, 0.2, 0.8, 0.4, 0.7], 'type': 'primary'},
    {'id': 'S3', 'readings': [0.6, 0.5, 0.4, 0.3, 0.8], 'type': 'secondary'},
    {'id': 'S4', 'readings': [0.3, 0.6, 0.7, 0.5, 0.4], 'type': 'secondary'}
]

# Threshold levels used in aggregation (critical for control flow)
thresholds = [120, 95, 110]

# Dead variables - misleading intermediate results
baseline_score = analyze_phase_coherence([r['readings'][0] for r in sensor_data])
stability = evaluate_stability_index([len(d['readings']) for d in sensor_data])
entropy_metric = compute_entropy([sum(d['readings']) for d in sensor_data])

calibration_ok = validate_calibration([0.1, 0.3, 0.2, 0.4])

# Main execution point - triggers the key statement
final_diagnostic = aggregate_metrics(sensor_data, thresholds)

# Output the target result
print(f"Target result: {final_diagnostic}")