import math

# Simulated sensor data processing system for environmental monitoring
raw_readings = [145, 203, 178, 211, 194, 256, 132, 187]

# Irrelevant calibration constants (distractors)
calibration_offset_a = 0.87
reference_threshold_x = 192.5
dummy_factor_k = 4.13
temporal_damping = 0.91
baseline_shift_z = 12.7

# Preprocessing: normalize readings using min-max scaling
def normalize(data):
    min_val, max_val = min(data), max(data)
    return [(x - min_val) / (max_val - min_val) for x in data]

scaled_data = normalize(raw_readings)

# Apply irrelevant transformation path (dead code path - not used later)
smoothed_data = []
for i in range(len(scaled_data)):
    weight = 0.5 if i == 0 else 0.3 if i == 1 else 0.2
    smoothed_data.append(scaled_data[i] * weight)

# Another decoy function with no actual usage
def apply_filter(signal, alpha=0.6):
    filtered = [signal[0]]
    for x in signal[1:]:
        filtered.append(alpha * x + (1 - alpha) * filtered[-1])
    return filtered

# Unused but plausible intermediate result
deceptive_median = sorted(scaled_data)[len(scaled_data)//2]

# Extract key features from normalized data
mean_level = sum(scaled_data) / len(scaled_data)
variance = sum((x - mean_level) ** 2 for x in scaled_data) / len(scaled_data)
std_dev = math.sqrt(variance)
peak_to_peak = max(scaled_data) - min(scaled_data)

# Derived metrics with meaningful names
metrics = {
    'stability': 1 / (std_dev + 0.1),
    'uniformity': 1 - variance,
    'dynamic_range': peak_to_peak,
    'consistency': sum(1 for x in scaled_data if abs(x - mean_level) < std_dev) / len(scaled_data)
}

# Weight configuration influenced by hypothetical standards
weights = {
    'stability': 0.4,
    'uniformity': 0.3,
    'dynamic_range': 0.2,
    'consistency': 0.1
}

# Red herring computation: entropy-like measure (unused)
pseudo_entropy = -sum(x * math.log(x + 1e-9) for x in scaled_data)
redundancy_index = 1 / (1 + pseudo_entropy)

# Bit manipulation decoy chain
bit_analysis = 0
for val in raw_readings:
    bit_analysis ^= int(val * 1.7) & 255
bit_analysis = (bit_analysis << 3) | (bit_analysis >> 5)
bit_analysis &= 0xFF

# Core evaluation logic using lambda abstraction
scoring_engine = lambda m, w: sum(m[key] * w.get(key, 0) for key in m)

# Auxiliary diagnostic trace (irrelevant to final score)
diagnostic_vector = [math.sin(x * 2 * math.pi) for x in scaled_data]
coherence_metric = abs(sum(diagnostic_vector)) / len(diagnostic_vector)

# Critical execution point
final_score = scoring_engine(metrics, weights)

# Additional distraction: recursive checksum (unused)
def calc_recursive_checksum(data, depth=0):
    if depth >= 3 or len(data) == 1:
        return data[0] % 7
    mid = len(data) // 2
    left = calc_recursive_checksum(data[:mid], depth + 1)
    right = calc_recursive_checksum(data[mid:], depth + 1)
    return (left ^ right) % 7

# Print target result
print(f"Result: {final_score}")