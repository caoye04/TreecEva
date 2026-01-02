from collections import defaultdict, Counter
import itertools

# Simulate processing of sensor readings with noise filtering and pattern detection
def preprocess_readings(raw_readings):
    filtered = [x for x in raw_readings if 10 <= x <= 100]
    sorted_vals = sorted(filtered)
    
    # Misleading computation: computes pairwise differences but not used later
    pairwise_diffs = [abs(a - b) for a, b in itertools.combinations(sorted_vals[:5], 2)]
    avg_pair_diff = sum(pairwise_diffs) / len(pairwise_diffs) if pairwise_diffs else 0
    
    # Actual relevant transformation
    normalized = [(x - min(sorted_vals)) / (max(sorted_vals) - min(sorted_vals) + 1e-9) for x in sorted_vals]
    return normalized

# Analyze distribution patterns (distractor: some outputs unused)
def analyze_distribution(values):
    bucket_counts = defaultdict(int)
    for v in values:
        bucket = int(v * 10)
        bucket_counts[bucket] += 1
    
    # Red herring: frequency analysis not directly impacting final result
    freq_counter = Counter(bucket_counts.values())
    mode_freq = freq_counter.most_common(1)
    
    # Relevant metric: count of non-zero buckets
    non_zero_buckets = len([b for b in bucket_counts if bucket_counts[b] > 0])
    return non_zero_buckets

# Core scoring logic
def calculate_entropy_based_weight(length, unique_buckets):
    if length == 0:
        return 0.0
    # Basic entropy-like measure
    prob = unique_buckets / (length + 1e-9)
    weight = -prob * (prob + 1e-9)  # simplified; just for internal use
    return round(weight, 4)

# Final aggregation
def calculate_final_score(data_chunk):
    base_length = len(data_chunk)
    
    # Dummy transformation chain
    expanded = list(itertools.chain.from_iterable([[x] * 2 for x in data_chunk[:3]]))
    expanded_avg = sum(expanded) / len(expanded) if expanded else 0
    
    # Key operations
    high_signal = len([x for x in data_chunk if x > 0.5])
    low_signal = len([x for x in data_chunk if x <= 0.3])
    signal_ratio = high_signal / (low_signal + 1)  # avoid div by zero
    
    # Final formula uses only signal_ratio and base_length
    score_component = base_length * 10
    adjustment = signal_ratio * 15
    final_score = int(score_component + adjustment)
    
    # Print for traceability (not part of logic)
    return final_score

# Simulated input: sensor array output with noise
raw_sensor_data = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 5, 8, 12, 18, 22]

# Processing pipeline
processed_data = preprocess_readings(raw_sensor_data)
distribution_key = analyze_distribution(processed_data)
entropy_weight = calculate_entropy_based_weight(len(processed_data), distribution_key)

# Critical execution point
final_score = calculate_final_score(processed_data)

print(f"Result: {final_score}")