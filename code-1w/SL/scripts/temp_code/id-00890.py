import math

# Simulated sensor array data (real and irrelevant)
sensor_ids = [101, 102, 103, 104, 105]
base_frequencies = {101: 50.0, 102: 60.0, 103: 45.5, 104: 55.0, 105: 40.0}
calibration_offsets = {101: 0.12, 102: 0.08, 103: 0.15, 104: 0.10, 105: 0.05}

# Irrelevant metadata
device_location = 'Grid Sector 7'
operator_id = 'OP-992'
last_maintenance = '2023-10-05'

# Raw signal inputs (some relevant, some red herrings)
raw_signals = [
    [1.2, 1.5, 1.3, 1.7, 2.0, 1.8],
    [0.8, 0.9, 1.1, 1.0, 0.7, 0.6],
    [2.5, 2.3, 2.6, 2.4, 2.7, 2.5],
    [0.3, 0.4, 0.2, 0.5, 0.6, 0.4],
    [1.0, 1.1, 0.9, 1.2, 1.0, 1.1]
]

# Distractor: unused signal set
legacy_signals = [
    [3.1, 3.0, 3.2],
    [0.1, 0.2, 0.1]
]

# Decoy function that looks important but isn't used
def legacy_diagnostic(data):
    return sum([sum(d) for d in data]) * 0.1

# Signal quality tracker (partially relevant)
signal_quality = {
    sid: 'HIGH' if freq > 50.0 else 'LOW' for sid, freq in base_frequencies.items()
}

# Intermediate processing with distractors
noisy_indices = {101: [0, 4], 104: [5]}
smoothing_factor = 0.85

# Real processing steps
filtered_signals = []
for i, sig in enumerate(raw_signals):
    filtered = []
    for j, val in enumerate(sig):
        sensor_id = sensor_ids[i]
        offset = calibration_offsets[sensor_id]
        adjusted = val + offset
        
        # Apply smoothing only to non-noisy points
        if sensor_id in noisy_indices and j in noisy_indices[sensor_id]:
            adjusted *= 1.1  # slight boost on noisy readings
        
        # Red herring: frequency-based modulation (unused later)
        nominal_freq = base_frequencies[sensor_id]
        modulated = adjusted * (nominal_freq / 50.0) if nominal_freq > 45 else adjusted
        
        filtered.append(adjusted)  # only adjusted value is actually used
    
    filtered_signals.append(filtered)

# Distractor: attempt to normalize all signals globally (not used)
all_values = [v for sublist in filtered_signals for v in sublist]
mean_val = sum(all_values) / len(all_values)
normalized_signals = [[v / mean_val for v in s] for s in filtered_signals]

# Actual relevant transformation: compute RMS per sensor
processed_signals = []
for fsig in filtered_signals:
    rms = math.sqrt(sum([x**2 for x in fsig]) / len(fsig))
    processed_signals.append(round(rms, 4))

# Another decoy structure
system_status = {
    'uptime': 1274,
    'load_avg': [0.45, 0.67, 0.52],
    'diagnostics': 'OK'
}

# Critical analysis function with nested logic and lambda
analyze_readings = lambda signals: (
    sum(
        list(
            map(
                lambda x: (
                    x * 1.5 if x < 1.0 else (
                        x * 0.9 if 1.0 <= x < 2.0 else (
                            x * 0.7  # higher readings get dampened
                        )
                    )
                ),
                signals
            )
        )
    ) + 10.5  # base correction factor
)

# Dead code path - never executed
if False:
    backup_analysis = 0
    for s in processed_signals:
        if s > 1.5:
            backup_analysis += s * 2
    system_status['fallback'] = backup_analysis

# Key statement
final_diagnostic = analyze_readings(processed_signals)

# Irrelevant formatting
report_header = f"Diagnostic Report: {device_location} | Operator: {operator_id}"
print(report_header)

# Output the target result
print(f"Target result: {final_diagnostic}")