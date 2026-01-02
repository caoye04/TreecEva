from collections import defaultdict, Counter
import math

# Simulated sensor network data processing with diagnostic analysis

# Raw sensor inputs (simulated)
sensor_ids = ['S1', 'S2', 'S3', 'S4']
raw_readings = [
    [14, 17, 15, 92, 16],
    [11, 13, 88, 12, 14],
    [10, 87, 13, 15, 18],
    [86, 12, 14, 11, 13]
]

# Irrelevant auxiliary mapping (distractor)
unit_conversions = {
    'C_to_F': lambda x: x * 9/5 + 32,
    'kPa_to_psi': lambda x: x * 0.145038
}

# Misleading preprocessing path (dead code)
def legacy_normalize(data):
    max_val = max(max(row) for row in data)
    return [[round(x / max_val, 3) for x in row] for row in data]

# Unused statistical baseline (red herring)
baseline_stats = {
    'mean': 15.2,
    'std_dev': 2.1,
    'outlier_threshold': 3.5
}

# Fault pattern signatures (partially relevant, partially distractor)
fault_patterns = defaultdict(lambda: 'unknown')
fault_patterns.update({
    86: 'vibration_surge',
    87: 'bearing_stress',
    88: 'rotor_imbalance',
    92: 'thermal_overload'
})

# Decoy fault counter (looks important but unused in final logic)
device_fault_count = defaultdict(int)
for readings in raw_readings:
    for val in readings:
        if val in fault_patterns and 'surge' in fault_patterns[val]:
            device_fault_count['S'+str(readings.index(val))] += 1

# Real processing begins here
abnormal_threshold = 85

# Identify high-risk values and their positions
anomaly_map = {}
for i, readings in enumerate(raw_readings):
    for j, val in enumerate(readings):
        if val > abnormal_threshold:
            anomaly_map[sensor_ids[i]] = anomaly_map.get(sensor_ids[i], []) + [(j, val)]

# Sensor health scoring (complex transformation with distractors)
health_scores = {}
for sid in sensor_ids:
    base_score = 100
    if sid in anomaly_map:
        penalty = sum(5 for _, v in anomaly_map[sid] if v > 90) + sum(2 for _, v in anomaly_map[sid] if 85 < v <= 90)
        decay_factor = 0.95 ** len(anomaly_map[sid])
        base_score = round(base_score * decay_factor - penalty)
    health_scores[sid] = max(base_score, 0)

# Mock calibration adjustment (irrelevant computation)
calibration_matrix = [
    [round(math.sin(i*j + 0.1), 4) for j in range(5)]
    for i in range(4)
]

# Data processor function with embedded logic
processed_data = []
for i, readings in enumerate(raw_readings):
    filtered = [x for x in readings if x < abnormal_threshold]  # Remove anomalies
    smoothed = []
    window = 3
    for k in range(len(filtered)):
        start = max(0, k - window // 2)
        end = min(len(filtered), k + window // 2 + 1)
        avg = sum(filtered[start:end]) / (end - start)
        smoothed.append(round(avg, 2))
    processed_data.append(smoothed)

# Threshold configuration map (critical for final result)
threshold_map = {
    'critical': 85,
    'warning': 70,
    'decay_rate': 0.95
}

# Advanced diagnostic engine
pattern_recognition = lambda seq: sum(1 for a, b in zip(seq, seq[1:]) if b > a) > len(seq) // 2

# Secondary decoy analyzer (misleading path)
class LegacyAnalyzer:
    def __init__(self, data):
        self.data = data
        self.trend = self._compute_trend()
    
    def _compute_trend(self):
        flat = [item for sublist in self.data for item in sublist]
        return 'rising' if sum(flat[-10:]) > sum(flat[:10]) else 'falling'

legacy_analysis = LegacyAnalyzer(raw_readings)  # Computed but unused

# Core analysis function
def analyze_readings(cleaned_data, limits):
    # Compute aggregate statistics
    all_vals = [val for sublist in cleaned_data for val in sublist]
    mean_val = sum(all_vals) / len(all_vals)
    peak = max(all_vals)
    
    # Determine severity level
    if peak >= limits['critical']:
        level = 'critical'
    elif peak >= limits['warning']:
        level = 'warning'
    else:
        level = 'normal'
    
    # Apply correction based on trend
    trend_upward = pattern_recognition(all_vals)
    modifier = 1.1 if trend_upward else 0.9
    
    # Diagnostic score calculation
    base_diagnostic = mean_val * modifier
    decayed = base_diagnostic * (limits['decay_rate'] ** 2)
    
    # Final adjustment using health scores (only S3 matters)
    focus_sensor_score = health_scores['S3']
    if focus_sensor_score < 50:
        decayed *= 0.8
    
    return int(round(decayed))

# Execute critical statement
final_diagnostic = analyze_readings(processed_data, threshold_map)
print(f"Target result: {final_diagnostic}")