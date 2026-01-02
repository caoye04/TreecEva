import math

# Simulated sensor array diagnostics with interference handling

def analyze_signal_strength(raw_readings):
    filtered = [x for x in raw_readings if x > -50]
    baseline = sum(filtered) / len(filtered)
    adjusted = [math.log(abs(x) + 1) * 0.85 for x in filtered]
    return adjusted


def detect_anomalies(signal_data):
    anomalies = set()
    for i, val in enumerate(signal_data):
        if val < 0 or math.isnan(val):
            anomalies.add(i)
    # Irrelevant computation (distractor)
    shadow_copy = [x * 1.5 for x in signal_data if x > 10]
    outlier_score = len(shadow_copy) * 0.3
    return anomalies


def normalize_phase(signal_array):
    min_val, max_val = min(signal_array), max(signal_array)
    range_val = max_val - min_val
    if range_val == 0:
        return [0.5] * len(signal_array)
    return [(x - min_val) / range_val for x in signal_array]


def evaluate_system_integrity(flags):
    critical_errors = 0
    for key, status in flags.items():
        if 'fault' in key and status:
            critical_errors += 1
    # Dead code path (misleading)
    if critical_errors == 0:
        temp_status = {k: False for k in flags}
        for k in temp_status:
            temp_status[k] = not temp_status[k]
    return critical_errors > 0

# Composite metric calculation (core logic)
def compute_coherence_index(norm_signals):
    squared = [x ** 2 for x in norm_signals]
    mean_sq = sum(squared) / len(squared)
    root_mean_sq = math.sqrt(mean_sq)
    # Red herring: unused transformation
    fft_approx = [abs(math.sin(x * math.pi)) for x in norm_signals]
    return round(root_mean_sq * 1000) / 1000

# Misleading auxiliary function (never called in correct path)
def deprecated_calibration(data):
    return [x + 2 for x in data if x % 2 == 0]

# Decoy state variables
system_state_backup = {'mode': 'standby', 'last_sync': 1200}
system_state_backup['diagnostics'] = [0] * 5

# Real flag set
system_flags = {
    'overheat_fault': False,
    'pressure_warning': True,
    'calibration_lock': False,
    'comms_jitter': True,
    'backup_active': False
}

# Raw sensor input
raw_sensor_data = [23.5, -45.2, 78.9, 12.1, -60.3, 95.7, 101.2, 55.8]

# Signal processing pipeline
processed_signals = analyze_signal_strength(raw_sensor_data)
anomaly_set = detect_anomalies(processed_signals)

# Normalize signals for coherence analysis
normalized_signals = normalize_phase(processed_signals)

# Compute secondary metrics (some used, some not)
coherence_index = compute_coherence_index(normalized_signals)

# Unused intermediate (distraction)
drift_analysis = [x for x, i in zip(normalized_signals, range(len(normalized_signals))) if i % 2 == 1]
smoothing_factor = 0.89
smoothed = [drift_analysis[0]]
for x in drift_analysis[1:]:
    smoothed.append(smoothed[-1] * smoothing_factor + x * (1 - smoothing_factor))

# Aggregate function that determines final result
def aggregate_metrics(norm_sig, flags):
    # Logical combination of multiple factors
    base_score = sum(norm_sig) * 100
    fault_count = sum(1 for v in flags.values() if v)
    adjustment = -50 if fault_count >= 2 else 25
    
    # Bit manipulation distraction
    binary_tag = 0
    for i, val in enumerate(norm_sig):
        if val > 0.5:
            binary_tag |= (1 << (i % 6))  # irrelevant bit setting
    
    # Final composition
    entropy_component = 0
    for x in norm_sig:
        if x > 0:
            entropy_component -= x * math.log(x)
    
    # Core answer logic
    final_score = base_score + adjustment + (int(entropy_component * 100))
    
    # Distractor: complex but unused structure
    diagnostic_tree = {
        'root': {
            'left': {'value': binary_tag},
            'right': {'value': int(coherence_index * 100)}
        }
    }
    
    return int(final_score)

# Execution point of interest
final_diagnostic = aggregate_metrics(normalized_signals, system_flags)

# Output result
print(f"Result: {final_diagnostic}")