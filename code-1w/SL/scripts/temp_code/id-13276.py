from itertools import combinations, cycle
import math

# Simulated sensor array data with noise and metadata
raw_readings = [104, 92, 115, 88, 97, 121, 84, 96, 103, 111]
noise_profile = [0.12, -0.05, 0.31, -0.18, 0.09, 0.24, -0.11, 0.07, -0.22, 0.15]
metadata_flags = ['OK', 'CAL', 'OK', 'ERR', 'OK', 'CAL', 'OK', 'OK', 'ERR', 'OK']

# Irrelevant auxiliary transformation (dead path)
def legacy_transform(x):
    return sum([i * val for i, val in enumerate(x)]) // len(x)

# Decoy function that looks important but isn't used in critical path
def calculate_coherence(data):
    paired_diffs = [abs(a - b) for a, b in zip(data, data[1:])]
    return sum(paired_diffs) / len(paired_diffs) if paired_diffs else 0

# Critical preprocessing: filter by status and apply noise correction
def preprocess_sensors(readings, noise, flags):
    cleaned = []
    for i, flag in enumerate(flags):
        if flag == 'OK':
            corrected = readings[i] + int(noise[i] * 100)
            cleaned.append(corrected)
    return cleaned

# Secondary transformation with bit manipulation red herring
def enhance_signal(data):
    amplified = []
    rotation_cycle = cycle([1, 2, 3])
    for val in data:
        # Bit manipulation distraction
        shifted = (val << 1) ^ 0b1010
        # Real transformation
        enhanced_val = val + (val % next(rotation_cycle))
        amplified.append(enhanced_val)
    return amplified

# Core logic hidden among distractors
def generate_triplet_entropy(data):
    if len(data) < 3:
        return 0.0
    # Generate all triplets - looks computationally heavy but small input
    triplet_combinations = list(combinations(data, 3))
    entropies = []
    for triplet in triplet_combinations:
        mean = sum(triplet) / 3
        variance = sum((x - mean) ** 2 for x in triplet) / 3
        entropy = math.log(variance + 1) if variance > 0 else 0.0
        entropies.append(entropy)
    return sum(entropies) / len(entropies) if entropies else 0.0

# Main computation buried in context
def compute_filtration(dataset, offset):
    base_metric = sum([x for x in dataset if x % 2 == 1])  # sum of odds
    adjustment = int(offset * 10)  # scale down offset impact
    result = base_metric - adjustment
    # Additional decoy logic
    if result > 100:
        result = result ^ 0b1100  # irrelevant bit flip
    return result

# Misleading initialization sequence (appears critical)
temp_cache = {}
for idx, val in enumerate(raw_readings):
    temp_cache[f'idx_{idx}'] = val ** 2 - noise_profile[idx] * 50

# Dead code path with plausible naming
def validate_checksum(arr):
    total = 0
    for i, v in enumerate(arr):
        total += v * (i + 1)
    return total % 1024

# Real execution begins here
filtered_data = preprocess_sensors(raw_readings, noise_profile, metadata_flags)
validated_data = [x for x in filtered_data if 85 < x < 120]  # secondary filter
processed_signal = enhance_signal(validated_data)

# Red herring: coherence score calculated but not used
coherence_score = calculate_coherence(processed_signal)

# Key entropy calculation feeding into final answer
entropy_measure = generate_triplet_entropy(processed_signal)
entropy_offset = math.sin(entropy_measure) * 2.5

# Critical statement containing the target variable
filtration_score = compute_filtration(filtered_data, entropy_offset)

# Print final result as required
print(f"Result: {filtration_score}")