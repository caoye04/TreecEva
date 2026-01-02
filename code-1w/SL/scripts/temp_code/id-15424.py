from collections import defaultdict, Counter

# Simulated sensor array data with noise and redundant readings
data_stream = [
    (1007, 'temp', 23.5), (1008, 'pressure', 101.3), (1009, 'humidity', 45.2),
    (1010, 'temp', 24.1), (1011, 'co2', 410), (1012, 'light', 300),
    (1013, 'temp', 22.8), (1014, 'pressure', 101.5), (1015, 'humidity', 47.1),
    (1016, 'motion', 1), (1017, 'temp', 24.0), (1018, 'co2', 425),
    (1019, 'pressure', 101.2), (1020, 'humidity', 46.3), (1021, 'temp', 23.9)
]

# Irrelevant baseline catalog (distractor)
category_codes = {'temp': 0, 'pressure': 1, 'humidity': 2, 'co2': 3, 'light': 4, 'motion': 5}
code_lookup = {v: k for k, v in category_codes.items()}

# Misleading calibration map with unused entries (red herring)
calibration_offset = defaultdict(float)
for sensor_type in ['temp', 'pressure', 'humidity']:
    calibration_offset[sensor_type] = 0.1 if sensor_type == 'temp' else 0.05

calibration_offset['ph'] = 0.2  # Unused sensor type

diagnostic_flags = []
raw_aggregates = defaultdict(list)

# Step 1: Organize raw data by sensor type (relevant)
for sensor_id, s_type, reading in data_stream:
    if s_type in ['temp', 'pressure', 'humidity', 'co2']:
        adjusted = reading + calibration_offset[s_type]  # Apply real but minor adjustment
        raw_aggregates[s_type].append(adjusted)

# Step 2: Compute preliminary stats - some used, some not (distractor)
prelim_stats = {}
for stype, vals in raw_aggregates.items():
    prelim_stats[stype] = {
        'raw_count': len(vals),
        'mean_val': sum(vals) / len(vals),
        'peak': max(vals),
        'floor': min(vals)
    }

# Step 3: Filter only temperature and CO2 above threshold (critical path)
filtered_data = []
for entry in data_stream:
    sid, typ, val = entry
    if typ == 'temp' and 23.0 <= val <= 24.5:
        filtered_data.append(entry)
    elif typ == 'co2' and val > 400:
        filtered_data.append(entry)

# Step 4: Build threshold map (used later in processing)
threshold_map = defaultdict(lambda: None)
threshold_map['temp'] = (23.0, 24.5)
threshold_map['co2'] = (400, 500)
threshold_map['voc'] = (200, 1000)  # Dead entry - never used

# Step 5: Auxiliary diagnostic function with early returns and nesting

def analyze_pattern(values):
    if not values:
        return 0
    sorted_vals = sorted(values)
    n = len(sorted_vals)
    if n < 3:
        return sorted_vals[-1] * 2
    
    # Compute moving trend on last three (distraction)
    trend = (sorted_vals[-1] - sorted_vals[-3]) / 2
    if trend > 0.5:
        return sorted_vals[-1] * 1.1
    elif trend < -0.5:
        return sorted_vals[-1] * 0.9
    else:
        return sorted_vals[-1]  # Return latest if stable

# Step 6: Secondary metadata collection (mostly irrelevant)
entry_timestamps = {sid: 1678880000 + idx*30 for idx, (sid, _, _) in enumerate(data_stream)}
timestamp_groups = Counter([ts // 3600 for ts in entry_timestamps.values()])

# Step 7: Process readings - this is where final_diagnostic is computed

def process_readings(data, thresholds):
    result_map = defaultdict(list)
    
    for sid, stype, val in data:
        low, high = thresholds[stype]
        if low <= val <= high:
            result_map[stype].append(val)
    
    diagnostics = []
    
    for stype, readings in result_map.items():
        base_score = sum(readings)
        
        # Apply analysis pattern only if temp
        if stype == 'temp':
            trend_adjusted = analyze_pattern(readings)
            base_score += trend_adjusted / 10
        
        # Nested conditional scoring (complex logic)
        if len(readings) >= 3:
            if stype == 'temp':
                penalty = 0.5 if max(readings) - min(readings) > 1.0 else 0.1
                base_score -= penalty * 10
            elif stype == 'co2':
                base_score += 5
        else:
            if stype == 'co2':
                base_score += 2

        diagnostics.append(int(round(base_score)))
    
    # Final aggregation with character counting distraction
    code_name = "sensor_diag_v2"
    char_bonus = len([c for c in code_name if c in 'aeiou'])  # Always 5
    
    # Key computation step
    final_sum = sum(diagnostics) + char_bonus
    
    # Dead branch (never executes due to data)
    if 'voc' in result_map:
        final_sum += 100
    
    return final_sum

# Step 8: Execute critical statement
final_diagnostic = process_readings(filtered_data, threshold_map)

# Print result as required
print(f"Target result: {final_diagnostic}")