import itertools

# Simulated sensor array data with noise filtering
raw_signals = [0.48, 0.72, 0.33, 0.91, 0.57, 0.63, 0.29, 0.88]
filtered = [x for x in raw_signals if x > 0.3 and x < 0.8]
smoothed = [round((a + b) / 2, 2) for a, b in zip(filtered, filtered[1:])]  # Moving average
tone_mapping = {i: round(1 / (1 + 0.1 * i), 3) for i in range(len(smoothed))}

# Irrelevant audio processing stubs (dead code path)
def apply_reverb(signal, level):
    return [s * (0.8 + level * 0.2) for s in signal]

def compress_dynamic_range(signal, threshold=0.5):
    return [min(s, threshold) + 0.5 * max(s - threshold, 0) for s in signal]

# Unused calibration routines
baseline_offset = sum([i * 0.01 for i in range(len(raw_signals))])
system_gain = 1.04
reference_pattern = list(itertools.permutations([1, 0, 0], 2))
valid_states = [p for p in reference_pattern if sum(p) > 0]

# Signal coherence computation (distractor)
coherence_pairs = list(itertools.combinations_with_replacement(filtered, 2))
phase_sync = sum(1 for a, b in coherence_pairs if abs(a - b) < 0.1)

# Real processing begins here — performance metric calculation
primary_metrics = [x ** 2 for x in smoothed if x > 0.4]
secondary_metrics = [x for x in smoothed if x <= 0.4]

# Baseline thresholds for evaluation
baseline = {
    'threshold_A': 0.45,
    'penalty_factor': 0.9,
    'boost_window': 2
}

# Decoy state tracker (irrelevant)
current_state = {'mode': 'IDLE', 'level': 0, 'active': False}
state_transition_log = []

def update_state(mode, level):
    nonlocal current_state
    current_state = {'mode': mode, 'level': level, 'active': True}
    state_transition_log.append(f'{mode}:{level}')

# Dummy recursive smoother (never called)
def recursive_denoise(data, depth=0):
    if depth >= 2 or len(data) < 2:
        return data
    reduced = [(a + b) / 2 for a, b in zip(data, data[1:])]
    return recursive_denoise(reduced, depth + 1)

# Core evaluation logic
status_flags = [1 if x > baseline['threshold_A'] else -1 for x in primary_metrics]
positive_count = sum(1 for f in status_flags if f == 1)
negative_count = sum(1 for f in status_flags if f == -1)

# Weighted score accumulation
weight_sequence = [1.0, 1.1, 1.25]  # Boost weights over time
weighted_primary = sum(p * weight_sequence[i % 3] for i, p in enumerate(primary_metrics))
weighted_secondary = sum(s * 0.7 for s in secondary_metrics)

def adjust_for_variance(values, factor):
    mean_val = sum(values) / len(values) if values else 0
    variance = sum((v - mean_val) ** 2 for v in values) / len(values) if values else 0
    return mean_val * (1 + factor * variance)

adjusted_main = adjust_for_variance(primary_metrics, 0.3)
adjusted_aux = adjust_for_variance(secondary_metrics, 0.1)

# Final performance scoring
result_score = 0
if positive_count > negative_count:
    result_score += weighted_primary * baseline['boost_window']
else:
    result_score += weighted_primary * baseline['penalty_factor']

result_score += adjusted_main
result_score -= abs(weighted_secondary - adjusted_aux)

# Distractor: unused normalization chain
normalized_metrics = [m / (sum(primary_metrics) + 0.1) for m in primary_metrics]
scaled_output = [round(n * 100, 1) for n in normalized_metrics]

# Red herring: fake aggregation
aggregate_fingerprint = sum([int(s * 100) for s in smoothed]) % 77

# Actual output
print(f"Result: {result_score}")