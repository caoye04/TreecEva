import math

# Simulated bio-signature analysis system for cellular health evaluation

def generate_entropy_map(cell_id):
    # Irrelevant complex-looking computation (dead end)
    phase_shift = (cell_id * 7) % 13
    entropy_values = [((i ** 2 + phase_shift) % 11) / 17 for i in range(10)]
    return sum(entropy_values)  # Unused in final logic

def evaluate_resilience_index(age_factor):
    # Distractor function: looks important but not used
    if age_factor < 0:
        return 0
    index = 1.0
    for k in range(1, 6):
        index += math.sin(age_factor / k)
    return round(index, 4)

def compute_phase_vector(elements):
    # Another red herring: complex code path that feeds unused variables
    transformed = set()
    for e in elements:
        transformed.add((e * 11) % 19)
    shifted = [v ^ 7 for v in sorted(transformed)]
    return shifted  # Never actually used

# Core data structures with mixed relevance
baseline_readings = {
    'ref_a': 0.87,
    'ref_b': 1.03,
    'threshold': 0.95,
    'tolerance_window': 0.12
}

health_signature = [
    {'metric': 'voltage_potential', 'value': 0.91, 'weight': 0.6},
    {'metric': 'ion_flow', 'value': 0.97, 'weight': 0.8},
    {'metric': 'membrane_stability', 'value': 0.83, 'weight': 1.0},
    {'metric': 'channel_activity', 'value': 1.05, 'weight': 0.7}
]

# Irrelevant global variables (distractors)
cell_cycle_phase = 'G2'
cycle_duration = 23.7
mitosis_flag = False
replication_log = [False] * 5

# Decoy intermediate calculations
raw_coherence = 0
for entry in health_signature:
    raw_coherence += entry['value'] * 0.25  # Misleading average

adjusted_reference = baseline_readings['ref_a'] * 1.05  # Looks like correction, unused

# Key lambda: filters and weights valid metrics above threshold
weight_filter = lambda x: x['value'] >= baseline_readings['threshold'] - baseline_readings['tolerance_window']

# Actual relevant logic begins here — well hidden among noise
filtered_metrics = list(filter(weight_filter, health_signature))

# Compute composite score using only qualifying metrics
composite_score = 0.0
for metric in filtered_metrics:
    deviation = abs(metric['value'] - baseline_readings['ref_b'])
    penalty = deviation * metric['weight']
    composite_score += penalty

# Secondary adjustment based on modular consistency
consistency_key = 0
for i, m in enumerate(filtered_metrics):
    consistency_key += (int(m['value'] * 100) + i) % 7

# Linear search for dominant anomaly (another real step)
dominant_anomaly = None
for m in health_signature:
    if m['value'] > baseline_readings['ref_b'] + 0.05:
        dominant_anomaly = m['metric']
        break

# Simulate corrective response vector (partially relevant)
correction_vector = []
if dominant_anomaly:
    for i in range(len(filtered_metrics)):
        correction_vector.append((consistency_key + i) % 5)

# Real signal: aggregate diagnostic from multiple sources
aggregation_seeds = [3, 1, 4, 1, 5]
seed_sum = sum(aggregation_seeds[:len(correction_vector)]) if correction_vector else 0

# Final diagnostic calculation — depends on composite_score, consistency_key, and seed_sum
intermediate_signal = composite_score * 100 + consistency_key
final_diagnostic = int(intermediate_signal - seed_sum * 2.5)

# Print result as required
print(f"Result: {final_diagnostic}")