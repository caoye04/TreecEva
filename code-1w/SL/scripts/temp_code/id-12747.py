import math

# Simulated sensor data and calibration constants (some are decoys)
sensor_readings = [0.88, -1.22, 3.14, 2.71, -0.55, 1.41, -2.3, 0.693]
baseline_offset = 0.13
noise_floor = 0.05
dummy_threshold = 1.5  # unused red herring
calibration_map = {'a': 0.95, 'b': 1.05, 'c': 1.1}  # irrelevant mapping

# Irrelevant preprocessing: dummy transformations
shifted_values = [x + baseline_offset for x in sensor_readings]
scaled_values = [x * 1.02 for x in shifted_values]  # distractor path

# Real signal processing begins
filtered_data = [x for x in sensor_readings if abs(x) > noise_floor]
adjusted_data = [round(x - baseline_offset, 3) for x in filtered_data]

# Bit manipulation for checksum (red herring section)
def compute_legacy_checksum(arr):
    result = 0
    for val in arr:
        bits = int(abs(val * 100)) & 0xFF
        result ^= bits
    return result + 1000  # never used in final logic

legacy_checksum = compute_legacy_checksum(sensor_readings)  # dead assignment

# Signal categorization with early termination
def categorize_amplitude(x):
    if x < -1.0:
        return 'LOW'
    elif x > 2.0:
        return 'HIGH'
    else:
        return 'MID'

# Apply categorization
amplitude_classes = [categorize_amplitude(x) for x in adjusted_data]

# Misleading statistical block
def compute_entropy(arr):
    from collections import Counter
    counts = Counter(arr)
    total = len(arr)
    entropy = -sum((count / total) * math.log2(count / total) for count in counts.values())
    return entropy

entropy_score = compute_entropy(amplitude_classes)  # computed but unused

# Core transformation: frequency domain simulation (simplified)
def simulate_frequency_response(data):
    transformed = []
    for i, val in enumerate(data):
        phase_shifted = val * math.cos(math.pi * i / 4)
        amplitude_mod = phase_shifted * (1 + 0.1 * (i % 3))
        transformed.append(round(amplitude_mod, 4))
    return transformed

frequency_data = simulate_frequency_response(adjusted_data)

# Secondary filter based on index parity (relevant)
even_indexed = [v for i, v in enumerate(frequency_data) if i % 2 == 0]
odd_indexed = [v for i, v in enumerate(frequency_data) if i % 2 == 1]  # unused

# Energy aggregation
energy_primary = sum([x**2 for x in even_indexed])
energy_secondary = sum([x**2 for x in odd_indexed])  # calculated but not critical

# Data normalization and thresholding
def normalize_and_clip(arr, limit=3.0):
    norm_factor = math.sqrt(sum([x**2 for x in arr])) or 1.0
    normalized = [x / norm_factor for x in arr]
    clipped = [max(-limit, min(limit, x)) for x in normalized]
    return clipped

processed_data = normalize_and_clip(even_indexed)

# Final diagnostic engine
def analyze_signal(signal):
    if not signal:
        return -1
    
    # Compute weighted center of mass in signal
    weighted_sum = sum(i * x for i, x in enumerate(signal))
    total_weight = sum(signal) or 1.0
    centroid = weighted_sum / total_weight
    
    # Apply corrective bias based on length
    length_bias = len(signal) * 0.05
    adjusted_centroid = centroid + length_bias
    
    # Final nonlinear transformation
    if adjusted_centroid != 0:
        result = math.log(abs(adjusted_centroid)) * 100
    else:
        result = 0
    
    return round(result, 4)

final_diagnostic = analyze_signal(processed_data)
print(f"Target result: {final_diagnostic}")