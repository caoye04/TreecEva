from collections import defaultdict, Counter
import math

# Simulated IoT sensor data aggregation and health diagnostics
def collect_sensor_readings():
    readings = [
        ('temp', 36.8), ('hr', 74), ('spo2', 98),
        ('temp', 37.2), ('hr', 78), ('spo2', 96),
        ('temp', 38.1), ('hr', 85), ('spo2', 94),
        ('temp', 36.9), ('hr', 76), ('spo2', 97)
    ]
    grouped = defaultdict(list)
    for sensor, value in readings:
        grouped[sensor].append(value)
    return grouped

# Misleading auxiliary function - never called
def analyze_stress_levels(data):
    stress_markers = {k: sum(1 for x in v if x > 80) for k, v in data.items()}
    return dict(stress_markers)

# Red herring: unused transformation
transform_log = []
def apply_calibration(value, sensor_type):
    if sensor_type == 'temp':
        corrected = value * 1.02 + 0.1
    elif sensor_type == 'hr':
        corrected = max(0, value - 2)
    else:
        corrected = value
    transform_log.append(corrected)
    return corrected

# Decoy data structure
historical_baseline = {
    'temp': [36.5, 36.7, 37.0, 36.8],
    'hr': [70, 72, 75, 73],
    'spo2': [98, 97, 98, 96]
}

# Real processing begins here
def compute_deviation_score(values, base):
    mean_val = sum(values) / len(values)
    variance = sum((x - mean_val) ** 2 for x in values) / len(values)
    return abs(mean_val - base) + math.sqrt(variance + 1e-5)

# Auxiliary counters (some irrelevant)
event_counter = Counter()
critical_flags = set()

# Simulate intermediate diagnostic flags (some are red herrings)
flag_metadata = {}
def raise_flag(code, severity, desc):
    critical_flags.add(code)
    flag_metadata[code] = {'severity': severity, 'desc': desc}
    event_counter[code] += 1

# Main logic with distractors
sensor_data = collect_sensor_readings()

# Irrelevant sorting - doesn't affect outcome
for key in sensor_data:
    sensor_data[key].sort()

# Fake normalization pass
normalized_data = {}
for k, v in sensor_data.items():
    avg = sum(v) / len(v)
    normalized_data[k] = [x / avg for x in v]  # Not used later

# Real baseline definitions
baselines = {'temp': 36.8, 'hr': 72, 'spo2': 97}
thresh_offsets = {'temp': 0.8, 'hr': 10, 'spo2': 2}

# Compute threshold bounds
thresholds = {}
for metric, base in baselines.items():
    tolerance = thresh_offsets[metric]
    thresholds[metric] = (base - tolerance, base + tolerance)

# Intermediate deviation tracking (only temp used in final calc)
deviations = {}
for metric, values in sensor_data.items():
    dev = compute_deviation_score(values, baselines[metric])
    deviations[metric] = round(dev, 3)

# Dead branch: never executed due to condition
if len(sensor_data['temp']) < 3:
    raise_flag('INSUFFICIENT_DATA', 1, 'Not enough temperature samples')

# Real conditional logic path
active_alerts = 0
if deviations['temp'] > 0.5:
    active_alerts += 1
if deviations['hr'] > 1.2:
    active_alerts += 1
if deviations['spo2'] > 0.8:
    active_alerts += 1

# Flag generation (distractor)
if active_alerts >= 2:
    raise_flag('MULTI_SYSTEM_STRESS', 2, 'Elevated metrics in multiple domains')

# Core calculation chain
weighted_risk = 0
weighted_risk += deviations['temp'] * 3.0  
weighted_risk += deviations['hr'] * 1.5
weighted_risk += deviations['spo2'] * 2.0

# Secondary adjustment based on threshold breaches
breach_count = 0
for metric, (low, high) in thresholds.items():
    current_mean = sum(sensor_data[metric]) / len(sensor_data[metric])
    if current_mean < low or current_mean > high:
        breach_count += 1

# Final adjustment using breach count (minor weight)
adjusted_risk = weighted_risk + (breach_count * 0.25)

# Health scoring transformation
health_score = 100 - (adjusted_risk * 8.5)

# Mapping score to diagnostic level
if health_score > 90:
    diagnostic_level = 1
elif health_score > 80:
    diagnostic_level = 2
elif health_score > 70:
    diagnostic_level = 3
else:
    diagnostic_level = 4

# Final processing function
health_data = {
    'metrics': deviations,
    'alerts': active_alerts,
    'score': health_score,
    'level': diagnostic_level
}

def process_metrics(data, threshold_map):
    level = data['level']
    alerts = data['alerts']
    score = data['score']
    
    # Complex interaction formula
    impact_factor = 1 + (alerts * 0.15)
    decay = 0.95 ** level
    
    # Final diagnostic value computation
    raw_diagnostic = score * impact_factor * decay
    
    # Normalize to clinical index scale (0-1000)
    scaled_diagnostic = int(raw_diagnostic * 10)
    
    # Additional smoothing based on threshold stability
    stable_metrics = 0
    for m, vals in sensor_data.items():
        mean_val = sum(vals) / len(vals)
        low_t, high_t = threshold_map[m]
        if low_t <= mean_val <= high_t:
            stable_metrics += 1
    
    # Smoothing bonus (max +50)
    stability_bonus = stable_metrics * 16  # 16*3=48 < 50
    final_diagnostic = scaled_diagnostic + stability_bonus
    
    return final_diagnostic

# Execute main computation
final_diagnostic = process_metrics(health_data, thresholds)

# Print result as required
print(f"Target result: {final_diagnostic}")