import math

def analyze_pattern(sequence, threshold):
    count = 0
    temp_sum = 0
    dummy_result = 0
    for i, val in enumerate(sequence):
        if val > threshold:
            count += 1
            temp_sum += val * (i + 1)
        else:
            temp_sum -= val // 2
    # Distractor: complex-looking but unused calculation
    dummy_result = sum(x ** 0.5 for x in sequence if x % 2 == 0) * count
    return count > 3


def transform_values(data):
    shifted = [x << 1 for x in data]  # Bit manipulation red herring
    adjusted = [x + 5 for x in shifted]
    return [x for x in adjusted if x % 3 != 0]


def compute_metrics(values):
    total = 0
    factor = 1
    for idx, (a, b) in enumerate(zip(values[:-1], values[1:])):
        if idx % 2 == 0:
            total += a * b
        else:
            total -= a + b
    # Dead code path - never executed due to fixed input length
    if len(values) > 100:
        factor = math.log(len(values))
    return total * factor


def filter_and_scale(dataset, flags):
    result = []
    scale_factor = 2.5
    offset = 10
    noise_floor = 0.01
    for i, item in enumerate(dataset):
        if flags[i % len(flags)] is True:
            scaled = item * scale_factor + offset
            if scaled > noise_floor:
                result.append(int(scaled))
        else:
            result.append(item >> 2)  # Unused branch distraction
    return result


def process_results(data, config):
    base_sum = sum(data)
    multiplier = 1
    for i, val in enumerate(data):
        if i % 3 == 0 and config[i % len(config)]:
            multiplier *= 2
    # Key logic embedded among distractions
    adjustment = 0
    for j in range(len(data)):
        if j < len(config) and config[j]:
            adjustment += int(math.sin(j) ** 2 * 10)
    return base_sum * multiplier + adjustment

# Irrelevant helper (decoy function)
def validate_integrity(stream):
    checksum = 0
    for byte in stream:
        checksum ^= byte
    return checksum == 0

# Main execution flow with mixed relevance
raw_input = [7, 14, 21, 13, 9, 6, 8]
decoy_sequence = [x ^ 5 for x in raw_input]  # Bitwise red herring

# Transform data using relevant and irrelevant steps
temp_data = transform_values(raw_input)

# Conditional branching based on analysis (distractor call)
analysis_flag = analyze_pattern(decoy_sequence, 10)

# Control structure with misleading intermediate
control_flags = [True, False, True, True, False]

# Real transformation chain
transformed_data = filter_and_scale(temp_data, control_flags)

# Decoy metric computation (unused result)
unused_metric = compute_metrics(transformed_data)

# Critical statement containing answer
critical_index = len(transformed_data) // 2
temp_store = transformed_data[:critical_index]
final_output = process_results(transformed_data, control_flags)

# Print final result as required
print(f"Target result: {final_output}")