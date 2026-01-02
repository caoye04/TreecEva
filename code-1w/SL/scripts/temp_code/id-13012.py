def preprocess_readings(raw_readings):
    filtered = [x for x in raw_readings if x > 0]
    adjusted = [x * 1.5 for x in filtered]
    return adjusted


def generate_sequence(n):
    seq = [1, 1]
    for i in range(2, n):
        seq.append(seq[i-1] + seq[i-2])
    return seq  # Unused function - red herring


def compute_entropy(data):
    from math import log2
    freq = {}
    for item in data:
        freq[item] = freq.get(item, 0) + 1
    total = len(data)
    entropy = 0.0
    for count in freq.values():
        p = count / total
        entropy -= p * log2(p)
    return entropy  # Computationally relevant but not on critical path


def shift_cipher(text, key):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - base + key) % 26 + base)
        else:
            result += char
    return result  # Decoy cryptographic function


def validate_checksum(arr):
    checksum = 0
    for val in arr:
        checksum = (checksum + val) % 257
    return checksum == 137  # Arbitrary condition - distractor logic


def transform_signal(signal_data):
    processed = []
    for val in signal_data:
        temp = (val ** 2) % 101
        if temp % 2 == 0:
            processed.append(temp + 5)
        else:
            processed.append(temp - 3)
    return processed


def analyze_pattern(metrics):
    cumulative = 0
    for i, val in enumerate(metrics):
        if i % 3 == 0:
            cumulative += val * 2
        elif i % 3 == 1:
            cumulative += val
        else:
            cumulative -= val // 4
    return cumulative

# Main execution flow
raw_sensor_data = [12, -5, 23, 8, 0, 17, 4, -3, 19]

# Irrelevant transformations
fibonacci_test = generate_sequence(10)
entropy_value = compute_entropy(fibonacci_test)
ciphered_tag = shift_cipher("diagnostics", 7)

# Core processing path begins
processed_data = preprocess_readings(raw_sensor_data)
transformed_signal = transform_signal(processed_data)

# Simulate multiple system checks
checksum_valid = validate_checksum(transformed_signal)
signal_set = set(transformed_signal)
expanded_metrics = [x for x in transformed_signal if x in {y % 61 for y in processed_data}]
filtered_metrics = [x for x in expanded_metrics if x > 10]
duplicate_check = len(transformed_signal) != len(set(transformed_signal))

# Key transformation
adjusted_metrics = []
for idx, val in enumerate(filtered_metrics):
    if idx % 2 == 0:
        adjusted_metrics.append(val + idx)
    else:
        adjusted_metrics.append(val * (idx % 5))

# Final analysis step
final_diagnostic = analyze_pattern(adjusted_metrics)

# Print result as required
print(f"Target result: {final_diagnostic}")