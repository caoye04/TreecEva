from collections import defaultdict, Counter
import math

# Simulated sensor data processing with performance evaluation
def analyze_readings(readings):
    stats = defaultdict(float)
    temp_count = 0
    total_power = 0.0

    for r in readings:
        if r < 0:
            continue  # Invalid reading
        if 10 <= r <= 50:
            stats['valid_count'] += 1
            stats['sum'] += r
            temp_count += 1
            total_power += r ** 0.8

    if stats['valid_count'] > 0:
        stats['average'] = stats['sum'] / stats['valid_count']
    else:
        stats['average'] = 0

    # Irrelevant transformation
    decay_factor = 0.95
    adjusted_power = total_power
    for _ in range(5):
        adjusted_power *= decay_factor

    return dict(stats)

# Misleading auxiliary function (dead code path)
def calculate_efficiency_index(data):
    if not data:
        return -1
    index = 0
    for val in data:
        index += abs(val) % 7
    return index * 1.5

# Core logic disguised among distractors
def transform_sequence(seq):
    transformed = []
    bit_flags = 0
    for item in seq:
        shifted = (item << 2) & 0xFF
        if shifted > 100:
            bit_flags |= 1
        transformed.append(shifted ^ 0x5A)
    return transformed, bit_flags

# Unused utility
def validate_checksum(buffer):
    checksum = 0
    for b in buffer:
        checksum = (checksum + b) & 0xFFFF
    return checksum == 0x1234

# Main evaluation logic with red herrings
def evaluate_performance(metrics, threshold):
    score = 0
    penalty = 0

    # Real computation branch
    if 'average' in metrics:
        raw_value = metrics['average'] * 1.75
        if raw_value > threshold:
            score += int(raw_value)
        else:
            score += 50

    # Distractor: complex but unused calculation
    outlier_count = 0
    for k, v in metrics.items():
        if v != 0 and math.log(v + 1) > 2.5:
            outlier_count += 1

    temp_array = [score for _ in range(3)]
    for i in range(len(temp_array)):
        temp_array[i] = (temp_array[i] + 13) * 2
        if i % 2 == 0:
            temp_array[i] -= 5

    # Another decoy operation
    histogram = Counter(temp_array)
    decoy_result = sum(histogram.values()) * 0.1

    # Critical branching logic (depends on multiple prior states)
    extra_bonus = 0
    bonus_multiplier = 1
    if metrics.get('valid_count', 0) > 3:
        bonus_multiplier *= 1.2
    if score > 60:
        extra_bonus = 25

    final_component = score * bonus_multiplier + extra_bonus

    # Final assignment - this is the key statement
    final_score = int(final_component - penalty)

    # Unused trace variable
    debug_trace = f"Score={score}, Penalty={penalty}, Final={final_score}"

    return final_score

# Simulated input data
sensor_readings = [12, 45, 8, 23, 56, 34, 19, 41]
metric_data = analyze_readings(sensor_readings)
base_threshold = 28

# Transform sequence - looks important but only bit_flags matters indirectly
processed_seq, flags = transform_sequence([10, 20, 30])

# Decoy call
_ = calculate_efficiency_index(sensor_readings)

# Key execution point
final_score = evaluate_performance(metric_data, base_threshold)

print(f"Result: {final_score}")