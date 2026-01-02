from collections import defaultdict, Counter

# Simulated sensor data processing with diagnostic analysis
def preprocess_signal(raw_samples):
    filtered = [x for x in raw_samples if abs(x) > 0.1]
    normalized = [round(x / max(filtered), 3) for x in filtered]
    return normalized

# Irrelevant helper: computes statistical moments (not used in final result)
def compute_moments(data):
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    skewness = sum((x - mean_val) ** 3 for x in data) / (len(data) * variance ** 1.5)
    return (mean_val, variance, skewness)

# Distraction function: frequency analysis with unused transforms
def spectral_analysis(signal):
    transformed = []
    for i in range(len(signal)):
        acc = 0
        for j in range(8):  # Simulate DFT-like computation
            angle = i * j * 3.14159 / 4
            acc += signal[i] * (2 if j % 2 == 0 else 0.5) * (1 if (j//2) % 2 == 0 else -1)
        transformed.append(round(acc, 3))
    magnitude = [abs(x) for x in transformed]
    peak_freq = magnitude.index(max(magnitude)) if magnitude else 0
    return peak_freq  # Never actually used

# Core logic: pattern matching with bit-flagged states
def detect_anomaly_pattern(seq):
    state_flags = 0
    transitions = 0
    for i in range(1, len(seq)):
        delta = seq[i] - seq[i-1]
        if delta > 0.3:
            state_flags |= 1  # Set bit 0
            transitions += 1
        elif delta < -0.3:
            state_flags ^= 2  # Toggle bit 1
            transitions += 1
        if i % 7 == 0:
            state_flags |= 4  # Artificial periodic flag (red herring)
    return state_flags & 3, transitions  # Mask out artificial bits

# Calibration-sensitive analyzer
def analyze_signal(pattern, calib):
    # Misleading unpacking and unused assignments
    (*_, last_sample), (first_calib, *rest_calib) = pattern, calib
    
    # Dead code path: complex sorting that isn't used
    sorted_calib = sorted(rest_calib, key=lambda x: -x)
    rank_map = {val: idx for idx, val in enumerate(sorted_calib)}
    
    # Actual relevant computation begins here
    base_score = int(abs(last_sample) * 100)
    adjustment = first_calib * 2
    
    # Conditional expression based on pattern characteristics
    anomaly_code, steps = detect_anomaly_pattern(pattern)
    modifier = 3 if anomaly_code == 3 and steps > 2 else (-2 if anomaly_code == 0 else 1)
    
    # Bitwise combination
    intermediate = (base_score ^ adjustment) & 0xFFFF
    final_value = (intermediate + modifier) & 0x7FFF
    
    # Decoy operation (no effect due to masking above)
    if final_value > 10000:
        final_value = final_value >> 4
    
    return final_value

# Irrelevant global counters (distractors)
counter_A = Counter()
counter_B = defaultdict(int)
for k in ['X', 'Y', 'Z']:
    counter_A[k] = len(k) * 10
counter_B['temp'] += 5

data_stream = [-0.2, 0.5, 0.9, 0.3, -0.7, -0.8, 0.1, 0.6, 0.7]
calibration_vector = [0.45, 0.33, 0.22, 0.55, 0.11]

# Unused intermediate results
denoised = preprocess_signal(data_stream)
# _ = compute_moments(denoised)
# _ = spectral_analysis(denoised)

# Critical execution point
pattern_buffer = [round(x, 2) for x in denoised if x != 0.1]
calibration_data = [int(x * 100) for x in calibration_vector]
final_diagnostic = analyze_signal(pattern_buffer, calibration_data)

print(f"Result: {final_diagnostic}")