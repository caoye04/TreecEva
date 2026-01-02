from collections import defaultdict, Counter
import math

# Simulated sensor data from multiple sources
telemetry_stream = [
    [1.2, 0.8, 1.5, 2.3, 1.1],
    [0.9, 1.0, 1.6, 2.1, 1.3],
    [1.3, 1.7, 2.5, 2.4, 1.2],
    [0.7, 0.5, 1.8, 2.6, 1.4]
]

# Irrelevant baseline calibration (red herring)
calibration_offsets = [0.1, -0.05, 0.2, 0.0, 0.15]
adjusted_offsets = [math.sin(x) * 0.01 for x in range(len(calibration_offsets))]

# Misleading data transformation path (dead code)
def legacy_normalize(data):
    mean_val = sum(data) / len(data)
    return [(x - mean_val) * 0.9 for x in data]

# Unused recursive function (distractor)
def calculate_entropy_recursive(seq, depth=0):
    if depth > 5 or len(seq) == 0:
        return 0.0
    p = len([x for x in seq if x > 1.0]) / len(seq)
    if p == 0 or p == 1:
        return 0
    return -p * math.log(p) + calculate_entropy_recursive(seq[1:], depth + 1)

# Real processing begins here
aggregated_readings = []
for sequence in telemetry_stream:
    # Apply actual offset (not calibration_offsets!)
    corrected = [x * 1.05 for x in sequence]
    aggregated_readings.extend(corrected)

# Compute statistical profile (partially relevant)
mean_signal = sum(aggregated_readings) / len(aggregated_readings)
variance = sum((x - mean_signal) ** 2 for x in aggregated_readings) / len(aggregated_readings)
std_dev = math.sqrt(variance)

# Generate outlier mask using z-scores
z_scores = [(x - mean_signal) / std_dev for x in aggregated_readings]
outlier_mask = [abs(z) > 2.0 for z in z_scores]

# Distractor: unused frequency analysis
frequencies = defaultdict(int)
for val in aggregated_readings:
    bucket = int(round(val * 2))  # bin by half-unit
    frequencies[bucket] += 1
frequency_counter = Counter(frequencies)

# Threshold configuration map (critical)
threshold_map = {
    'low': mean_signal - std_dev,
    'high': mean_signal + std_dev * 1.5,
    'critical': mean_signal + std_dev * 2.2
}

# Signal state classification with bit flags (mix of concepts)
state_flags = []
for i, val in enumerate(aggregated_readings):
    flag = 0
    if val < threshold_map['low']:
        flag |= 1  # under threshold
    if val > threshold_map['high']:
        flag |= 2  # over high
    if val > threshold_map['critical']:
        flag |= 4  # critical overload
    if outlier_mask[i]:
        flag |= 8  # identified as outlier
    state_flags.append(flag)

# Processed data structure (tuple unpacking and assignment)
processed_data = list(zip(aggregated_readings, state_flags, z_scores))

# Decoy function that looks important but isn't used
def generate_diagnostic_report(data, config):
    total_flags = sum(flag for _, flag, _ in data)
    max_z = max(abs(z) for _, _, z in data)
    return {'total_flags': total_flags, 'max_z_score': max_z, 'size': len(data)}

# Core analysis function with multiple logic layers
def analyze_signal(signal_data, thresholds):
    # Count occurrences by category
    category_count = defaultdict(int)
    magnitude_sum = 0.0
    
    for value, flag, z in signal_data:
        # Relevant filtering logic
        if flag & 2:  # High threshold exceeded
            magnitude_sum += value
            
        # Complex conditional categorization
        if flag & 4 and not (flag & 1):  # Critical but not low
            category_count['severe'] += 1
        elif flag & 2 and z > 0:
            category_count['elevated'] += 1
        elif value > thresholds['low'] and abs(z) < 1.5:
            category_count['stable'] += 1

    # Bit manipulation for status encoding
    encoded_status = 0
    for count in category_count.values():
        encoded_status ^= (count * 3)  # XOR accumulation
    
    # Final diagnostic computation chain
    base_score = magnitude_sum * 100
    adjustment_factor = abs(category_count['severe'] - category_count['elevated'])
    if adjustment_factor > 0:
        adjustment_factor = math.log(adjustment_factor + 1)
    else:
        adjustment_factor = 0.5
    
    # Key calculation
    intermediate = base_score / (1 + adjustment_factor)
    final_value = int(intermediate) ^ encoded_status  # Mix arithmetic and bitwise
    
    # Dead code branch (never reached due to structure)
    if False:
        backup = sum(category_count.values()) * 1000
        final_value = backup if backup > final_value else final_value
    
    return final_value

# Execute main analysis
temp_var = analyze_signal(processed_data[:2], threshold_map)  # Unused call (misleading)
final_diagnostic = analyze_signal(processed_data, threshold_map)

print(f"Result: {final_diagnostic}")