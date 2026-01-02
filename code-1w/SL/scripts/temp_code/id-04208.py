import math

# Simulated sensor data processing with diagnostic analysis
raw_samples = [i * 0.5 for i in range(100)]
baseline_offset = 2.5
noise_floor = 0.15
sample_window = 10

# Irrelevant calibration constants (distractors)
calibration_key = 0.987
reference_checksum = 54321
temp_buffer = [0] * 15
device_id = 'SENS-ALPHA-9'
activation_epoch = 1678886400

# Signal transformation phase
filtered_samples = []
for s in raw_samples:
    corrected = (s - baseline_offset) * calibration_key
    if abs(corrected) > noise_floor:
        filtered_samples.append(round(corrected, 3))

# Dead code path - never executed due to prior filtering (red herring)
if len(temp_buffer) > 100:
    for i in range(len(temp_buffer)):
        temp_buffer[i] = math.sin(i) * reference_checksum

# Actual relevant processing begins here
aggregated_metrics = {
    'sum': 0.0,
    'count_above_threshold': 0,
    'peaks': [],
    'entropy_estimate': 0.0
}

threshold = 3.0
for val in filtered_samples:
    aggregated_metrics['sum'] += val
    if val > threshold:
        aggregated_metrics['count_above_threshold'] += 1
        if len(aggregated_metrics['peaks']) < 5:  # Only keep first 5 peaks
            aggregated_metrics['peaks'].append(val)

# Compute entropy-like measure using set cardinality (key concept)
sample_set = set(filtered_samples)
distinct_count = len(sample_set)
aggregated_metrics['entropy_estimate'] = -sum(math.log(1 / distinct_count) for _ in range(distinct_count)) if distinct_count else 0.0

# Secondary transformation: accumulate and scale
accumulated_energy = sum(x**2 for x in filtered_samples)
normalized_power = accumulated_energy / len(filtered_samples) if filtered_samples else 0

# Decoy function - looks important but unused (misleading intermediate)
def compute_integrity_score(data):
    score = 0
    for d in data:
        score += math.cos(d) * 0.1
    return score

# Unused recursive red herring
def integrate_recursive(arr, idx=0):
    if idx >= len(arr):
        return 0
    return arr[idx] + 0.5 * integrate_recursive(arr, idx + 1)

# Real processing chain
processed_samples = []
for i in range(0, len(filtered_samples), sample_window):
    window = filtered_samples[i:i + sample_window]
    if len(window) == sample_window:
        window_avg = sum(window) / len(window)
        processed_samples.append(round(window_avg, 3))

# Another irrelevant buffer
status_log = []
for tick in range(5):
    status_log.append(f"System check {tick}: OK")

# Core diagnostic logic (target execution point)
def analyze_signal(metrics):
    base_value = metrics['sum']
    peak_influence = 0
    for p in metrics['peaks']:
        peak_influence += math.sqrt(p)
    
    # Set-based dispersion factor
    dispersion_factor = len(set(round(x, 1) for x in metrics['peaks'])) if metrics['peaks'] else 1
    
    # Final computation
    result = base_value + peak_influence * dispersion_factor
    result -= metrics['entropy_estimate']
    return int(round(result))

# Final assignment (critical statement)
final_diagnostic = analyze_signal({
    'sum': aggregated_metrics['sum'],
    'peaks': aggregated_metrics['peaks'],
    'entropy_estimate': aggregated_metrics['entropy_estimate']
})

print(f"Result: {final_diagnostic}")