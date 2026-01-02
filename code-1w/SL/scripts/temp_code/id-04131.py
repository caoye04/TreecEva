import itertools

# Sensor simulation and diagnostic system
base_offsets = [0.1, -0.2, 0.35, -0.08]
diagnostic_threshold = 0.45
calibration_sequence = (1.1, 0.9, 1.05, 0.95)

# Irrelevant configuration block (distractor)
legacy_modes = {'A': 1, 'B': 2, 'C': None}
temporal_weights = {i: pow(0.9, i) for i in range(6)}
extraneous_flag = False

# Simulated sensor array readings (some corrupted)
sensor_readings = [
    [1.2, 0.8, 1.0, 1.1],
    [0.7, 1.3, 0.9, 1.0],
    [1.5, 0.5, 1.1, 0.9],
    [0.4, 1.6, 0.8, 1.2]
]

# Auxiliary transformation (partially relevant)
def apply_calibration(readings, calib):
    return [r * calib[i % len(calib)] for i, r in enumerate(readings)]

# Red herring function – looks important but unused
def compute_legacy_score(data, mode='A'):
    if mode == 'C': return 0
    weight = legacy_modes.get(mode, 1)
    return sum(d ** 2 for d in data) * weight

# Core processing pipeline
transformed_readings = []
for idx, reading_set in enumerate(sensor_readings):
    adjusted = apply_calibration(reading_set, calibration_sequence)
    offset_val = base_offsets[idx % len(base_offsets)]
    shifted = [val + offset_val for val in adjusted]
    transformed_readings.append(shifted)

# Mask generation using set operations (meaningful distractor)
available_indices = set(range(4))
corrupted_sensors = {2}
valid_indices = available_indices - corrupted_sensors

# Filtering logic with conditional expressions
filtered_metrics = []
for t_read in transformed_readings:
    # Only use valid sensors (index 2 excluded)
    selected = [t_read[i] for i in valid_indices]
    avg_val = sum(selected) / len(selected)
    
    # Apply dynamic threshold filter
    meets_criteria = avg_val > diagnostic_threshold
    
    # Use conditional expression to decide inclusion format
    entry = {'value': avg_val, 'status': 'valid'} if meets_criteria else {'value': avg_val, 'status': 'discarded'}
    
    # Only include valid entries
    if entry['status'] == 'valid':
        filtered_metrics.append(entry['value'])

# Dead code path – simulates alternate processing
if extraneous_flag:
    fallback_data = list(itertools.chain.from_iterable(transformed_readings))
    filtered_metrics = [x for x in fallback_data if x > 0.5]

# Secondary filtering based on variance (additional relevance)
def calculate_variance(data):
    mean = sum(data) / len(data)
    return sum((x - mean) ** 2 for x in data) / len(data)

variance_capped_metrics = [
    x for x in filtered_metrics 
    if x <= diagnostic_threshold + 0.3
]

# Decoy transformation chain
aggregated_snapshot = {
    'raw_count': len(filtered_metrics),
    'capped_count': len(variance_capped_metrics),
    'sum_total': sum(filtered_metrics),
    'peak': max(filtered_metrics) if filtered_metrics else 0
}

snapshot_values = list(aggregated_snapshot.values())
# Unused transformation - red herring
weighted_moments = [
    val * pow(i + 1, 0.5) for i, val in enumerate(snapshot_values)
]

# Critical computation path
rolling_pairs = list(itertools.pairwise(variance_capped_metrics))

# Compute interaction score from adjacent valid metrics
interaction_score = 0
for a, b in rolling_pairs:
    diff = abs(a - b)
    product = a * b
    if diff < 0.5:
        interaction_score += product * (1 - diff)

# Final diagnostic depends only on interaction_score and capped count
# All prior complexity serves as interference
final_diagnostic = 0
if variance_capped_metrics:
    density_factor = len(variance_capped_metrics) / 4.0
    final_diagnostic = interaction_score * density_factor + len(variance_capped_metrics)
else:
    final_diagnostic = -999.0

# Target result output
print(f"Result: {final_diagnostic}")