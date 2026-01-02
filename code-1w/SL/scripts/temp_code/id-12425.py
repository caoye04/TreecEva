from collections import defaultdict, Counter

# Simulated sensor array data with diagnostic flags
data_stream = [
    (101, 'TEMP', 36.8, True),
    (102, 'PRESSURE', 1013, False),
    (103, 'TEMP', 39.1, True),
    (104, 'HUMIDITY', 45, True),
    (105, 'TEMP', 37.0, True),
    (106, 'PRESSURE', 995, False),
    (107, 'HUMIDITY', 60, True),
    (108, 'TEMP', 41.2, True),
    (109, 'PRESSURE', 1020, False),
    (110, 'HUMIDITY', 33, True)
]

# Irrelevant metadata - distractor
system_config = {
    'calibration_version': 'v2.1',
    'last_sync': '2023-11-05',
    'units': {'TEMP': 'C', 'PRESSURE': 'hPa', 'HUMIDITY': '%'},
    'sampling_rate': 10
}

# Decoy function - never called
def analyze_trend(data):
    return sum([x[2] for x in data if x[1] == 'TEMP']) / len([x for x in data if x[1] == 'TEMP'])

# Misleading intermediate calculation - dead path
baseline_pressure = sum([x[2] for x in data_stream if x[1] == 'PRESSURE']) // len([x for x in data_stream if x[1] == 'PRESSURE'])
adjusted_baseline = baseline_pressure * 1.003 + 5  # unused adjustment

# Distractor: fake normalization logic
normalization_factors = defaultdict(float)
normalization_factors['TEMP'] = 1.0
normalization_factors['HUMIDITY'] = 0.01
normalization_factors['PRESSURE'] = 0.1

# Unused transformation map
transform_map = {uid: (sensor, round(val * normalization_factors[sensor], 2)) 
                for uid, sensor, val, active in data_stream}

# Real processing begins here — filtering active sensors only
active_data = [entry for entry in data_stream if entry[3]]

# Group readings by type — relevant
readings_by_type = defaultdict(list)
for uid, stype, value, active in active_data:
    readings_by_type[stype].append(value)

# Compute statistical outliers - used in filtering
outliers = set()
for stype, values in readings_by_type.items():
    mean_val = sum(values) / len(values)
    std_dev = (sum((v - mean_val) ** 2 for v in values) / len(values)) ** 0.5
    for i, v in enumerate(values):
        if abs(v - mean_val) > 1.8 * std_dev:
            outliers.add((stype, v))

# Filtered data excludes outliers — key step
filtered_data = [(uid, stype, val, active) for uid, stype, val, active in active_data 
                 if (stype, val) not in outliers]

# Threshold configuration - relevant mapping
threshold_map = defaultdict(dict)
threshold_map['TEMP']['warning'] = 38.0
threshold_map['TEMP']['critical'] = 40.0
threshold_map['HUMIDITY']['warning'] = 50
threshold_map['HUMIDITY']['critical'] = 70
threshold_map['PRESSURE']['warning'] = 1000
threshold_map['PRESSURE']['critical'] = 980

# Diagnostic counters - irrelevant but plausible
alert_counter = Counter()
device_status = defaultdict(lambda: 'OK')

# Bitwise device health simulation - red herring
device_health_flags = 0b1101
mask_critical = 0b1000
mask_warning = 0b0100
mask_info = 0b0010

# Fake status update loop - dead code
for uid in [d[0] for d in filtered_data]:
    shift = uid % 4
    flag = (device_health_flags >> shift) & 0b1
    if flag:
        device_status[uid] = 'WARNING'
        alert_counter['simulated'] += 1  # never impacts result

# Real processing function
def process_readings(data, thresholds):
    diagnostics = []
    
    # Nested logic with multiple steps
    for uid, stype, val, _ in data:
        base_diag = 0
        warn_thresh = thresholds[stype]['warning']
        crit_thresh = thresholds[stype]['critical']
        
        if stype == 'TEMP':
            if val >= crit_thresh:
                base_diag = 3
            elif val >= warn_thresh:
                base_diag = 2
            else:
                base_diag = 1
        elif stype == 'HUMIDITY':
            if val >= crit_thresh:
                base_diag = 3
            elif val >= warn_thresh:
                base_diag = 2
            else:
                base_diag = 1
        elif stype == 'PRESSURE':
            if val < crit_thresh:
                base_diag = 3
            elif val < warn_thresh:
                base_diag = 2
            else:
                base_diag = 1
        
        # Apply weighting based on position in stream - subtle but valid
        position_weight = (uid - 100) % 4 + 1
        weighted_diag = base_diag * position_weight
        
        # XOR-based anomaly detection - actually used
        anomaly_key = int(val) ^ uid  # bitwise XOR
        if anomaly_key % 7 == 0:
            weighted_diag += 1
        
        diagnostics.append(weighted_diag)
    
    # Final aggregation: sum with conditional offset
    total_score = sum(diagnostics)
    count_pressure = len([d for d in data if d[1] == 'PRESSURE'])
    
    # Conditional bonus logic — depends on exact count
    if count_pressure >= 2:
        total_score += 5
    else:
        total_score -= 2
    
    # Secondary adjustment based on reading diversity
    types_present = {d[1] for d in data}
    if len(types_present) == 3:
        total_score += 3
    
    return total_score

# Key execution point
final_diagnostic = process_readings(filtered_data, threshold_map)
print(f"Result: {final_diagnostic}")