import itertools

# Simulated sensor array data (frequency bins)
frequency_readings = [12, 15, 22, 8, 41, 33, 29, 11]

# Irrelevant auxiliary data (distractor)
aux_temperatures = [23.4, 24.1, 22.8, 25.0, 23.9]
baseline_offsets = {i: val * 0.1 for i, val in enumerate(frequency_readings)}

# Noise filtering configuration (partially relevant)
filter_kernel = lambda x: x if x > 10 else 0
smoothed = list(map(filter_kernel, frequency_readings))

# Decoy function – looks important but unused in final path
def legacy_process(data):
    return [d * 0.95 for d in data if d > 12]

# Signal normalization using combinatorics-inspired weighting
combinations = list(itertools.combinations([1, 2, 3, 4], 3))
weight_sequence = [len(set(combo)) for combo in combinations]  # Always 3, but disguised
normalization_factor = sum(weight_sequence) / len(weight_sequence)

# Real preprocessing step
scaled_readings = [r * normalization_factor for r in smoothed]

# Threshold map generation with set operations (relevant)
active_indices = {i for i, v in enumerate(scaled_readings) if v > 20}
edge_set_a = {1, 3, 5, 7}
edge_set_b = {2, 5, 6, 7}
overlap_edges = edge_set_a & edge_set_b  # {5, 7}

threshold_map = {}
for idx in range(len(scaled_readings)):
    if idx in active_indices:
        threshold_map[idx] = 25 + len(overlap_edges) * 2
    else:
        threshold_map[idx] = 15

# Dead code path (misleading control flow)
if len(aux_temperatures) > 10:
    scaled_readings = [s * 1.1 for s in scaled_readings]
elif any(t > 30 for t in aux_temperatures):
    scaled_readings = [s * 0.9 for s in scaled_readings]
else:
    pass  # No effect, but distracts

# Data structuring via tuple unpacking (relevant)
processed_data = []
for i, val in enumerate(scaled_readings):
    category = 'HIGH' if val > threshold_map[i] else 'LOW'
    processed_data.append((i, val, category))

# Core analysis logic
state_transitions = 0
current_state = 'LOW'
for _, value, category in processed_data:
    if current_state == 'LOW' and category == 'HIGH':
        state_transitions += 1
        current_state = 'HIGH'
    elif current_state == 'HIGH' and category == 'LOW':
        current_state = 'LOW'

# Secondary metric (red herring)
avg_magnitude = sum(scaled_readings) / len(scaled_readings)

# Final diagnostic calculation (key statement)
def analyze_signal(data, thresholds):
    high_count = sum(1 for _, _, cat in data if cat == 'HIGH')
    weighted_score = high_count * 100 + state_transitions * 10
    
    # Distractor computation (unused)
    fake_dependency = avg_magnitude * 0.5
    dummy_adjustment = len(thresholds.get(99, 'N/A')) * 0  # Invalid key, returns 0
    
    return weighted_score - 42  # Final adjustment

final_diagnostic = analyze_signal(processed_data, threshold_map)
print(f"Target result: {final_diagnostic}")