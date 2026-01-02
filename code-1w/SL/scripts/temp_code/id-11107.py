from collections import defaultdict, Counter
from itertools import zip_longest

# Simulated sensor array data with multiple noise sources
def fetch_sensor_streams():
    raw_signals = [
        [3, 1, 4, 1, 5, 9, 2, 6, 5, 3],
        [2, 7, 1, 8, 2, 8, 1, 8, 2, 8],
        [1, 6, 1, 8, 0, 3, 3, 9, 8, 8],
        [9, 7, 9, 3, 2, 3, 8, 4, 6, 2]
    ]
    timestamps = [1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009]
    metadata = {'nodes': 4, 'sampling_rate': 10, 'version': '2.1'}
    return raw_signals, timestamps, metadata

# Irrelevant auxiliary function - decoy for signal modulation
def modulate_frequency(signal, freq):
    return [int(x * freq % 7) for x in signal]

# Core processing: filter out noise based on dynamic baselines
def compute_adaptive_baseline(signal):
    baseline = sum(signal[:5]) / 5
    deviations = [abs(x - baseline) for x in signal]
    tolerance = sum(deviations[:5]) / 5
    return [x for x in signal if abs(x - baseline) <= 2 * tolerance]

# Secondary validation layer using voting mechanism
def validate_consistency(grouped_readings):
    transposed = list(zip_longest(*grouped_readings, fillvalue=0))
    consensus = []
    for readings in transposed:
        count = Counter(readings)
        mode_val, freq = count.most_common(1)[0]
        consensus.append(mode_val if freq >= 2 else 0)
    return consensus

# Red herring function: simulates calibration but unused
def trigger_calibration_cycle(node_id):
    history = defaultdict(list)
    for step in range(5):
        adjustment = (node_id * step) % 9
        history['adjustments'].append(adjustment)
        temp_offset = abs(adjustment - 4) ** 0.5
        history['thermal_drift'].append(temp_offset)
    return history

# Misleading intermediate diagnostic
aux_diagnostics = {
    'peak_noise_ratio': 0.87,
    'signal_entropy': 3.141593,
    'spike_count': 12,
    'baseline_drift': -0.45
}

# Main filtering logic with distractor variables
raw_data, time_stamps, config = fetch_sensor_streams()
filtered_data = []
for stream in raw_data:
    cleaned = compute_adaptive_baseline(stream)
    expanded = [x + 1 for x in cleaned]  # slight correction
    padded = (expanded + [0] * 10)[:10]
    filtered_data.append(padded)

# Generate fake anomaly triggers (dead code path)
current_alerts = []
for i, series in enumerate(filtered_data):
    if sum(series) > 30 and i % 3 == 0:
        current_alerts.append(f"ALERT_NODE_{i}")
    elif len([x for x in series if x > 7]) > 2:
        current_alerts.append(f"OVERLOAD_{i}")

# Unused complex structure - creates distraction
analysis_grid = [[defaultdict(int) for _ in range(3)] for __ in range(3)]
for r in range(3):
    for c in range(3):
        analysis_grid[r][c]['score'] = (r * 2 + c) ** 2
        analysis_grid[r][c]['weight'] = r + c * 0.5

# Critical threshold map for diagnostic engine
threshold_map = {
    'critical': 7.0,
    'warning': 4.5,
    'info': 2.0
}

# Real processing begins: validate across nodes
consensus_readings = validate_consistency(filtered_data)

# Secondary filter based on threshold zones
zone_scores = defaultdict(float)
for val in consensus_readings:
    if val >= threshold_map['critical']:
        zone_scores['critical'] += 1.5
    elif val >= threshold_map['warning']:
        zone_scores['warning'] += 1.1
    elif val >= threshold_map['info']:
        zone_scores['info'] += 0.7

# Decoy calculation with bit manipulation (irrelevant)
bitwise_signature = 0
for i, score in enumerate(zone_scores.values()):
    shifted = int(score) << i
    bitwise_signature ^= shifted
    bitwise_signature = bitwise_signature % 1000

# Final diagnostic computation - this is the key statement
final_diagnostic = 0
for i, reading in enumerate(consensus_readings):
    contribution = reading * (i + 1)
    if contribution > threshold_map['warning']:
        final_diagnostic += int(contribution * 0.9)
    else:
        final_diagnostic -= int(contribution * 0.25)

Result: {final_diagnostic}