import math

# Simulated sensor fusion system for environmental monitoring
def acquire_raw_data():
    raw_sequence = [i**2 + 3*i - 7 for i in range(15)]
    offset_compensation = sum(raw_sequence) % 11
    normalized = [x - offset_compensation for x in raw_sequence]
    return normalized

def filter_outliers(data, threshold=2.5):
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    std_dev = math.sqrt(variance)
    filtered = [x for x in data if abs(x - mean_val) <= threshold * std_dev]
    return filtered

def generate_lookup(keys):
    # Distractor: complex dictionary generation with unused mappings
    base_map = {k: (k * 11) % 17 for k in keys}
    extended = {k: (base_map[k] ** 2) % 19 for k in base_map}
    meta_info = {'version': '2.1', 'active': True, 'mode': 'diagnostic'}
    if meta_info['version'] == '2.1':
        extended.update({k + 100: k for k in base_map})
    return base_map  # Misleading: returns base_map instead of extended

def transform_signal(values):
    # Apply FFT-like transformation (simplified)
    transformed = []
    n = len(values)
    for k in range(n):
        real_part = sum(values[i] * math.cos(2 * math.pi * k * i / n) for i in range(n))
        imag_part = sum(-values[i] * math.sin(2 * math.pi * k * i / n) for i in range(n))
        magnitude = math.sqrt(real_part**2 + imag_part**2)
        transformed.append(round(magnitude, 3))
    return transformed

def slice_window(data, window_size=7):
    # Overlapping window slicing with string-based labeling (uses slicing and string methods)
    labels = [f'win_{i:02d}' for i in range(len(data) - window_size + 1)]
    windows = [data[i:i+window_size] for i in range(len(data) - window_size + 1)]
    labeled_windows = {labels[i]: windows[i] for i in range(len(labels))}
    return labeled_windows

def integrate_phase_shift(signal_parts):
    # Distractor function: looks important but not used in final path
    adjusted = []
    for label, values in signal_parts.items():
        shift = len(label) % 4
        rolled = values[-shift:] + values[:-shift] if shift else values
        adjusted.append(sum(rolled))
    return adjusted

def compute_entropy(arr):
    # Unused statistical analysis (dead code path)
    counts = {}
    for x in arr:
        counts[x] = counts.get(x, 0) + 1
    probs = [count / len(arr) for count in counts.values()]
    entropy = -sum(p * math.log2(p) for p in probs)
    return round(entropy, 4)

def reconstruct_timeline(segments):
    # Another decoy function with dictionary operations
    timeline = {}
    for key, segment in segments.items():
        index = int(key.split('_')[1])
        timeline[index] = sum(segment) * (index % 3 + 1)
    ordered = [timeline[k] for k in sorted(timeline.keys())]
    return ordered

def analyze_readings(spectrum):
    # Core analysis: find dominant harmonic via peak detection
    peak_index = 0
    peak_value = spectrum[0]
    for i in range(1, len(spectrum)):
        if spectrum[i] > peak_value:
            peak_value = spectrum[i]
            peak_index = i
    
    # Secondary metric: cumulative energy in first half
    mid = len(spectrum) // 2
    energy = sum(x**2 for x in spectrum[:mid])
    
    # Final diagnostic score: weighted combination
    diagnostic_score = (peak_index * 1000) + (energy / 100)
    return int(diagnostic_score)

def auxiliary_validation(test_data):
    # Bit manipulation red herring
    checksum = 0
    for val in test_data:
        temp = (val ^ 255) & 0xFF
n        checksum = (checksum << 1 | (checksum >> 7)) & 0xFF
    return checksum

def main_pipeline():
    # Step 1: Acquire and clean raw sensor data
    raw_signals = acquire_raw_data()
    cleaned_signals = filter_outliers(raw_signals)
    
    # Step 2: Generate irrelevant lookup (distractor)
    indices = [1, 3, 5, 7, 9]
    lookup_table = generate_lookup(indices)  # Not used later
    
    # Step 3: Transform to frequency domain
    processed_signals = transform_signal(cleaned_signals)
    
    # Step 4: Create windowed slices (used only partially)
    windowed_data = slice_window(processed_signals, 5)
    
    # Step 5: Reconstruct timeline from slices (dead end)
    dummy_timeline = reconstruct_timeline(windowed_data)
    
    # Step 6: Attempt phase integration (unused)
    dummy_shifted = integrate_phase_shift(windowed_data)
    
    # Step 7: Compute entropy (red herring statistic)
    _ = compute_entropy([int(x) for x in processed_signals if x > 10])
    
    # Step 8: Validate with auxiliary checksum (irrelevant)
    _ = auxiliary_validation([int(x) for x in processed_signals])
    
    # Step 9: Core diagnostic analysis (this is the critical path)
    final_diagnostic = analyze_readings(processed_signals)
    
    # Print result as required
    print(f"Target result: {final_diagnostic}")
    return final_diagnostic

# Execute main logic
result = main_pipeline()