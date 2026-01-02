import math

def analyze_signal_integrity(raw_samples, noise_floor):
    filtered_samples = [s for s in raw_samples if abs(s) > noise_floor]
    squared_energy = sum([x ** 2 for x in filtered_samples])
    phase_shift = 0.0
    for i in range(len(filtered_samples)):
        if i % 3 == 0:
            phase_shift += math.sin(filtered_samples[i] * 0.1)
    return squared_energy, phase_shift


def evaluate_harmonic_distortion(levels):
    harmonics = set()
    for l in levels:
        if l > 0:
            for factor in range(2, 6):
                harmonics.add(l * factor)
    reference_tones = {100, 200, 300, 400, 500}
    interference = harmonics.intersection(reference_tones)
    return len(interference), harmonics

def compute_stability_index(timestamps, values):
    if len(timestamps) < 2:
        return 0.0
    time_deltas = [timestamps[i+1] - timestamps[i] for i in range(len(timestamps)-1)]
    value_changes = [abs(values[i+1] - values[i]) for i in range(len(values)-1)]
    stability = 0.0
    for td, vc in zip(time_deltas, value_changes):
        if td > 0:
            stability += vc / td
    return stability / len(time_deltas) if time_deltas else 0.0

# Irrelevant helper (decoy)
def auxiliary_calib_adjust(x):
    return (x * 1.05) + 2.7

# Unused function (dead path)
def deprecated_normalization(data):
    max_val = max(data) if data else 1
    return [d / max_val for d in data]

# Misleading intermediate variables
baseline_offset = 42
compensation_factor = 0.88
reference_anchor = 987.6

# Simulated sensor inputs
sensor_readings = [0.1, -0.3, 0.5, 0.0, 0.7, -0.2, 1.1, 0.9, 0.0, 1.3]
timestamp_sequence = [10, 15, 23, 35, 41, 50, 62, 70, 85, 90]
operational_levels = [50, 100, 150, 200, 250]

# Distraction: complex but unused transformation chain
transformed_chain = [
    math.log(abs(x) + 1) * 1.7 for x in sensor_readings
]
processed_chain = [
    auxiliary_calib_adjust(y) for y in transformed_chain if y > 0.5
]

# Real signal analysis
energy_metric, phase_correction = analyze_signal_integrity(sensor_readings, 0.2)
interference_count, all_harmonics = evaluate_harmonic_distortion(operational_levels)

# Fake diagnostic (red herring)
current_compliance = (energy_metric * 0.9 + phase_correction * 5.0) / 100.0

# Another distraction block
snapshot_buffer = []
for val in sensor_readings:
    if val > 0.6:
        snapshot_buffer.append(val ** 2 + 0.1)

# Key data structure with relevant and irrelevant fields
reliability_log = {
    'primary_energy': energy_metric,
    'phase_sync': phase_correction,
    'instability_score': compute_stability_index(timestamp_sequence, sensor_readings),
    'harmonic_risk': interference_count,
    'baseline': baseline_offset,
    'debug_trace': [0.1, 0.2],
    'calibration_state': False
}

# Threshold logic with distractor condition
threshold_filter = lambda x: x > 0.5

# Core computation buried in abstraction
final_diagnostic = 0.0
def aggregate_metrics(log, threshold_fn):
    total = 0.0
    count = 0
    # Mix of relevant and irrelevant checks
    if 'primary_energy' in log and log['primary_energy'] > 0:
        total += log['primary_energy']
        count += 1
    if 'instability_score' in log:
        normalized_instability = log['instability_score'] * 100
        if threshold_fn(normalized_instability):
            total += normalized_instability
            count += 1
    if 'harmonic_risk' in log:
        total += log['harmonic_risk'] * 10
        count += 1
    # This field looks important but isn't used
    if 'phase_sync' in log and log['phase_sync'] > 0.1:
        total += 5  # minor boost
    return round(total / count, 6) if count else 0.0

# Final assignment - critical execution point
final_diagnostic = aggregate_metrics(reliability_log, threshold_filter)

print(f"Result: {final_diagnostic}")