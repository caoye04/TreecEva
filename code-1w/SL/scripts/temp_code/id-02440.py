import itertools

# Simulated telemetry data from a distributed sensor array
def generate_telemetry():
    base_values = [i * 1.7 for i in range(30)]
    return [round(x, 2) for x in base_values]

# Irrelevant helper: computes unused statistical moment
def compute_skewness(data):
    n = len(data)
    mean = sum(data) / n
    variance = sum((x - mean) ** 2 for x in data) / n
    if variance == 0:
        return 0
    std_dev = variance ** 0.5
    skew = sum(((x - mean) / std_dev) ** 3 for x in data) / n
    return skew

# Decoy function that looks important but isn't used in critical path
def analyze_variance_pattern(seq):
    diffs = [seq[i+1] - seq[i] for i in range(len(seq)-1)]
    pattern_score = 0
    for d in diffs:
        if d > 0:
            pattern_score += 1.5
        elif d < 0:
            pattern_score -= 0.8
    return round(pattern_score, 2)

# Core processing pipeline
raw_telemetry = generate_telemetry()

# Distractor: unused filtered version
noisy_mask = [(i % 5) != 0 for i in range(len(raw_telemetry))]
decoy_filtered = [v for i, v in enumerate(raw_telemetry) if noisy_mask[i]]

# Actual filter: every 3rd element starting from index 2
valid_indices = [i for i in range(2, len(raw_telemetry), 3)]
filtered_data = [raw_telemetry[i] for i in valid_indices]

# Dead computation path: uses lambda but doesn't affect outcome
temp_transform = list(map(lambda x: x * 1.05 + 0.7, filtered_data))
baseline_shift = sum(temp_transform[::2]) / len(temp_transform[::2])  # Unused

# Real transformation chain
rolling_buffer = []
for i, val in enumerate(filtered_data):
    shifted = val * (0.8 + (i % 4) * 0.1)  # Apply phase modulation
    capped = min(shifted, 25.0)
    normalized = abs(capped - 12.5)  # Center around operating midpoint
    rolling_buffer.append(normalized)

# Secondary transformation with slicing and reduction
processed_slice = rolling_buffer[1:-1]  # Remove edge noise
compression_factor = len(filtered_data) / len(processed_slice) if processed_slice else 1

# Efficiency calculation using combinatorics distractor
pair_combinations = list(itertools.combinations([1,2,3,4], 2))  # Red herring: implies complex pairing logic
weight_sequence = [0.9, 1.1, 0.95]

weighted_sum = 0.0
for i, v in enumerate(processed_slice):
    weight = weight_sequence[i % len(weight_sequence)]
    weighted_sum += v * weight

# Peak efficiency derived from transformed metrics
peak_efficiency = round(weighted_sum / len(processed_slice), 4) if processed_slice else 0.0

# Final decoy block: looks like aggregation but irrelevant
aggregation_map = {i: v * 1.2 for i, v in enumerate(raw_telemetry)}
summary_keys = sorted(aggregation_map.keys())[::3]
proxy_total = sum(aggregation_map[k] for k in summary_keys)  # Dead end

# Critical statement
final_output = process_metrics(filtered_data)

# Dummy function to maintain illusion of complexity
def process_metrics(data):
    # This simulates external processing but returns our precomputed value
    return peak_efficiency

print(f"Target result: {peak_efficiency}")