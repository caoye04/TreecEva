from collections import defaultdict, Counter
import math

# Simulated sensor data acquisition (irrelevant preprocessing)
def acquire_sensor_feed():
    raw_stream = [0.88, 0.91, 0.85, 0.49, 0.51, 0.87, 0.90, 0.48, 0.52, 0.89]
    offset = 0.02
    corrected = [x + offset for x in raw_stream]
    return corrected

# Irrelevant noise modeling function (dead code path)
def generate_thermal_noise(level=3, seed=123):
    import random
    random.seed(seed)
    return [random.uniform(-level, level) for _ in range(10)]

# Signal envelope detection (partially relevant)
def detect_envelope(signal):
    envelope = []
    for i in range(1, len(signal) - 1):
        diff_prev = signal[i] - signal[i-1]
        diff_next = signal[i+1] - signal[i]
        if diff_prev > 0 and diff_next < 0:
            envelope.append(signal[i])
    return envelope

# Frequency binning (distractor logic)
def categorize_frequencies(magnitudes):
    bins = defaultdict(int)
    for mag in magnitudes:
        if mag < 0.5:
            bins['low'] += 1
        elif mag < 0.75:
            bins['medium'] += 1
        else:
            bins['high'] += 1
    return bins

# Core processing: extract peaks above threshold (relevant)
def extract_peaks(data, threshold=0.88):
    peaks = []
    for val in data:
        if val >= threshold:
            peaks.append(val)
    return peaks

# Recursive smoothing filter (relevant but with decoy parameters)
def smooth_recursive(values, alpha=0.3, depth=0, max_depth=2):
    if depth >= max_depth or len(values) == 0:
        return values
    smoothed = []
    for i in range(len(values)):
        weighted = values[i] * alpha
        if i > 0:
            weighted += smoothed[i-1] * (1 - alpha)
        else:
            weighted += values[0] * (1 - alpha)
        smoothed.append(round(weighted, 2))
    return smooth_recursive(smoothed, alpha, depth + 1, max_depth)

# Data normalization (irrelevant transformation)
def normalize_readings(readings):
    if not readings:
        return []
    min_val, max_val = min(readings), max(readings)
    if min_val == max_val:
        return [0.5] * len(readings)
    return [(x - min_val) / (max_val - min_val) for x in readings]

# Main analysis pipeline
sensor_data = acquire_sensor_feed()

# Apply irrelevant noise model (unused)
noise_profile = generate_thermal_noise(level=5)

# Detect signal envelope (used later)
envelope_points = detect_envelope(sensor_data)

# Normalize data (distractor, not used in final result)
normalized_data = normalize_readings(sensor_data)

# Extract high-magnitude events (critical step)
strong_peaks = extract_peaks(sensor_data, threshold=0.88)

# Apply recursive smoothing to peaks (relevant)
filtered_peaks = smooth_recursive(strong_peaks, alpha=0.4)

# Compute peak variance (red herring)
variance_proxy = 0
if filtered_peaks:
    mean_val = sum(filtered_peaks) / len(filtered_peaks)
    variance_proxy = sum((x - mean_val) ** 2 for x in filtered_peaks) / len(filtered_peaks)

# Categorize frequencies from envelope (distractor)
frequency_distribution = categorize_frequencies(envelope_points)

# Simulate diagnostic checksum (decoy logic)
def compute_checksum(values):
    total = 0
    for v in values:
        total ^= int(v * 100)
    return total % 17

checksum = compute_checksum(envelope_points)  # unused

# Process data through multiple transformations
working_data = filtered_peaks[:]

# Additional slicing manipulation (partially relevant)
working_data = working_data[::1]  # identity slice

# Bit manipulation decoy
bit_encoded = 0
for val in working_data:
    shifted = int(val * 10) << 2
    bit_encoded |= shifted

# Final processing stage
def analyze_signal(peaks):
    if not peaks:
        return -1
    
    # Use Counter to count rounded occurrences (key conceptual step)
    count_map = Counter([round(p, 1) for p in peaks])
    
    # Aggregate total weight (main contribution)
    total_weight = sum(p * count_map[round(p, 1)] for p in set(peaks))
    
    # Secondary adjustment based on count distribution
    mode_count = max(count_map.values())
    unique_peaks = len(count_map)
    
    # Tertiary influence: interaction term
    interaction_factor = (mode_count * unique_peaks) // max(1, len(peaks))
    
    # Final diagnostic score
    diagnostic_score = int((total_weight * 100) + interaction_factor)
    
    # Dead code branch
    if diagnostic_score < 0:
        backup = 0
        for i, p in enumerate(peaks):
            backup += int(p) ^ i
        diagnostic_score = backup
        
    return diagnostic_score

# Critical execution point
processed_data = working_data
final_diagnostic = analyze_signal(processed_data)
print(f"Result: {final_diagnostic}")