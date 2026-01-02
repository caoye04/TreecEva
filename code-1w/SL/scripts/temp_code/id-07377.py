from collections import defaultdict

# Simulate sensor data processing with noise filtering and performance scoring
def process_sensor_readings(raw_readings):
    filtered_data = []
    noise_floor = 0.1
    signal_boost = 1.5
    temp_adjustment = 0.0

    for reading in raw_readings:
        adjusted = reading * signal_boost
        if abs(adjusted) > noise_floor:
            filtered_data.append(adjusted)

    return filtered_data


def calculate_entropy(values):
    from math import log2
    freq = defaultdict(int)
    total = len(values)
    entropy = 0.0

    for v in values:
        freq[round(v, 1)] += 1

    for count in freq.values():
        p = count / total
        entropy -= p * log2(p) if p > 0 else 0

    return round(entropy, 4)


def evaluate_performance(metrics, threshold):
    score = 0
    penalty = 0

    # Key logic branch affecting final score
    if metrics['stability'] > threshold:
        score += 25
    else:
        penalty += 10

    if metrics['consistency'] >= 0.85:
        score += 20

    if metrics['response_time'] < 0.5:
        score += 15

    # Irrelevant computation - distractor (bitwise on float converted to int)
    magic_key = int(metrics['response_time'] * 1000) ^ int(metrics['consistency'] * 100)
    magic_key = magic_key & 0xFF | 0x100

    # Unused branching - dead code path
    if magic_key > 300:
        return -999  # never reached

    # More irrelevant variables
    debug_trace = [magic_key >> i for i in range(3)]
    checksum = sum(debug_trace) & 0xFFFF

    final = score - penalty
    return final

# Main execution flow
raw_sensor_input = [0.05, 0.03, 0.12, 0.15, 0.09, 0.11, 0.13, 0.08, 0.10, 0.14]
base_threshold = 0.75

processed = process_sensor_readings(raw_sensor_input)

# Compute derived metrics
metric_data = defaultdict(float)
metric_data['stability'] = sum(processed) / len(processed)
metric_data['consistency'] = len(processed) / len(raw_sensor_input)
metric_data['response_time'] = 0.42 + (len(processed) * 0.01)  # simulated delay factor

# Secondary distraction: string-based status tagging (unused)
status_tags = ['OK' if x > 0.1 else 'LOW' for x in processed]
status_counter = {tag: status_tags.count(tag) for tag in set(status_tags)}

# Additional red herring: entropy calculation not used in final score
redundant_entropy = calculate_entropy(processed)

# Critical statement
final_score = evaluate_performance(metric_data, base_threshold)

print(f"Result: {final_score}")