def preprocess_signal(raw_samples):
    filtered = [x for x in raw_samples if x > -50 and x < 50]
    normalized = [round(x / max(filtered), 3) for x in filtered]
    return normalized


def generate_sequence(length):
    seq = [1, 1]
    for i in range(2, length):
        seq.append(seq[i-1] + seq[i-2])  # Fibonacci-like, irrelevant
    return seq


def compute_entropy(data):
    from math import log2
    freq_map = {}
    for item in data:
        freq_map[item] = freq_map.get(item, 0) + 1
    total = len(data)
    entropy = -sum((count / total) * log2(count / total) for count in freq_map.values())
    return round(entropy, 4)


def shift_cipher(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result  # Distractor function


def evaluate_outliers(data, threshold=3):
    mean_val = sum(data) / len(data)
    std_dev = (sum((x - mean_val) ** 2 for x in data) / len(data)) ** 0.5
    outliers = [x for x in data if abs(x - mean_val) > threshold * std_dev]
    return len(outliers) > 0


def analyze_pattern(dataset, limit):
    cumulative = 0
    for val in dataset:
        if val < 0:
            cumulative += abs(val) * 2
        else:
            cumulative += int(val * 10)
    return cumulative % 10000

# Main execution block
raw_input_data = [120, -45, 33, 77, -12, 50, 91, -60, 44, 28]
decoy_matrix = [[i*j for j in range(5)] for i in range(5)]  # Unused structure

# Irrelevant transformations
token_stream = 'hello world secure entry'
encoded_message = shift_cipher(token_stream, 13)
fib_sequence = generate_sequence(10)

# Signal preprocessing step
processed_signal = preprocess_signal(raw_input_data)

# Entropy computation on processed data (distractor metric)
signal_entropy = compute_entropy(processed_signal)

# Detect anomalies
has_anomalies = evaluate_outliers(processed_signal, threshold=2.5)

# Transform via set operations: eliminate duplicates and apply condition
unique_vals = list(set([round(x * 100) for x in processed_signal]))
adjusted_vals = [x - 50 for x in unique_vals if x > 10]  # Further filtering

# Introduce bitwise manipulation red herring
temp_flags = 0
for v in adjusted_vals[:3]:
    temp_flags ^= int(v) & 0xFF  # Bitwise XOR with masking, not used later

# Key transformation pipeline
total_sum = sum(adjusted_vals)
shifted_sum = total_sum >> 2  # Integer division by 4 via bit shift
scaled_data = [x / 7 for x in adjusted_vals]
rounded_data = [int(x) for x in scaled_data]
transformed_data = [x + (x << 1) for x in rounded_data]  # x + 2*x = 3*x

# Threshold logic
key_threshold = len(transformed_data) * 2

# Decoy conditional block (never executed due to logic)
if has_anomalies and signal_entropy > 10:
    fallback_result = compute_entropy(fib_sequence)
    final_diagnostic = fallback_result
else:
    # Critical statement
    final_diagnostic = analyze_pattern(transformed_data, key_threshold)

print(f'Result: {final_diagnostic}')