import math

# System health monitoring simulation with obfuscated signal processing

def preprocess_signal(raw_data):
    filtered = [x for x in raw_data if x > 0]
    normalized = [round(math.log(val), 3) for val in filtered]
    return normalized

# Irrelevant helper: text analysis decoy
def analyze_text_pattern(text):
    char_freq = {c: text.count(c) for c in set(text)}
    upper_count = len([c for c in text if c.isupper()])
    reversed_text = text[::-1]
    word_count = len(text.split())
    # This function is never called but looks important
    return {'freq': char_freq, 'uppercase': upper_count}

# Core transformation chain
raw_telemetry = [144, 25, 49, 81, 100, 169, 196, 225]
processed = preprocess_signal(raw_telemetry)

# Bit manipulation layer (partially relevant)
bit_encoded = []
for val in processed:
    int_val = int(val * 10)  # Scale to integer
    transformed = (int_val ^ 255) & 1023  # XOR + mask
    bit_encoded.append(transformed)

# Decoy data structure - mimics real processing
historical_snapshots = {
    'baseline_2023': [120, 45, 78, 90],
    'thresholds': {'warning': 75, 'critical': 95},
    'metadata': {'version': '2.1', 'checksum': 'a1b2c3'}
}

# Unused but plausible-looking functions
def compute_entropy(data):
    total = sum(data)
    probs = [d / total for d in data]
    return -sum(p * math.log(p) for p in probs if p > 0)

def generate_checksum(sequence):
    return sum(ord(c) for c in str(sequence)) % 1000

# Real processing begins here
segment_a = bit_encoded[::2]
segment_b = bit_encoded[1::2]

# Conditional expression mix
scaling_factor = 1.75 if len(segment_a) > 3 else 2.25
offset_correction = 15 if sum(bit_encoded) % 2 == 0 else -15

# Encoding segments with distraction
encoded_segments = []
for i, val in enumerate(segment_a):
    # Mix arithmetic and bitwise
    temp = (val >> 2) * scaling_factor
    noise_injected = temp + (i % 7)  # Minor perturbation
    encoded_segments.append(noise_injected)

# Dead code path: looks like it's used
auxiliary_buffer = []
for x in segment_b:
    squared = x ** 2
    modulated = squared % 1000
nonsense_flag = False
if len(auxiliary_buffer) > 10:
    auxiliary_buffer.clear()

# Weight assignment with red herring
weights = [0.8, 1.2, 0.9, 1.1]  # Aligned with segment_a length

# Critical computation obscured by context
intermediate_sum = 0
for idx in range(len(encoded_segments)):
    weighted_val = encoded_segments[idx] * weights[idx]
    intermediate_sum += weighted_val

# Distractor: unused statistical calculation
mean_fake = sum(encoded_segments) / len(encoded_segments)
std_dev_fake = math.sqrt(sum((x - mean_fake) ** 2 for x in encoded_segments) / len(encoded_segments))

# Actual final step
final_diagnostic = aggregate_metrics(encoded_segments, weights)

# Implementation of required function
def aggregate_metrics(segments, w):
    total = 0.0
    for i in range(len(segments)):
        total += segments[i] * w[i]
    adjustment = math.sin(len(w)) * 10
    return round(total + adjustment, 4)

# Print result as required
print(f"Target result: {final_diagnostic}")