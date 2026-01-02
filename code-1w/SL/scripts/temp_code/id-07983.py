def analyze_readings(readings):
    # Irrelevant preprocessing (distractor)
    normalized = [r / max(readings) for r in readings]
    smoothed = [sum(normalized[i:i+3]) / 3 for i in range(len(normalized) - 2)]
    
    # Relevant computation: detect anomalies
    anomalies = 0
    trend_score = 0
    for i, val in enumerate(readings):
        if val > 90:
            anomalies += 1
            if i > 0 and readings[i-1] > 80:
                trend_score += 2
    return anomalies, trend_score

# Decoy function - never called
def calculate_stress_index(data):
    stress = 0
    for d in data:
        stress += d ** 0.5 * 3.14
    return stress % 100

# Another decoy - looks important but unused
baseline_shift = 0.05
scaling_factor = 1.75
offset_table = {i: i*0.1 for i in range(10)}

# Real data
sensor_ids = ['S1', 'S2', 'S3', 'S4']
diagnostics = {'S1': [], 'S2': [], 'S3': [], 'S4': []}

# Simulated health sensor readings (fictional units)
raw_data = {
    'S1': [75, 82, 95, 67, 88],
    'S2': [50, 45, 60, 55, 70],
    'S3': [90, 92, 88, 94, 89],
    'S4': [30, 35, 40, 25, 33]
}

# Thresholds for alerts (real logic)
thresholds = {
    'critical': 90,
    'warning': 80,
    'normal': 60
}

# Intermediate processing with distractors
aggregated_stats = {}
total_entries = 0
duplicate_check = set()
for sid, values in raw_data.items():
    total_entries += len(values)
    aggregated_stats[sid] = {
        'max_val': max(values),
        'above_warning': len([v for v in values if v > thresholds['warning']]),
        'peaks': len([v for v in values if v > thresholds['critical']])
    }
    # Red herring: tracking duplicates that don't exist
    for v in values:
        if v in duplicate_check:
            print(f'Duplicate detected: {v}')  # Dead code path
        duplicate_check.add(v)

# Unused transformation (misleading)
shifted_data = {}
for k, v in raw_data.items():
    shifted_data[k] = [x + baseline_shift for x in v]

# Core logic disguised among noise
health_data = []
for sid in sensor_ids:
    readings = raw_data[sid]
    anomaly_count, trend = analyze_readings(readings)
    # Only sensors S1 and S3 contribute to final diagnostic
    if sid in ['S1', 'S3']:
        entry = {
            'id': sid,
            'anomalies': anomaly_count,
            'trend': trend,
            'weight': 1.5 if sid == 'S3' else 1.0
        }
        health_data.append(entry)

# Critical operation buried in abstraction
extra_weights = {'S1': 1.0, 'S3': 1.8}  # Conflicting info - distractor

def process_metrics(data_list, limits):
    base = 0
    bonus = 0.0
    for item in data_list:
        base += item['anomalies'] * 5
        bonus += item['trend'] * item['weight']
        # Misleading conditional that seems important but doesn't trigger
        if item['anomalies'] > 10:
            bonus += 20  # unreachable due to data
    # Final formula combines multiple concepts
    result = (base * 3.7) + (bonus * 2.15)
    return int(result)  # deterministic integer output

# Execution point of interest
final_diagnostic = process_metrics(health_data, thresholds)

# Print required at end
print(f"Target result: {final_diagnostic}")