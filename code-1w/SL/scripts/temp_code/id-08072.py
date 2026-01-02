from collections import defaultdict, Counter
import math

# Simulated sensor data processing with red herrings
def preprocess_signal(raw_readings):
    filtered = [x for x in raw_readings if x > -50 and x < 150]
    shifted = [x + 3 for x in filtered]
    return shifted

# Irrelevant transformation — looks important but unused later
def encrypt_sequence(data):
    return [((val << 2) ^ 0xAB) & 0xFF for val in data]

# Another decoy function that's defined but not used in main flow
def compute_entropy(arr):
    counts = Counter(arr)
    total = len(arr)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

# Core logic disguised among distractions
def extract_features(dataset, threshold=10):
    stats = defaultdict(int)
    temp_buffer = []
    
    for i, val in enumerate(dataset):
        if i % 3 == 0:
            stats['triple_index'] += 1
        if val > threshold:
            temp_buffer.append(val * 1.5)
        else:
            temp_buffer.append(val ** 0.5 if val >= 0 else 0)
    
    # Real usage: this derived value matters
    avg_val = sum(temp_buffer) / len(temp_buffer) if temp_buffer else 0
    stats['adjusted_avg'] = int(avg_val) + 7
    return dict(stats)

# Central transformation that feeds into final result
def transform_sequence(seq):
    modified = [seq[i] * (i + 1) for i in range(len(seq))]
    sliced_part = modified[2:9:2]  # slicing operation used here
    return [x - 5 for x in sliced_part]

# Main analysis function — only one that affects final answer
def analyze_pattern(values, offset):
    accumulator = 0
    multiplier = len(values) % 7
    
    for idx, v in enumerate(values):
        if idx % 2 == 0:
            accumulator += (v + offset) * 2
        else:
            accumulator -= (v - offset) // 2
    
    # Final computation step
    return accumulator * multiplier

# --- Execution Flow with Distractors ---

# Real input data
raw_sensor_data = [4, 8, 6, 7, 5, 3, 0, 9, 2, 1, 8, 4]

# Dead-end variables — look like they're used
encrypted_stream = encrypt_sequence(raw_sensor_data)
diagnostic_checksum = sum(encrypted_stream) % 256

# Actual preprocessing path
cleaned_data = preprocess_signal(raw_sensor_data)
feature_map = extract_features(cleaned_data, threshold=5)

# Key transformation chain
transformed_data = transform_sequence(cleaned_data)
baseline_offset = feature_map['adjusted_avg']  # depends on prior logic

# Critical execution point
final_diagnostic = analyze_pattern(transformed_data, baseline_offset)

# Print target result
print(f"Target result: {final_diagnostic}")