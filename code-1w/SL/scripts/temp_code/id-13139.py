import itertools

# Simulated sensor array diagnostics with interference
base_offsets = [0.1, -0.3, 0.4, 0.05]
signal_strengths = [85, 92, 78, 96, 88]
noise_floor = 0.07

def apply_calibration(raw_vals, factor=1.02):
    return [v * factor for v in raw_vals if v > 75]

def generate_combinations(data):
    # Distractor: generates unused combinatorial data
    return list(itertools.combinations(data, 3))

def shift_window(sequence, window_size=3):
    # Real use: used later in processing
    return [sum(sequence[i:i+window_size]) for i in range(len(sequence)-window_size+1)]

def filter_anomalies(readings):
    avg = sum(readings) / len(readings)
    return [r for r in readings if abs(r - avg) < 0.5]

def recursive_transform(seq, depth=0):
    if depth >= 3:
        return seq
    # Bit manipulation red herring
    transformed = [(int(x * 100) ^ 15) + depth for x in seq]
    return recursive_transform([t / 100.0 for t in transformed], depth + 1)

def compute_entropy(values):
    # Dead function - not used in main logic
    from math import log2
    total = sum(values)
    probs = [v / total for v in values]
    return -sum(p * log2(p) for p in probs if p > 0)

def extract_features(data_stream):
    # Mix of relevant and irrelevant operations
    windowed = shift_window(data_stream)
    enhanced = apply_calibration(windowed, factor=1.01)
    
    # Decoy conditional with misleading intermediate
    threshold_check = any(w > 250 for w in windowed)
    adjustment_factor = 0.9 if threshold_check else 1.1  # Unused
    
    # Actual transformation path
    features = [f * 1.05 for f in enhanced]
    return features

def detect_phase_shift(signal_list):
    # Irrelevant bit shifting operations
    shifted_bits = [(int(s) << 2) | 1 for s in signal_list]
    return sum(shifted_bits[:4]) % 100

def integrate_readings(signals):
    # Critical path: uses list comprehension and conditional expression
    calibrated = [s * 1.03 if s > 80 else s * 0.98 for s in signals]
    return sum(calibrated) / len(calibrated)

def analyze_readings(processed):
    # Final computation with distractors
    baseline = sum(processed) / len(processed)
    variance = sum((x - baseline) ** 2 for x in processed) / len(processed)
    peak = max(processed)
    
    # Red herring: complex but unused calculation
    cyclic_pattern = [(i, (peak * (i % 3)) ** 0.5) for i in range(5)]
    pattern_score = sum(t[1] for t in cyclic_pattern) if len(cyclic_pattern) > 3 else 0
    
    # Real answer computation
    diagnostic_value = baseline + (variance * 0.1) - 5
    return int(diagnostic_value * 10) / 10.0  # Rounded to 1 decimal

# Irrelevant global variables
system_mode = "diagnostic"
debug_trace = True
timestamp_log = [1623456789, 1623456849, 1623456909]

# Unused helper
def validate_checksum(data):
    return sum(data) % 256

# Main execution flow with decoy calls
raw_signals = [0.88, 0.76, 0.91, 0.83, 0.79]
processed_offsets = [abs(o) for o in base_offsets]
calibration_sequence = apply_calibration(signal_strengths)

# Generate unused combinatorial data (distractor)
combinations = generate_combinations(signal_strengths)

# Real signal processing begins
amplified = [s * 1.1 for s in raw_signals]
smoothed = shift_window([int(s*100)/100.0 for s in amplified])
filtered = filter_anomalies(smoothed)

# Recursive transformation applied
transformed_filtered = recursive_transform(filtered)

# Feature extraction (uses result)
extracted_features = extract_features(transformed_filtered)

# Integration step
integrated = integrate_readings(extracted_features)

# Final processing pipeline
intermediate_signals = [integrated * 1.02]
intermediate_signals.extend(transformed_filtered)
processed_signals = [min(max(sig, 0.5), 1.0) for sig in intermediate_signals]  # Clamp values

# Key statement
final_diagnostic = analyze_readings(processed_signals)

# Output result
print(f"Result: {final_diagnostic}")