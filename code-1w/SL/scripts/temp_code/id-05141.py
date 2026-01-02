from collections import defaultdict, Counter
import math

# Simulated sensor data processing with diagnostic logic
def collect_readings():
    raw_signals = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    offset = 2
    adjusted = [x + offset for x in raw_signals]
    return adjusted

def filter_anomalies(data):
    mean_val = sum(data) / len(data)
    filtered = [x for x in data if abs(x - mean_val) < 2.5]
    # Irrelevant transformation (distractor)
    squared_map = [x**2 for x in data]
    temp_result = sum(squared_map[:3]) * 0.1
    return filtered

def reconstruct_sequence(cleaned):
    count_map = defaultdict(int)
    for val in cleaned:
        count_map[val] += 1
    sorted_unique = sorted(set(cleaned))
    # Dead path: never used (distractor)
    if len(sorted_unique) > 10:
        extended = sorted_unique + [0] * 5
    else:
        extended = None
    reconstructed = []
    for val in sorted_unique:
        reconstructed.extend([val] * count_map[val])
    return reconstructed

def apply_phase_shift(seq):
    shifted = []
    for i, val in enumerate(seq):
        if i % 2 == 0:
            shifted.append(val + i // 2)
        else:
            shifted.append(val - (i // 3))
    # Misleading intermediate computation (red herring)
    checksum = 0
    for x in shifted:
        checksum = (checksum * 31 + x) % 10007
    scale_factor = math.log(checksum + 10) / 2.5
    # Unused scaled version (distractor)
    scaled_seq = [x * scale_factor for x in shifted]
    return shifted

def generate_metadata(processed):
    meta = {}
    meta['length'] = len(processed)
    meta['range'] = max(processed) - min(processed)
    meta['mode_freq'] = max(Counter(processed).values())
    # Decoy calculation with no downstream use
    entropy = 0.0
    total = len(processed)
    for count in Counter(processed).values():
        p = count / total
        entropy -= p * math.log(p)
    meta['entropy_approx'] = round(entropy, 3)
    return meta

def transform_entry(entry, index):
    if entry % 2 == 0:
        return entry * 2 + (index % 3)
    else:
        return entry * 3 - (index % 4)

def batch_transform(data_list):
    transformed = []
    for idx, val in enumerate(data_list):
        new_val = transform_entry(val, idx)
        transformed.append(new_val)
    # Parallel irrelevant tracking (distractor)
    magnitude_sum = sum(abs(x) for x in transformed)
    growth_rate = magnitude_sum / (len(transformed) + 1e-5)
    return transformed

def analyze_pattern(dataset):
    stats = defaultdict(float)
    for num in dataset:
        if num > 10:
            stats['high'] += 1
        elif num > 5:
            stats['medium'] += 1
        else:
            stats['low'] += 1
    # Core logic: weighted diagnostic score
    score = 0
    score += stats['high'] * 7
    score += stats['medium'] * 3
    score += stats['low'] * 1
    # Additional adjustment based on bit patterns (relevant)
    bit_count = 0
    for num in dataset:
        bit_count += bin(num).count('1')
    adjustment = bit_count % 5
    final_score = score + adjustment
    
    # Multiple decoy computations below (misleading paths)
    avg_bits = bit_count / len(dataset) if dataset else 0
    complexity_index = avg_bits * len(stats) + sum(dataset) % 100
    normalized_score = (final_score / 100.0) * (complexity_index + 1)
    
    # Final result derived from deterministic chain
    return int(final_score)

# Main execution flow
sensor_data = collect_readings()
cleaned_data = filter_anomalies(sensor_data)
reconstructed_data = reconstruct_sequence(cleaned_data)
shifted_data = apply_phase_shift(reconstructed_data)
metadata = generate_metadata(shifted_data)
transformed_data = batch_transform(shifted_data)
final_diagnostic = analyze_pattern(transformed_data)
print(f"Target result: {final_diagnostic}")