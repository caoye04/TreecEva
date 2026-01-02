def preprocess_signal(raw_samples):
    filtered = [x for x in raw_samples if abs(x) > 0.1]
    normalized = [round(x / max(filtered), 3) for x in filtered]
    return normalized


def generate_sequence(length):
    seq = [1, 1]
    for i in range(2, length):
        seq.append(seq[i-1] + seq[i-2])
    return seq


def evaluate_stability(readings):
    baseline = sum(readings) / len(readings)
    variance = sum((x - baseline) ** 2 for x in readings) / len(readings)
    return variance < 0.5


def encode_state(signal):
    encoded = ''
    for val in signal:
        encoded += '1' if val > 0 else '0'
    return encoded


def decode_binary_string(binary_str):
    # Irrelevant decoding function (dead code path)
    return int(binary_str, 2)


def compute_checksum(data):
    # Misleading checksum with no impact on final result
    checksum = 0
    for item in data:
        checksum ^= int(abs(item) * 100)
    return checksum


def transform_dataset(signal):
    # Unused transformation (distractor)
    return [x * 2 for x in signal if x < 0]


def analyze_pattern(dataset, threshold):
    count = 0
    for i in range(1, len(dataset)):
        if dataset[i] > dataset[i-1] and dataset[i] > threshold:
            count += 1
    adjustment = len([x for x in dataset if x < 0])
    return count * 100 + adjustment

# Main execution flow
raw_sensor_data = [-2.1, 0.5, 3.4, -0.3, 5.6, 1.2, -1.1, 4.4, 0.8]
key_threshold = 1.0

# Step 1: Preprocess signal to remove noise
processed_signal = preprocess_signal(raw_sensor_data)

# Step 2: Generate Fibonacci sequence for unrelated diagnostic test
fibonacci_test = generate_sequence(7)

# Step 3: Evaluate stability (used to create distraction)
stability_flag = evaluate_stability(fibonacci_test)

# Step 4: Encode signal state into binary (irrelevant to final answer)
binary_representation = encode_state(processed_signal)

# Step 5: Compute useless checksum (distractor variable)
misleading_checksum = compute_checksum(processed_signal)

# Step 6: Transform dataset (result ignored)
discarded_transformation = transform_dataset(processed_signal)

# Step 7: Analyze actual pattern in processed data
final_diagnostic = analyze_pattern(processed_signal, key_threshold)

# Output target result
print(f"Result: {final_diagnostic}")