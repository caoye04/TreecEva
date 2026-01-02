from collections import defaultdict, Counter
import math

# Simulated sensor data ingestion (irrelevant in part)
sensor_ids = ['S1', 'S2', 'S3', 'S4']
raw_readings = {
    'S1': [14, 17, 23, 14, 19],
    'S2': [8, 11, 9, 13],
    'S3': [25, 27, 25, 26, 28, 25],
    'S4': [5, 7, 6]
}

# Irrelevant preprocessing: normalize readings (unused later)
normalized = {}
for sid, vals in raw_readings.items():
    mean_val = sum(vals) / len(vals)
    normalized[sid] = [round((x - mean_val) / mean_val, 3) for x in vals]

# Core signal processing begins
baseline_offsets = {'S1': 12, 'S2': 10, 'S3': 25, 'S4': 6}

# Misleading transformation: frequency emulation (partially irrelevant)
freq_weights = defaultdict(float)
total_power = 0
for i, sid in enumerate(sensor_ids):
    base = baseline_offsets[sid]
    weight = (base ** 0.5) * (i + 1)
    freq_weights[sid] = round(weight, 3)
    total_power += weight

# Dead code path: unused calibration function
def calibrate_sensor(x, mode='legacy'):
    if mode == 'legacy':
        return (x >> 1) + (x << 2)
    else:
        return x ^ 255

# Signal mapping with red herring logic
bit_flags = {}
for sid in sensor_ids:
    offset = baseline_offsets[sid]
    # Complex but mostly irrelevant bit logic
    flag = ((offset & 15) ^ 7) | (offset >> 3)
    bit_flags[sid] = flag % 11  # Normalize to small range

# Real processing starts here
processed_data = []
divergence_log = []

for sid, readings in raw_readings.items():
    base = baseline_offsets[sid]
    deviations = [abs(r - base) for r in readings]
    avg_dev = sum(deviations) / len(deviations)
    divergence_log.append(avg_dev)
    
    # Key transformation: weighted contribution
    if avg_dev > 3.0:
        processed_data.append(base + (avg_dev / 2))
    else:
        processed_data.append(base - 1)

# Threshold system with decoy entries
threshold_map = defaultdict(lambda: 15.0)
threshold_map.update({
    'S1': 4.2, 'S2': 3.8, 'S3': 5.1, 'S4': 2.9,
    'fallback': 10.0, 'emergency': 20.0, 'unused_mode': 1.5
})

# Unused statistical analysis (distractor)
stats_summary = Counter()
for val in processed_data:
    bucket = int(val) // 5
    stats_summary[f'group_{bucket}'] += 1

# Critical diagnostic function with embedded logic
def analyze_signal(data_list, thresholds):
    cumulative_score = 0.0
    adjustment_factor = 1.0
    
    # Simulate multi-stage diagnosis
    for i, val in enumerate(data_list):
        # Use index-based modulation (red herring)
        temp_mod = (i + 1) * 0.9 if i % 2 == 0 else (i + 1) * 1.1
        adjusted_val = val * temp_mod
        
        # Actual decision logic
        if adjusted_val > list(thresholds.values())[i]:
            cumulative_score += math.log(adjusted_val) * 1.5
        else:
            cumulative_score -= math.sqrt(abs(adjusted_val - 5)) * 0.8
    
    # Final nonlinear correction (key step)
    if cumulative_score > 0:
        adjustment_factor = 1.75
    else:
        adjustment_factor = 0.65
    
    final_score = cumulative_score * adjustment_factor
    
    # Additional distraction: XOR-based checksum (unused)
    checksum = 0
    for b in f'{final_score:.4f}'.encode('ascii'):
        checksum ^= b
    
    return round(final_score, 4)

# Execute critical statement
final_diagnostic = analyze_signal(processed_data, threshold_map)

# Print result as required
print(f"Result: {final_diagnostic}")