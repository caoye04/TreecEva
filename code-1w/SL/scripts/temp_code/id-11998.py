from collections import defaultdict, Counter
import math

# Simulated sensor data processing pipeline for environmental anomaly detection
def fetch_raw_readings():
    return [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6]

def apply_noise_filter(data):
    filtered = []
    for i in range(len(data)):
        if i == 0 or i == len(data) - 1:
            filtered.append(data[i])
        else:
            smoothed = (data[i-1] + 2 * data[i] + data[i+1]) // 4
            filtered.append(smoothed)
    return filtered

def compute_entropy(values):
    counts = Counter(values)
    total = len(values)
    entropy = 0.0
    for count in counts.values():
        prob = count / total
        entropy -= prob * math.log2(prob)
    return round(entropy, 6)

def generate_checksum(sequence):
    # Irrelevant checksum for distractor
    chk = 0
    for val in sequence:
        chk = (chk * 31 + val) % 10007
    return chk

def detect_outliers(data, threshold=2):
    mean_val = sum(data) / len(data)
    std_dev = (sum((x - mean_val) ** 2 for x in data) / len(data)) ** 0.5
    return [i for i, x in enumerate(data) if abs(x - mean_val) > threshold * std_dev]

def shift_cipher_encode(sequence, shift_key):
    # Decoy transformation
    return [(x + shift_key) % 10 for x in sequence]

def reconstruct_timeline(indices, length):
    timeline = [False] * length
    for idx in indices:
        timeline[idx] = True
    return timeline

def aggregate_by_magnitude(data):
    # Complex but irrelevant aggregation
    bins = defaultdict(int)
    for val in data:
        bin_key = val // 3
        bins[bin_key] += 1
    return dict(bins)

def analyze_pattern(dataset, sensitivity):
    # Core relevant logic
    frequency_map = Counter(dataset)
    dominant_value = frequency_map.most_common(1)[0][1]
    
    # Secondary metric: gap variance
    positions = defaultdict(list)
    for idx, val in enumerate(dataset):
        positions[val].append(idx)
    
    avg_gaps = []
    for pos_list in positions.values():
        if len(pos_list) > 1:
            gaps = [pos_list[i] - pos_list[i-1] for i in range(1, len(pos_list))]
            avg_gaps.append(sum(gaps) / len(gaps))
    
    if not avg_gaps:
        pattern_score = dominant_value
    else:
        mean_gap = sum(avg_gaps) / len(avg_gaps)
        pattern_score = dominant_value * (sensitivity / mean_gap)
    
    # Tertiary adjustment based on distribution skew
    sorted_vals = sorted(frequency_map.values())
    mid = len(sorted_vals) // 2
    lower_half = sorted_vals[:mid]
    upper_half = sorted_vals[mid:]
    if len(lower_half) == 0:
        skew_index = 0
    else:
        skew_index = (sum(upper_half) - sum(lower_half)) / len(lower_half)
    
    final_adjustment = pattern_score + (skew_index * 0.75)
    return int(round(final_adjustment))

# Main execution flow
raw_readings = fetch_raw_readings()
filtered_readings = apply_noise_filter(raw_readings)

# Distractor computations
entropy_metric = compute_entropy(filtered_readings)
checksum_value = generate_checksum(filtered_readings)
outlier_indices = detect_outliers(filtered_readings, threshold=1.5)
timeline_flags = reconstruct_timeline(outlier_indices, len(filtered_readings))
cipher_shifted = shift_cipher_encode(filtered_readings, 7)
aggregated_bins = aggregate_by_magnitude(filtered_readings)

# Key transformation: focus on repeating patterns
transformed_data = []
for i, val in enumerate(filtered_readings):
    if i % 3 == 0:
        transformed_data.append(val * 2)
    elif i % 4 == 0:
        transformed_data.append(val + 1)
    else:
        transformed_data.append(val)

# Noise injection for distraction
noise_sequence = [i % 5 for i in range(len(transformed_data))]
noisy_data = [a ^ b for a, b in zip(transformed_data, noise_sequence)]

key_threshold = 3

# Critical statement
final_diagnostic = analyze_pattern(transformed_data, key_threshold)

print(f"Result: {final_diagnostic}")