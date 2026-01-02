from collections import defaultdict, Counter
import itertools

# Simulated telemetry data from system sensors
telemetry_streams = [
    [1, 0, 1, 1, 0, 1, 0, 0],
    [0, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 1, 1, 1]
]

# Irrelevant signal processing (distractor)
def analyze_noise_pattern(stream):
    noise_count = 0
    for bit in stream:
        if bit == 0:
            noise_count += 1
    return noise_count * 0.5

# Unused transformation function (dead code path)
def transform_signal(stream):
    return [x ^ 1 for x in stream][::-1]

# Misleading metric with decoy usage
baseline_offset = 3.14159
temporal_factor = sum(len(s) for s in telemetry_streams) / 2

# Core data aggregation
aggregated_bits = defaultdict(int)
for i, stream in enumerate(telemetry_streams):
    for j, bit in enumerate(stream):
        aggregated_bits[j] += bit

# Bit frequency analysis (relevant)
frequency_counter = Counter(aggregated_bits.values())
dominant_frequency = frequency_counter.most_common(1)[0][1]

# Simulate feature extraction from bit patterns
pattern_matrix = []
for stream in telemetry_streams:
    runs = []
    current_run = 1
    for k in range(1, len(stream)):
        if stream[k] == stream[k-1]:
            current_run += 1
        else:
            runs.append(current_run)
            current_run = 1
    runs.append(current_run)
    pattern_matrix.append(runs)

# Decoy statistical calculation (irrelevant)
avg_runs = sum(len(seq) for seq in pattern_matrix) / len(pattern_matrix)
run_entropy = 0
for seq in pattern_matrix:
    for r in seq:
        if r > 1:
            run_entropy += r * 0.1

# Real computation begins: weight assignment based on position impact
position_weights = {}
for pos in aggregated_bits:
    # Weight depends on both frequency and positional stability
    stability_score = abs(pos - 3.5) + 1  # Center-biased
    position_weights[pos] = (aggregated_bits[pos] + 1) / stability_score

# Control flow obfuscation with nested conditions (misleading branches)
optimization_mode = True
scaling_factor = 1.0
if optimization_mode:
    if dominant_frequency > 2:
        scaling_factor = 0.8
    else:
        scaling_factor = 1.2
else:
    scaling_factor = 1.5  # Dead branch (never reached)

# Generate combinatorial feature set (partial distractor)
combinatorial_features = []
for indices in itertools.combinations([0,1,2,3,4,5,6,7], 2):
    i1, i2 = indices
    if i1 in aggregated_bits and i2 in aggregated_bits:
        combo_score = (aggregated_bits[i1] + aggregated_bits[i2]) / (abs(i1 - i2) + 1)
        combinatorial_features.append(combo_score)

# Only first few features are actually used
trimmed_features = combinatorial_features[:4]
feature_bonus = sum(f for f in trimmed_features if f > 1.0)

# Key metric data construction (relevant path)
metric_data = {
    'base_strength': sum(aggregated_bits.values()),
    'pattern_consistency': len([v for v in aggregated_bits.values() if v >= 2]),
    'rare_position_penalty': len([v for v in aggregated_bits.values() if v == 1]),
    'feature_enhancement': feature_bonus
}

# Weight configuration (critical)
weights = {
    'strength': 1.2,
    'consistency': 2.0,
    'penalty': -0.8,
    'enhancement': 1.5
}

# Auxiliary unused scoring method (decoy)
def legacy_scoring(data):
    return (data['base_strength'] * 0.9 + 
            data['pattern_consistency'] * 1.1)

# Main evaluation logic
processed_values = []
for key in metric_data:
    normalized_key = key.replace('_', '')
    if 'strength' in normalized_key:
        processed_values.append(metric_data[key] * weights['strength'])
    elif 'consistency' in normalized_key:
        processed_values.append(metric_data[key] * weights['consistency'])
    elif 'penalty' in normalized_key:
        processed_values.append(metric_data[key] * weights['penalty'])
    elif 'enhancement' in normalized_key:
        processed_values.append(metric_data[key] * weights['enhancement'])

# Final score calculation
final_score = int(sum(processed_values) * scaling_factor + baseline_offset - run_entropy)

# Additional red herring computations (irrelevant)
signal_volume = sum(analyze_noise_pattern(s) for s in telemetry_streams)
theoretical_max = len(telemetry_streams) * 8
efficiency_ratio = final_score / theoretical_max if theoretical_max else 0

# Output result
print(f"Result: {final_score}")