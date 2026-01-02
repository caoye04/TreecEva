import itertools

# Simulated system metrics from performance monitoring
time_metrics = [120, 150, 135, 160, 145]
error_rates = [0.01, 0.03, 0.02, 0.05, 0.04]
throughput = [85, 90, 88, 92, 87]

# Irrelevant auxiliary data (distractor)
legacy_system_flags = {k: v for k, v in enumerate(['A', 'B', 'C', 'D', 'E'])}
unused_buffer = [0] * 100

# Weight configuration for evaluation (some weights are decoys)
full_weight_schema = {
    'latency': 0.4,
    'errors': 0.3,
    'throughput': 0.2,
    'compatibility': 0.1,  # unused in final calc
    'scalability': 0.05   # unused
}

# Active benchmark weights (subset used in actual computation)
benchmark_weights = {k: full_weight_schema[k] for k in ['latency', 'errors', 'throughput']}

# Misleading intermediate transformation (dead path)
def apply_legacy_correction(data):
    return [x * 0.95 for x in data if x > 100]  # never called

def normalize(data):
    min_val, max_val = min(data), max(data)
    if max_val == min_val:
        return [0.5 for _ in data]
    return [(x - min_val) / (max_val - min_val) for x in data]

def calculate_stability_indicator(seq):
    diffs = [abs(seq[i] - seq[i-1]) for i in range(1, len(seq))]
    return sum(diffs) / len(diffs) if diffs else 0

# Red herring function that looks important but is unused
def compute_compatibility_index(flags):
    return sum(ord(c) for c in flags.values()) % 100

# Real processing begins here
normalized_time = normalize([1/x for x in time_metrics])  # Inverse for faster = better
normalized_errors = normalize([1 - e for e in error_rates])  # Lower error = higher score
normalized_tput = normalize(throughput)

# Composite metric aggregation using weighted average
def aggregate_performance(components_list, weights):
    weighted_sum = 0.0
    total_weight = sum(weights.values())
    
    # Simulate multi-step fusion with distraction
    fusion_sequence = list(itertools.permutations(['a', 'b', 'c']))[:3]  # irrelevant
    temp_fusion_key = ''.join(fusion_sequence[0]) if fusion_sequence else 'abc'
    
    # Actual weighting
    for i, (name, comp) in enumerate(components_list.items()):
        if name in weights:
            weighted_sum += weights[name] * sum(comp) / len(comp)
    
    return weighted_sum / total_weight

# Additional distractor: fake decomposition
fake_decomposition = dict(zip(['part_x', 'part_y'], [(1,2), (3,4)]))

# Build metrics container
metrics = {
    'latency': normalized_time,
    'errors': normalized_errors,
    'throughput': normalized_tput,
    'ghost_metric': [0, 0]  # unused
}

# Spurious string-based validation (looks important, not used)
validation_key = "PERF_CHECK_" + "V2"
is_validated = validation_key.startswith("PERF") and len(validation_key) == 11

# Core evaluation logic
stability_bias = calculate_stability_indicator(time_metrics) * 0.01
offset_compensation = len([x for x in error_rates if x > 0.02]) * 0.005  # minor offset

# Final performance score calculation
def evaluate_performance(mets, wts):
    base_score = aggregate_performance(mets, wts)
    
    # Apply subtle corrections (small impact)
    corrected = base_score - stability_bias - offset_compensation
    
    # Dummy control flow to obscure logic
    if corrected > 1.0:
        corrected = 1.0
    elif corrected < 0.0:
        corrected = 0.0
    
    # Final scaling to integer-like score
    return int(round(corrected * 1000))

# Execute main logic
final_score = evaluate_performance(metrics, benchmark_weights)

# Print result as required
print(f"Target result: {final_score}")