from collections import defaultdict
import math

# Simulate a data processing pipeline for sensor signal analysis with distractions
def analyze_sensor_readings(raw_data):
    readings_log = defaultdict(int)
    temp_accumulator = 0
    peak_magnitude = 0

    for val in raw_data:
        readings_log[val] += 1
        temp_accumulator += abs(val)
        if abs(val) > peak_magnitude:
            peak_magnitude = abs(val)

    normalized_score = temp_accumulator / len(raw_data)
    return normalized_score, readings_log

# Misleading helper: appears useful but not used in critical path
def compute_entropy(data):
    freq_map = defaultdict(float)
    total = len(data)
    for item in data:
        freq_map[item] += 1.0
    entropy = 0.0
    for v in freq_map.values():
        p = v / total
        entropy -= p * math.log2(p)
    return entropy

# Core transformation chain
transform_pipeline = [
    lambda x: x ** 2,
    lambda x: x + 17 if x % 3 == 0 else x,
    lambda x: x ^ 0b1010,  # Bitwise distraction
    lambda x: int(str(x)[::-1]) if x > 10 else x  # Reverse digits if large
]

def apply_transforms(value, pipeline):
    result = value
    for func in pipeline:
        result = func(result)
    return result

# Main signal processor
def process_transmission(sequence, offset):
    adjusted_values = []
    cumulative_shift = 0

    for i, num in enumerate(sequence):
        shifted = num + offset + (i % 5)
        transformed = apply_transforms(shifted, transform_pipeline)
        adjusted_values.append(transformed)

        # Dead code branch — never executed due to logic
        if len(adjusted_values) > 1000:
            cumulative_shift += sum(x for x in adjusted_values if x < 0)

    # Real computation buried among distractors
    base_sum = sum(adjusted_values)
    length_factor = len(adjusted_values)
    magic_constant = 42
    checksum = (base_sum * magic_constant) % 97

    # Final computation using string manipulation
    checksum_str = str(checksum).ljust(4, '0')
    rotated = checksum_str[2:] + checksum_str[:2]  # Rotate left by 2
    final_signal = int(rotated)

    # Irrelevant post-processing
    validation_layer = ''.join(sorted(set(rotated)))
    debug_info = {"valid": True, "version": "2.1", "signal": final_signal}

    return final_signal

# Initialization data
sensor_input = [18, -5, 23, 14, 9, -11, 32, 7]
correction_offset = 3

# Execution flow with red herrings
_, log_data = analyze_sensor_readings(sensor_input)
dummy_entropy = compute_entropy(sensor_input)

# Key statement
final_signal = process_transmission(sensor_input, correction_offset)

# Output result as required
print(f"Result: {final_signal}")