import math

# Simulated sensor data processing with red herrings and distractions
def preprocess_signal(raw_signal):
    if not raw_signal:
        return []
    filtered = [x for x in raw_signal if x > 0.5]
    normalized = [round(x / max(filtered), 3) for x in filtered]
    return normalized

# Irrelevant helper - looks important but unused in critical path
def calculate_entropy(data):
    freq_map = {}
    for val in data:
        freq_map[val] = freq_map.get(val, 0) + 1
    entropy = 0.0
    total = len(data)
    for count in freq_map.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

# Another decoy function - operates on string representations
def validate_checksum(signal_str):
    if isinstance(signal_str, list):
        signal_str = ''.join(map(str, signal_str))
    digit_sum = sum(int(c) for c in signal_str if c.isdigit())
    return digit_sum % 7 == 0

# Core transformation - actually used
def encode_sequence(seq, key_offset):
    encoded = []
    for i, val in enumerate(seq):
        shifted = val * (i + 1) + key_offset
        encoded.append(int(round(shifted)))
    return encoded

# Data augmentation - misleading name, only does simple expansion
def augment_dataset(data_points):
    extended = []
    for dp in data_points:
        extended.append(dp)
        extended.append(dp * 0.95)  # minor variation
    return extended[:len(data_points)]  # returns same length!

# Real processing chain starts here
raw_input_stream = [0.8, 1.2, 0.6, 1.5, 0.9, 1.1, 0.7, 1.3]
base_reference = sum(x ** 0.5 for x in raw_input_stream[:4])
decoy_matrix = [[i * j for j in range(3)] for i in range(3)]

# Step 1: Preprocess signal
processed = preprocess_signal(raw_input_stream)

# Step 2: Generate auxiliary info (distraction)
length_snapshot = len(processed)
sum_check = sum(processed) * 1000
checksum_tag = f"CHK{int(sum_check)}"

# Step 3: Encode using dynamic offset
offset_key = int(math.floor(base_reference))
encoded_data = encode_sequence(processed, offset_key)

# Step 4: Augment (but doesn't really change much due to slice limit)
augmented_data = augment_dataset(encoded_data)

# Step 5: Transform via string-based manipulation (uses string method)
data_as_strings = [str(num) for num in augmented_data]
joined_signal = '-'.join(data_as_strings)
split_back = joined_signal.split('-')
reconstructed = [int(s) for s in split_back]

# Step 6: Apply threshold filter
threshold = 5
filtered_reconstructed = [x for x in reconstructed if x > threshold]

# Step 7: Map to diagnostic levels
diagnostic_map = {}
for val in filtered_reconstructed:
    band = val // 10
    diagnostic_map[val] = band * 2

# Step 8: Analyze pattern recursively
def analyze_pattern(data_list, limit):
    if not data_list or limit <= 0:
        return 1
    head = data_list[0]
    tail = data_list[1:]
    contribution = head % 7
    recursive_part = analyze_pattern(tail, limit - 1)
    return contribution * recursive_part + (head // 12)

# Critical assignment point
transformed_data = list(set(reconstructed))  # remove dups
transformed_data.sort(reverse=True)

# Final computation
final_diagnostic = analyze_pattern(transformed_data, threshold)

# Print result for verification
print(f"Result: {final_diagnostic}")