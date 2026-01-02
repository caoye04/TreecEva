import itertools

# Simulated sensor network data processing with diagnostic evaluation
sensor_ids = ['S1', 'S2', 'S3', 'S4']
deploy_zones = {1: 'North', 2: 'South', 3: 'East', 4: 'West'}
baseline_offsets = {'S1': 12.5, 'S2': 15.0, 'S3': 10.8, 'S4': 13.2}

calibration_sequence = [0.98, 1.02, 0.99, 1.01]
redundant_flags = [True, False, True, True, False]

# Raw readings from sensors (simulated)
raw_readings = {
    'S1': [102, 98, 105, 110, 95],
    'S2': [88, 92, 85, 87, 90],
    'S3': [115, 112, 118, 120, 110],
    'S4': [76, 78, 73, 77, 75]
}

# Auxiliary metadata (some irrelevant)
sensor_specs = {
    'range_max': 200,
    'precision_class': 'A',
    'last_calib': '2023-11-05'
}

# Irrelevant transformation chain (dead path)
def legacy_convert(val):
    return (val * 1.05) + 3.2

def calculate_entropy(data):
    # Unused function - red herring
    total = sum(data)
    probs = [float(d) / total for d in data]
    return -sum(p * p for p in probs)

# Core processing functions
def normalize_reading(raw_vals, offset, factor=1.0):
    adjusted = [(v + offset) * factor for v in raw_vals]
    return [round(x, 2) for x in adjusted]

def detect_anomalies(values, limit):
    return [v for v in values if abs(v) > limit]

def rolling_average(series, window=3):
    smoothed = []
    for i in range(len(series)):
        if i < window - 1:
            smoothed.append(series[i])
        else:
            window_avg = sum(series[i - window + 1:i + 1]) / window
            smoothed.append(round(window_avg, 2))
    return smoothed

# Complex filtering logic with distractors
temp_flags = {}
for sid in sensor_ids:
    temp_flags[sid] = len(raw_readings[sid]) % 2 == 1

status_registry = dict(zip(sensor_ids, [True]*4))
status_registry['S2'] = False  # Simulate maintenance mode

# Irrelevant set operations (distractor)
active_set = set(sensor_ids)
maintenance_set = {'S2'}
disabled_set = set()
zone_coverage = active_set - maintenance_set

# Primary data transformation pipeline
processed_data = {}
for s_id in sensor_ids:
    base_offset = baseline_offsets.get(s_id, 0)
    raw_seq = raw_readings[s_id]
    
    # Apply normalization with cyclic calibration factor
    calib_factor = calibration_sequence[hash(s_id) % len(calibration_sequence)]
    normalized = normalize_reading(raw_seq, base_offset, calib_factor)
    
    # Rolling average smoothing
    smoothed = rolling_average(normalized)
    
    # Inject irrelevant string operation (distractor)
    tag_suffix = ''.join(itertools.islice(itertools.cycle('XYZ'), 5))
    tag_suffix = tag_suffix.upper().replace('X', '0').lower()  # Complex no-op
    
    processed_data[s_id] = smoothed

# Filtering logic with decoy conditions
filter_threshold = 115.5
secondary_cap = 200.0
exclusion_list = []

filtered_data = {}
for key, readings in processed_data.items():
    # Real filter condition
    valid_readings = [r for r in readings if r < filter_threshold]
    
    # Fake complex exclusion (never used)
    if key in maintenance_set and len(valid_readings) > 3:
        continue  # Dead branch due to prior registry
    
    # Actual inclusion
    filtered_data[key] = valid_readings

# Create complex threshold map (used later)
threshold_map = {}
for idx, sensor in enumerate(sensor_ids):
    zone_key = idx + 1
    base_zone_threshold = 110 + (idx * 3)
    safety_margin = 5.5 if zone_key % 2 == 0 else 3.2
    threshold_map[sensor] = base_zone_threshold + safety_margin

# Decoy aggregation (irrelevant)
aggregated_stats = []
for vals in filtered_data.values():
    if vals:
        stat_entry = {
            'mean': sum(vals) / len(vals),
            'peak': max(vals),
            'stdev_guess': (max(vals) - min(vals)) / 4
        }
        aggregated_stats.append(stat_entry)  # Computed but unused

# Critical diagnostic function
def process_readings(data_dict, thresholds):
    diagnostics = []
    
    # Nested logic with multiple steps
    for sensor, samples in data_dict.items():
        if not samples:
            diagnostics.append(0)
            continue
        
        upper_limit = thresholds.get(sensor, 100)
        
        # Count how many readings exceed adjusted threshold
        count_high = 0
        cumulative_surplus = 0
        
        for val in samples:
            adjusted_limit = upper_limit * 0.95  # Slight tolerance
            if val > adjusted_limit:
                count_high += 1
                surplus = val - adjusted_limit
                cumulative_surplus += round(surplus, 2)
        
        # Complex scoring (only one part used)
        if count_high == 0:
            score = 10
        elif count_high == 1:
            score = 7
        elif count_high == 2:
            score = 4
        else:
            score = 1
        
        # Only this component is used in final result
        diagnostics.append(cumulative_surplus)
    
    # Final computation
    total_excess = sum(diagnostics)
    adjustment_factor = 0.85
    if len(diagnostics) >= 3:
        adjustment_factor *= 0.95
    
    intermediate_result = total_excess * adjustment_factor
    
    # Final nonlinear transformation
    if intermediate_result > 50:
        final_score = 100 - (intermediate_result / 2)
    elif intermediate_result > 20:
        final_score = 85 - (intermediate_result * 0.4)
    else:
        final_score = 90 - (intermediate_result * 0.2)
    
    return round(final_score, 4)

# Execution point of interest
final_diagnostic = process_readings(filtered_data, threshold_map)

# Print result as required
print(f"Target result: {final_diagnostic}")