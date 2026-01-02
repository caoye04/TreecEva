import itertools

# System health monitoring simulation with red herrings and complex data flow

def analyze_signal(noise_profile, threshold=0.67):
    filtered = [x for x in noise_profile if x > threshold]
    return len(filtered) > 3


def generate_combinations(elements):
    # Distractor: Unused function (dead code path)
    return list(itertools.combinations(elements, 3))


def compute_entropy(data_stream):
    from math import log2
    freq = {}
    for item in data_stream:
        freq[item] = freq.get(item, 0) + 1
    entropy = 0
    total = len(data_stream)
    for count in freq.values():
        p = count / total
        entropy -= p * log2(p)
    return round(entropy, 4)


def extract_diagnostics(raw_trace, mode='A'):
    # Relevant but partially misleading processing
    if mode == 'X':
        return sum(raw_trace) * 0.1
    elif mode == 'B':
        return max(raw_trace) - min(raw_trace)
    else:
        base_score = sum(x ** 0.5 for x in raw_trace if x % 2 == 0)
        adjustment = len([x for x in raw_trace if x > 5])
        return int(base_score) + adjustment

# Irrelevant constants and decoy data structures
CALIBRATION_TABLE = {i: (i * 1.07) for i in range(10, 40)}
TEMP_OFFSETS = [-2, 0, 1, 3, -1, 0, 2]
SYSTEM_FLAGS = [True, False, True, True]

# Core operational data
sensor_readings = [4, 9, 2, 8, 1, 7, 5]
tuned_weights = [0.3, 0.5, 0.8, 0.2, 0.9, 0.1, 0.7]
system_log = [1, 1, 0, 1, 0, 1, 1]

# Misleading intermediate computations (red herrings)
baseline_metric = compute_entropy([1, 2, 2, 3, 3, 3, 4])
noise_floor = [x * 0.05 for x in sensor_readings if x in {2, 4, 8}]
detected_spike = any(x > 0.9 for x in tuned_weights)

# Complex distractor block: unused derived values
aggregated_noise = 0
for i, w in enumerate(tuned_weights):
    if i % 2 == 0:
        aggregated_noise += w * TEMP_OFFSETS[i % len(TEMP_OFFSETS)]

# Simulated signal analysis (partially relevant)
cleaned_data = [x for x in sensor_readings if x >= 2]
signal_valid = analyze_signal([w * 1.5 for w in tuned_weights])

# Hidden dependency chain
intermediate_flag = extract_diagnostics(cleaned_data, mode='C') % 4 == 0

# Decoy transformation using set operations
unique_weights = set(tuned_weights)
adjusted_set = {round(w * 10) for w in unique_weights}
discrepancy = len(unique_weights) - len(adjusted_set) + 1

# Key logic buried in complexity
weight_mask = [int(w > 0.25) for w in tuned_weights]
masked_log = [a * b for a, b in zip(system_log, weight_mask)]
activation_count = sum(masked_log)

# Real computation path (non-obvious)
effective_signals = []
for i in range(len(sensor_readings)):
    if system_log[i] == 1 and tuned_weights[i] > 0.25:
        effective_signals.append(sensor_readings[i] * tuned_weights[i])

smoothed = [x for x in effective_signals if x > 0.5]
total_power = sum(smoothed)

# Final aggregation function combining multiple concepts
def aggregate_metrics(weights, log):
    weighted_sum = 0
    for i, w in enumerate(weights):
        if log[i] == 1:
            contribution = w * (i + 1)
            if i % 2 == 0:
                contribution *= 0.9
            else:
                contribution *= 1.1
            weighted_sum += contribution
    
    # Secondary adjustment based on hidden pattern
    pattern_match = sum(1 for i in range(len(log)-1) if log[i] == 1 and log[i+1] == 1)
    adjustment_factor = 1 + (pattern_match * 0.05)
    
    return int((weighted_sum * adjustment_factor) * 100) // 1  # Scale and discretize

# Critical statement - target of evaluation
final_diagnostic = aggregate_metrics(tuned_weights, system_log)

# Print result as required
print(f"Target result: {final_diagnostic}")