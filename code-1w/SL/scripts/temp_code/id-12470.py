from collections import defaultdict, Counter

# Simulated IoT sensor data processing with diagnostic evaluation
def collect_sensor_readings():
    readings = [
        ('temp', 36.8), ('hr', 74), ('spo2', 98),
        ('temp', 37.1), ('hr', 76), ('spo2', 97),
        ('temp', 37.5), ('hr', 80), ('spo2', 96),
        ('temp', 38.2), ('hr', 88), ('spo2', 95),
        ('temp', 39.0), ('hr', 95), ('spo2', 93)
    ]
    grouped = defaultdict(list)
    for sensor, val in readings:
        grouped[sensor].append(val)
    return grouped

# Irrelevant auxiliary function – dead code path
def analyze_pattern(sequence):
    if not sequence:
        return 0
    trend = 0
    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i-1]:
            trend += 1
        elif sequence[i] < sequence[i-1]:
            trend -= 1
    return trend * 2  # Unused result

# Misleading normalization function with decoy logic
def normalize(value, base=37.0, scale=1.0):
    adjusted = (value - base) / scale
    if adjusted > 1.0:
        return round(adjusted * 100)
    else:
        return int(abs(adjusted))  # Distractor: never actually used meaningfully

# Core processing pipeline
health_data = collect_sensor_readings()

# Decoy data structures with plausible but unused metrics
baseline_stats = {
    'temp_avg': sum(health_data['temp']) / len(health_data['temp']),
    'hr_peak': max(health_data['hr']),
    'spo2_trend': [b - a for a, b in zip(health_data['spo2'], health_data['spo2'][1:])]
}

# Fake risk scoring – looks important but irrelevant
risk_score = 0
for hr_val in health_data['hr']:
    if hr_val > 90:
        risk_score += 10
    elif hr_val > 80:
        risk_score += 5

# Threshold configuration map – ACTUALLY USED
threshold_map = defaultdict(dict)
threshold_map['temp']['high'] = 37.8
threshold_map['temp']['low'] = 36.0
threshold_map['hr']['high'] = 90
threshold_map['hr']['low'] = 60
threshold_map['spo2']['high'] = 100
threshold_map['spo2']['low'] = 95

# Auxiliary string-based flag system – red herring
status_flags = []
for temp in health_data['temp']:
    if temp > 38.0:
        status_flags.append('FEVER_ALERT')
    else:
        status_flags.append('NORMAL')

flag_counter = Counter(status_flags)

# Actual key computation function
abnormal_count = 0
for sensor_type, values in health_data.items():
    high_lim = threshold_map[sensor_type]['high']
    low_lim = threshold_map[sensor_type]['low']
    for v in values:
        if v > high_lim or v < low_lim:
            abnormal_count += 1

# Secondary metric – appears significant but is only partially relevant
episode_count = 0
in_episode = False
for v in health_data['temp']:
    if v >= threshold_map['temp']['high'] and not in_episode:
        episode_count += 1
        in_episode = True
    if v < threshold_map['temp']['high']:
        in_episode = False

# Tertiary distraction: bit manipulation on HR values (unused)
bit_analysis = 0
for val in health_data['hr']:
    shifted = (val << 1) ^ 0xFF
    if shifted % 3 == 0:
        bit_analysis += 1

# Final processing logic – this is where the answer originates
def process_metrics(data, thresholds):
    total_anomalies = 0
    for sensor, readings in data.items():
        hl = thresholds[sensor]['high']
        ll = thresholds[sensor]['low']
        # Use list comprehension to filter out-of-range values
        anomalies = [x for x in readings if x < ll or x > hl]
        total_anomalies += len(anomalies)
    
    # Apply conditional escalation based on spo2 duration
    spo2_vals = data['spo2']
    prolonged_low = sum(1 for x in spo2_vals if x < thresholds['spo2']['low'])
    if prolonged_low >= 3:
        total_anomalies += 2
    
    # Correct adjustment using logical conditions
    if data['temp'][-1] > thresholds['temp']['high'] and prolonged_low >= 2:
        total_anomalies += 1
    
    return total_anomalies

# Execution point of interest
final_diagnostic = process_metrics(health_data, threshold_map)

# Print required output
print(f"Result: {final_diagnostic}")