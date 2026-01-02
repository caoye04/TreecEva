from collections import defaultdict, Counter
import math

# Simulated sensor data processing pipeline for a medical diagnostics system
def analyze_readings(readings):
    processed = []
    for val in readings:
        if val < 0:
            continue
        transformed = int((val ** 0.5) * 10)
        if transformed > 100:
            transformed = 100
        processed.append(transformed)
    return processed

# Irrelevant helper - analyzes noise patterns (not used in final path)
def analyze_noise_pattern(signal):
    window_size = 3
    noise_score = 0
    for i in range(len(signal) - window_size + 1):
        window = signal[i:i+window_size]
        if len(set(window)) == window_size:
            noise_score += 1
    return noise_score

# Core transformation function
def normalize_sequence(seq):
    base_shift = sum(seq) // len(seq)
    return [x - base_shift + 50 for x in seq]

# Misleading aggregation - looks important but unused
unused_aggregates = defaultdict(float)
raw_samples = [121, 84, 144, 169, 100, 225, 196]
temp_converted = []
for sample in raw_samples:
    root_val = int(math.sqrt(sample))
    temp_converted.append(root_val)
    unused_aggregates['sum_sqrts'] += root_val
    unused_aggregates['count'] += 1

if unused_aggregates['count'] > 0:
    unused_aggregates['avg_sqrt'] = unused_aggregates['sum_sqrts'] / unused_aggregates['count']

# Real data path begins here
source_data = [150, 200, 175, 188, 163, 192, 181]
filtered_data = [x for x in source_data if x >= 160]
analyzed = analyze_readings(filtered_data)
normalized = normalize_sequence(analyzed)

# Decoy statistical analysis
mean_val = sum(normalized) // len(normalized)
variance_proxy = sum(abs(x - mean_val) for x in normalized) // len(normalized)
flagged = [x for x in normalized if abs(x - mean_val) > variance_proxy]

# Red herring: complex frequency analysis with no impact
freq_count = Counter(normalized)
dominant_levels = [k for k, v in freq_count.items() if v > 1]
adjustment_factor = 0
for level in dominant_levels:
    adjustment_factor += int(math.log(level + 1))

# Threshold configuration map (used later)
threshold_map = {}
for i, val in enumerate([55, 60, 65, 70]):
    label = chr(65 + i)
    threshold_map[label] = val + adjustment_factor  # adjustment_factor ends up being 0

# Unused recursive function - distractor
def calculate_depth_score(data, depth=0):
    if depth >= 3 or len(data) == 0:
        return depth
    split_point = len(data) // 2
    return calculate_depth_score(data[:split_point], depth + 1)

# Actual core metric computation
def compute_stability_index(seq):
    diffs = [abs(seq[i] - seq[i-1]) for i in range(1, len(seq))]
    avg_diff = sum(diffs) / len(diffs) if diffs else 0
    return round(100 - avg_diff, 2)

# Secondary metric with slicing distraction
def assess_consistency(pattern):
    if len(pattern) < 5:
        return 0
    segment_a = pattern[:len(pattern)//2]
    segment_b = pattern[len(pattern)//2:]
    
    # Meaningless overlap check
    overlap = len(set(segment_a) & set(segment_b))
    
    # Real consistency logic
    sorted_b = sorted(segment_b)
    trend = all(sorted_b[i] <= sorted_b[i+1] for i in range(len(sorted_b)-1))
    return 10 + overlap if trend else 10

# Main processing function that combines metrics
def process_metrics(data, thresholds):
    stability = compute_stability_index(data)
    consistency = assess_consistency(data)
    
    # Map data to categories using thresholds
    category_scores = defaultdict(int)
    for val in data:
        for label, thresh in thresholds.items():
            if val >= thresh:
                category_scores[label] += 1
    
    # Primary score calculation
    base_score = stability * 1.5 + consistency * 2
    
    # Apply category multipliers
    multiplier = 1.0
    for score in category_scores.values():
        if score >= 2:
            multiplier *= 1.1
    
    intermediate_result = base_score * multiplier
    
    # Final adjustment based on bit properties of sum
    data_sum = sum(data)
    binary_rep = bin(data_sum)[2:]
    ones_count = binary_rep.count('1')
    zero_groups = ''.join('1' if b == '1' else '0' for b in binary_rep).split('1')
    isolated_zeros = sum(1 for g in zero_groups if len(g) == 1)
    
    # The real adjustment: add difference between ones and isolated zeros
    final_adjustment = ones_count - isolated_zeros
    
    # Critical statement
    final_diagnostic = int(intermediate_result + final_adjustment)
    
    return final_diagnostic

# Execution flow
health_data = normalized  # comes from earlier processing
final_diagnostic = process_metrics(health_data, threshold_map)
print(f"Result: {final_diagnostic}")