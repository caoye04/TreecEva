import math

# Simulated sensor array diagnostics with interference
sensor_ids = ['S101', 'S102', 'S103', 'S104']
raw_readings = [89.5, 92.1, 87.3, 95.6]
baseline_calibrations = {sid: 85 + i * 2 for i, sid in enumerate(sensor_ids)}

# Irrelevant auxiliary data (distractor)
diagnostic_logs = {
    'timestamp': '2023-10-15T08:23:45',
    'location': 'Sector 7G',
    'operator': 'Dr. Alvarez',
    'device_version': 'v2.4.1'
}

# Misleading intermediate calculation (dead path)
effective_sensitivity = sum([1.07 ** i for i in range(len(sensor_ids))])
temp_compensation_factor = math.sin(math.pi / 6)  # Constant, never used later

# Core processing chain (relevant)
def normalize_reading(sid, reading):
    base = baseline_calibrations.get(sid, 85)
    return (reading - base) / base

# Apply normalization using list comprehension
normalized_deltas = [normalize_reading(sid, val) for sid, val in zip(sensor_ids, raw_readings)]

# Secondary transformation with red herring variables
adjusted_weights = []
for i, delta in enumerate(normalized_deltas):
    exp_factor = math.exp(-0.3 * i)
    dummy_offset = (i % 3) * 0.05  # Distractor computation
    weight = delta * exp_factor + 0.1  # Actual relevant logic
    adjusted_weights.append(weight)

# Create decoy function that looks important but is unused
def calculate_reliability_index(data, noise_floor=0.02):
    return sum([abs(x) > noise_floor for x in data]) / len(data) if data else 0

# Unused reliability analysis (dead code path)
reliability_scores = []
for w in adjusted_weights:
    score = int(min(10, max(1, abs(w) * 50)))
    reliability_scores.append(score)

# Simulated fault injection mask (partially irrelevant)
fault_mask = [w > 0.25 or i % 2 == 0 for i, w in enumerate(adjusted_weights)]
masked_weights = [w if mask else 0.0 for w, mask in zip(adjusted_weights, fault_mask)]

# Decoy statistical summary (distractor output)
mean_weight = sum(masked_weights) / len(masked_weights)
variance_proxy = sum([(w - mean_weight) ** 2 for w in masked_weights]) / len(masked_weights)

# Real processing begins here — hidden in middle of noise
processing_chain = []
for idx in range(len(sensor_ids)):
    # Composite metric combining multiple concepts
    primary = normalized_deltas[idx]
    secondary = adjusted_weights[idx]
    tertiary = abs(primary - secondary)  # Redundant but looks meaningful
    
    # Critical branching logic with nested conditions
    if primary > 0.05:
        if secondary > 0.15:
            contribution = primary * secondary * 100
        else:
            contribution = primary * 40
    else:
        if idx % 2 == 1:
            contribution = -secondary * 20
        else:
            contribution = primary * 10
    
    processing_chain.append(contribution)

# Another misleading transformation (not part of final result)
sorted_diagnostics = sorted(processing_chain, reverse=True)
top_three_avg = sum(sorted_diagnostics[:3]) / 3 if len(sorted_diagnostics) >= 3 else 0

# Threshold system with fake adaptiveness
thresholds = {
    'critical': 15.0,
    'warning': 5.0,
    'info': 0.5,
    'decay_rate': 0.9  # Unused parameter
}

# Central aggregation function — answer depends on this
def aggregate_metrics(metrics, config):
    total = 0.0
    for val in metrics:
        if val > config['critical']:
            total += val * 0.8
        elif val > config['warning']:
            total += val * 1.1
        elif val > config['info']:
            total += val * 0.9
        else:
            total -= abs(val) * 0.2
    # Final nonlinear adjustment
    if total > 0:
        total = math.log(1 + total) * 5
    else:
        total = total * 0.5
    return round(total, 6)

# Execute critical statement
final_diagnostic = aggregate_metrics(processing_chain, thresholds)

# Print result as required
print(f"Result: {final_diagnostic}")