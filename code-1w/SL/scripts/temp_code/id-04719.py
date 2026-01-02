from itertools import combinations
from math import log

# Simulated sensor data processing with diagnostic flags
def collect_diagnostics(sensor_readings):
    diagnostics = []n    total_power = 0
    spike_count = 0
    for reading in sensor_readings:
        if reading > 90:
            spike_count += 1
        total_power += reading ** 0.5
        if reading % 7 == 0:
            diagnostics.append(reading)
    efficiency = total_power / len(sensor_readings)
    return diagnostics, efficiency, spike_count

# Irrelevant helper: computes harmonic mean (not used in final result)
def harmonic_mean(vals):
    if 0 in vals:
        return 0
    return len(vals) / sum(1/v for v in vals)

# Data transformation pipeline
def transform_signal(raw_sequence):
    shifted = [v >> 2 for v in raw_sequence]  # Right shift by 2 bits
    filtered = [v for v in shifted if v & 1]  # Keep only odd values
    return list(set(filtered))  # Remove duplicates

# Core evaluation logic
def compute_entropy(values):
    if not values:
        return 0.0
    freq_map = {}
    for v in values:
        freq_map[v] = freq_map.get(v, 0) + 1
    entropy = 0.0
    total = len(values)
    for count in freq_map.values():
        p = count / total
        if p > 0:
            entropy -= p * log(p, 2)
    return round(entropy, 6)

# Misleading aggregation function (looks important but unused)
def legacy_aggregation(x):
    acc = 0
    for i in range(len(x)):
        acc += x[i] * (i + 1)
    return acc % 100

# Main analysis workflow
def analyze_pattern(data_stream):
    base_values = [x for x in data_stream if x < 50]
    high_freq_components = [x for x in data_stream if x in {23, 42, 47}]
    
    # Generate all 3-element subsequences (unused red herring)
    triplet_combinations = list(combinations(data_stream, 3))
    complex_triplets = [t for t in triplet_combinations if (t[0] ^ t[1] ^ t[2]) % 5 == 0]
    
    # Actual relevant transformation
    processed = transform_signal(base_values)
    entropy_metric = compute_entropy(processed)
    
    # Decoy metrics (never used)
    avg_val = sum(data_stream) / len(data_stream)
    peak_noise = max(data_stream) - min(data_stream)
    
    return processed, entropy_metric, len(complex_triplets)

# Final scoring with conditional weighting
def evaluate_performance(clean_data, cutoff):
    size_factor = len(clean_data)
    sum_value = sum(clean_data)
    xor_checksum = 0
    for val in clean_data:
        if val > cutoff:
            xor_checksum ^= val
        else:
            xor_checksum ^= (val << 1)
    balance_score = sum_value - size_factor * cutoff
    return int(balance_score + xor_checksum)

# Unused recursive function (distractor)
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

# Simulated input data
sensor_input = [84, 23, 91, 42, 77, 47, 63, 35, 28, 14, 98, 49]

# Step 1: Collect diagnostics (produces intermediate results)
diag_list, system_efficiency, spikes = collect_diagnostics(sensor_input)

# Step 2: Analyze pattern (core path)
aggregated_data, entropy_score, triplet_count = analyze_pattern(sensor_input)

# Step 3: Threshold determined from entropy (critical dependency)
threshold = int(entropy_score * 10)

# Step 4: Final evaluation (answer point)
final_score = evaluate_performance(aggregated_data, threshold)

# Print final result as required
print(f"Result: {final_score}")