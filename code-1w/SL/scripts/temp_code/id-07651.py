import math

def analyze_signal(data, threshold=0.5):
    magnitude = sum(x ** 2 for x in data) ** 0.5
    normalized = [x / magnitude for x in data]
    peaks = [i for i, x in enumerate(normalized) if x > threshold]
    return peaks if len(peaks) > 0 else [0]


def compute_checksum(sequence):
    # Irrelevant checksum computation (dead-end)
    chk = 0
    for s in sequence:
        chk ^= hash(str(s)) % 256
    return chk

# Simulated sensor readings (irrelevant data generation)
sensor_ids = ['S1', 'S2', 'S3']
raw_data = {
    'S1': [0.1, 0.4, 0.8, 0.3],
    'S2': [0.2, 0.6, 0.7, 0.5],
    'S3': [0.3, 0.9, 0.4, 0.2]
}

# Misleading preprocessing path (unused)
preprocessed = {}
for sid, readings in raw_data.items():
    filtered = [x for x in readings if x > 0.25]
    smoothed = [filtered[i] * 0.7 + (filtered[i-1] * 0.3 if i > 0 else 0) for i in range(len(filtered))]
    preprocessed[sid] = smoothed

# Actual relevant diagnostics
diagnostics = {
    'baseline_stability': 86,
    'phase_coherence': 44,
    'harmonic_distortion': 12,
    'noise_floor': 68,
    'signal_clarity': 52
}

# Distractor: irrelevant weight map (not used)
weight_map = {
    'W1': 0.8, 'W2': 1.2, 'W3': 0.9
}

# Correct weights used in calculation
weights = {
    'baseline_stability': 1.0,
    'phase_coherence': 0.75,
    'harmonic_distortion': -0.5,  # Penalty factor
    'noise_floor': -0.25,
    'signal_clarity': 0.6
}

# Dead function - looks important but unused
def evaluate_integrity(values):
    total = 0
    for v in values:
        if v > 50:
            total += math.log(v)
        else:
            total -= v / 10
    return round(total, 2)

# Auxiliary transformation with red herring output
def transform_metric(x, mode='A'):
    if mode == 'A':
        return (x ** 1.05) // 1
    elif mode == 'B':
        return int(math.sqrt(x) * 10)
    else:
        return x

# Complex conditional expression (used)
adjusted_clarity = 70 if diagnostics['signal_clarity'] >= 50 else 40

# Bitwise obfuscation of a constant (distractor)
secret_key = (0xABCD ^ 0x1234) & 0xFFFF  # Result: 0xBBF9
key_interpretation = secret_key >> 4

# Main processing function
def process_metrics(metrics, w):
    temp_results = {}
    
    # Step 1: Apply weights
    for k, v in metrics.items():
        if k in w:
            temp_results[k] = v * w[k]
    
    # Step 2: Aggregate with conditional adjustment
    base_sum = sum(temp_results.values())
    
    # Step 3: Apply non-linear correction based on harmonic distortion impact
    distortion_level = metrics['harmonic_distortion']
    if distortion_level > 10:
        base_sum *= 0.9  # 10% penalty
    
    # Step 4: Round to nearest integer
    intermediate = int(round(base_sum))
    
    # Step 5: Adjust by phase coherence threshold logic
    coherence = metrics['phase_coherence']
    bonus = 5 if coherence >= 40 and intermediate > 50 else 0
    intermediate += bonus
    
    # Step 6: Final clamp between 0 and 100
    final_score = max(0, min(100, intermediate))
    
    # Step 7: Diagnostic override check (never triggered - dead logic)
    if final_score == 99:
        # This block is unreachable given current inputs
        final_score = hash('override') % 10
    
    # Step 8: Add fixed offset from bitwise result (not actually used)
    # Note: key_interpretation is computed above but not used here
    
    return final_score

# Execute critical statement
final_diagnostic = process_metrics(diagnostics, weights)

# Print result as required
print(f"Target result: {final_diagnostic}")