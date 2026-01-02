import itertools

# Simulate multi-sensor signal processing with noise filtering and pattern detection
def preprocess_signal(raw_data, threshold=0.1):
    filtered = []
    cumulative_drift = 0.0
    for val in raw_data:
        if abs(val) > threshold:
            adjusted = val - (cumulative_drift * 0.05)
            filtered.append(round(adjusted, 3))
            cumulative_drift += abs(adjusted) % 0.3
    return filtered

# Detect equilibrium state based on symmetric patterns in processed signal
def detect_equilibrium(signal_sequence):
    if len(signal_sequence) < 4:
        return -1
    
    # Generate sliding windows of size 4 to detect local symmetry
    windows = [signal_sequence[i:i+4] for i in range(len(signal_sequence) - 3)]
    symmetry_scores = []
    
    for window in windows:
        # Measure symmetry: |a + d - (b + c)| → lower means more balanced
        score = abs(window[0] + window[3] - (window[1] + window[2]))
        symmetry_scores.append(round(score, 4))
    
    # Use itertools to group consecutive low-symmetry regions
    grouped_blocks = []
    current_block = 0
    for s in symmetry_scores:
        if s < 0.5:
            current_block += 1
        else:
            if current_block > 0:
                grouped_blocks.append(current_block)
                current_block = 0
    if current_block > 0:
        grouped_blocks.append(current_block)
    
    avg_symmetry = sum(symmetry_scores) / len(symmetry_scores) if symmetry_scores else 0
    max_run = max(grouped_blocks) if grouped_blocks else 0
    
    # Final equilibrium score combines symmetry, length, and continuity
    base_score = int((1 / (avg_symmetry + 0.1)) * max_run)
    penalty = len([s for s in symmetry_scores if s > 1.0])
    return base_score - penalty

# Irrelevant helper: computes statistical moments (not used in final logic)
def compute_moments(data):
    n = len(data)
    if n == 0:
        return 0, 0, 0, 0
    mean = sum(data) / n
    variance = sum((x - mean) ** 2 for x in data) / n
    skewness = sum((x - mean) ** 3 for x in data) / (n * variance ** 1.5) if variance > 0 else 0
    kurtosis = sum((x - mean) ** 4 for x in data) / (n * variance ** 2) - 3 if variance > 0 else 0
    return mean, variance, skewness, kurtosis

# Secondary distraction: frequency analysis using modulo patterns
def analyze_frequency_pattern(seq):
    freq_modulo = {}
    for num in seq:
        mod_val = int(abs(num) * 10) % 7
        freq_modulo[mod_val] = freq_modulo.get(mod_val, 0) + 1
    total = sum(freq_modulo.values())
    entropy = 0
    for v in freq_modulo.values():
        p = v / total
        entropy -= p * (p).log() if p > 0 else 0
    return entropy

# Main execution block simulating sensor array input
raw_sensor_data = [
    0.05, -0.12, 0.33, 0.21, -0.18, -0.25, 0.31, 0.13,
    -0.11, 0.09, 0.27, -0.24, -0.13, 0.34, 0.22, -0.15
]

# Step 1: Filter and adjust raw signals
distorted_correction_factor = 0.03
processed_signals = preprocess_signal(raw_sensor_data, threshold=0.1)

# Distraction: unused transformation branch
if len(processed_signals) > 10:
    alternate_path = [x * 1.5 for x in processed_signals if x > 0.2]
else:
    temp_shadow = [abs(y) ** 0.5 for y in processed_signals]

# Step 2: Detect equilibrium from processed signal
equilibrium_score = detect_equilibrium(processed_signals)

# Dead code: hypothetical calibration chain (never invoked)
def calibrate_system(mode='passive'):
    return {"status": "simulated", "mode": mode}

# Unused intermediate summaries
decay_rate = sum(abs(x) for x in processed_signals) * 0.01
moment_analysis = compute_moments(processed_signals)
frequency_entropy = analyze_frequency_pattern(processed_signals)

# Output result as required
print(f"Result: {equilibrium_score}")