from collections import defaultdict
import math

# Simulated sensor data processing with red herrings and complex logic paths
def preprocess_sensor_stream(raw_readings):
    processed = []
    temp_buffer = []
    checksum = 0
    decoy_accumulator = 0  # Irrelevant accumulator for distraction

    for val in raw_readings:
        if val < 0:
            temp_buffer.append(abs(val))
        elif val % 2 == 0:
            processed.append(val ** 0.5)
        else:
            processed.append(val * 2)
        checksum += val % 7
        decoy_accumulator += val * 11  # Misleading computation

    # Dead code path - never accessed under current logic
    if len(temp_buffer) > 100:
        fallback = [x ^ 3 for x in temp_buffer]
        return fallback

    return processed


def filter_anomalies(data_sequence, sensitivity):
    normal_range = []
    anomalies = []
    baseline = sum(data_sequence) / len(data_sequence)
    variance_pool = []  # Unused collection

    for x in data_sequence:
        if abs(x - baseline) < sensitivity:
            normal_range.append(x)
        else:
            anomalies.append(x)

    # Red herring transformation
    anomaly_score = 0
    for a in anomalies:
        anomaly_score += int(math.log(max(a, 1.1)) * 10)

    # Decoy sorting with no impact
    sorted(anomalies, reverse=True)

    return normal_range


def shift_cipher(text, offset):
    # Irrelevant utility function to distract
    result = ''
    for c in text:
        if c.isalpha():
            base = ord('a') if c.islower() else ord('A')
            result += chr((ord(c) - base + offset) % 26 + base)
        else:
            result += c
    return result


def transform_signal(pattern):
    # Core relevant transformation
    shifted = [p ^ 5 for p in pattern]  # Bitwise XOR manipulation
    scaled = [s * 1.5 for s in shifted]
    return [round(x, 3) for x in scaled]


def analyze_pattern(dataset, threshold):
    count_map = defaultdict(int)
    total_weight = 0.0
    intermediate_sum = 0  # Distractor variable

    for item in dataset:
        bucket = int(item // 2)
        count_map[bucket] += 1
        total_weight += item * (item > threshold)
        intermediate_sum += item % 4  # Meaningless accumulation

    # Conditional expression that appears important but is unused
    adjustment_factor = 1.1 if sum(count_map.values()) > threshold else 0.9

    # Real answer computation buried in logic
    filtered_values = [v for v in dataset if v > threshold]
    if not filtered_values:
        return 0

    product = 1
    for v in filtered_values:
        product *= (int(v) % 17)  # Modular arithmetic chain

    final_metric = product - (len(count_map) * 100)
    return final_metric

# Main execution flow
if __name__ == '__main__':
    # Initial sensor input
    telemetry_data = [12, 3, 8, 1, 5, 7, 11, 4, 9, 6, 10, 2, 13]

    # Step 1: Preprocess signal
    cleaned_signal = preprocess_sensor_stream(telemetry_data)

    # Step 2: Filter noise (threshold tuned to retain most data)
    refined_signal = filter_anomalies(cleaned_signal, sensitivity=3.5)

    # Step 3: Transform using bitwise operations
    transformed_data = transform_signal(refined_signal)

    # Step 4: Compute key threshold based on length (critical path)
    key_threshold = len(transformed_data) + 2

    # Step 5: Analyze final diagnostic pattern
    final_diagnostic = analyze_pattern(transformed_data, key_threshold)

    # Print result for extraction
    print(f"Target result: {final_diagnostic}")