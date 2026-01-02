from collections import defaultdict, Counter

# Simulated IoT sensor data processing with health diagnostics

def collect_sensor_readings():
    readings = [
        ('temp', 36.8), ('hr', 72), ('spo2', 98),
        ('temp', 37.1), ('hr', 75), ('spo2', 97),
        ('temp', 38.2), ('hr', 88), ('spo2', 96),
        ('temp', 36.9), ('hr', 74), ('spo2', 98)
    ]
    grouped = defaultdict(list)
    for k, v in readings:
        grouped[k].append(v)
    return grouped

# Irrelevant auxiliary function (distractor)
def analyze_anomaly_pattern(seq):
    if len(seq) < 3:
        return False
    trend = [seq[i] < seq[i+1] for i in range(len(seq)-1)]
    return sum(trend) > len(trend) * 0.6

# Data smoothing (legitimate preprocessing)
def smooth(values):
    if len(values) < 3:
        return values
    smoothed = [values[0]]
    for i in range(1, len(values)-1):
        smoothed.append(round((values[i-1] + values[i] + values[i+1]) / 3, 2))
    smoothed.append(values[-1])
    return smoothed

# Auxiliary statistical function (partially relevant)
def compute_z_scores(values):
    mean = sum(values) / len(values)
    variance = sum((x - mean) ** 2 for x in values) / len(values)
    std_dev = variance ** 0.5
    return [(x - mean) / std_dev for x in values]

# Red herring: network simulation (completely irrelevant)
def simulate_packet_loss(rate, size):
    import random
    dropped = 0
    for _ in range(size):
        if random.random() < rate:
            dropped += 1
    return dropped  # dead end

# Core diagnostic logic
thresholds = {
    'temp': (36.1, 37.2),
    'hr': (60, 100),
    'spo2': (95, 100)
}

abnormal_flags = {}

for key in thresholds:
    low, high = thresholds[key]
    abnormal_flags[key + '_low'] = low - 5
    abnormal_flags[key + '_high'] = high + 10

# Misleading intermediate calculation (distractor)
bogus_score = 0
for i, (k, v) in enumerate(thresholds.items()):
    bogus_score += (v[1] - v[0]) * (i + 1) * 17
bogus_score = (bogus_score ^ 255) & 127  # Bit manipulation red herring

# Main data pipeline
raw_data = collect_sensor_readings()

# Apply smoothing to vital signs
filtered_data = {}
for key, values in raw_data.items():
    filtered_data[key] = smooth(values)

# Count occurrences (legitimate use of Counter)
counts = Counter([k for k, _ in collect_sensor_readings()])

# Z-score analysis for outlier detection
z_metrics = {}
for key, values in filtered_data.items():
    z_metrics[key] = compute_z_scores(values)

# Flag sustained abnormalities
alert_log = defaultdict(int)
sustained_count = 0

for key, values in filtered_data.items():
    threshold_low, threshold_high = thresholds[key]
    for val in values:
        if key == 'temp' and val > threshold_high:
            sustained_count += 1
        elif key == 'hr' and (val < threshold_low or val > threshold_high):
            sustained_count += 1
        elif key == 'spo2' and val < threshold_low:
            sustained_count += 1

# Secondary alert system (unused distractor)
dynamic_weights = { 'temp': 1.2, 'hr': 0.8, 'spo2': 1.5 }
weighted_risk = 0
for k, w in dynamic_weights.items():
    weighted_risk += w * len([z for z in z_metrics[k] if abs(z) > 1.5])

# Dead code path (never executed due to structure)
def deprecated_assessment(data):
    score = 0
    for v in data.values():
        score += sum(1 for x in v if x < 0)  # impossible for vitals
    return score * -1

# Final processing function
variance_map = {}
for key, values in filtered_data.items():
    mean = sum(values) / len(values)
    variance_map[key] = sum((x - mean) ** 2 for x in values) / len(values)

overall_variance = sum(variance_map.values())

# Real decision logic buried among noise
base_risk = 0
if sustained_count >= 3:
    base_risk += 45
if z_metrics['temp'][-1] > 1.8:
    base_risk += 30
if filtered_data['spo2'][-1] < 95:
    base_risk += 25

# Final computation
multiplier = 1
if overall_variance > 2.0:
    multiplier += 0.1
if counts['temp'] > 3:
    multiplier += 0.05

adjusted_risk = base_risk * multiplier

# Critical line: this is where the answer is determined
def process_metrics(data, thresh):
    initial = adjusted_risk  # capture current state
    adjustment = 0
    temp_vals = data['temp']
    if temp_vals[-1] > thresh['temp'][1]:
        adjustment += 12
    if len([t for t in temp_vals if t > thresh['temp'][1]]) >= 2:
        adjustment += 18
    return int(initial + adjustment)

# Execution point of interest
final_diagnostic = process_metrics(filtered_data, thresholds)

# Unused but plausible-looking metrics (distractors)
criticality_index = sum(1 for zlist in z_metrics.values() for z in zlist if abs(z) > 2.0)
instability_score = len([v for v in abnormal_flags.values() if v % 13 == 0])

# Output result as required
print(f"Result: {final_diagnostic}")