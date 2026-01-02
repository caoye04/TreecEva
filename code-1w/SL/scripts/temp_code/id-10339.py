from collections import defaultdict, Counter

# Simulate sensor data ingestion with noise filtering
def fetch_sensor_data():
    raw_readings = [
        ('temp', 30), ('pressure', 101), ('temp', 35), ('humidity', 60),
        ('pressure', 102), ('temp', 40), ('humidity', 65), ('temp', 33)
    ]
    filtered = [r for r in raw_readings if r[1] > 0]
    grouped = defaultdict(list)
    for k, v in filtered:
        grouped[k].append(v)
    return grouped

# Misleading auxiliary function (dead logic path - never called)
def legacy_calibrate(x):
    return x * 0.95 + 2.1

# Another decoy: unused transformation
def frequency_analysis(data):
    counts = Counter([k for k, v in data])
    return {k: v / len(data) for k, v in counts.items()}

# Real processing pipeline
processed_data = []
decoy_matrix = [[i * j for j in range(3)] for i in range(3)]
normalization_factor = 0  # red herring; not actually used

sensor_data = fetch_sensor_data()

# Irrelevant aggregation
aggregated_stats = {}
for sensor_type, values in sensor_data.items():
    aggregated_stats[sensor_type] = {
        'sum': sum(values),
        'count': len(values),
        'range': max(values) - min(values)
    }

# Fake calibration sequence (distractor)
calibration_cache = {}
for typ in ['temp', 'pressure', 'humidity']:
    base = aggregated_stats.get(typ, {}).get('sum', 0)
    calibrated = (base * 1.05) if base > 0 else 0
    calibration_cache[typ] = round(calibrated, 2)

# Actual processing begins here
for typ, vals in sensor_data.items():
    avg = sum(vals) / len(vals)
    if typ == 'temp':
        processed_data.extend([v for v in vals if v >= avg])
    elif typ == 'pressure':
        processed_data.append(max(vals))
    else:
        processed_data.append(min(vals))

# Build threshold map with irrelevant entries
def build_threshold_map():
    tmap = defaultdict(lambda: 50)
    tmap['temp'] = 34
    tmap['pressure'] = 100
    tmap['light'] = 200  # unused sensor type
    tmap['co2'] = 450   # red herring
    return tmap

threshold_map = build_threshold_map()

# Decoy statistical summary (never used)
stats_summary = {
    k: {'z_score': (aggregated_stats[k]['sum'] - 50) / 5} 
    for k in aggregated_stats
}

# Core analysis function with conditional expressions and early returns
def analyze_readings(readings, thresholds):
    temp_count = 0
    critical_count = 0
    total_impact = 0.0

    for val in readings:
        if val > thresholds['temp']:
            temp_count += 1
            total_impact += val * 0.3
        if val > thresholds['pressure']:
            critical_count += 1
            total_impact += val * 0.7  # higher weight

        # Early exit red herring (never triggered due to data)
        if temp_count > 100:
            return -1  

    # Conditional expression with meaningful fallback
    adjustment = 1.25 if temp_count >= 2 else 0.85
    final_impact = total_impact * adjustment

    # Secondary logic: count high-readings but only if pressure events exist
    if critical_count == 0:
        return int(final_impact // 2)

    # Key assignment point
    final_diagnostic = int(round(final_impact))
    return final_diagnostic

# Execute main logic
temp_debug_log = [x for x in processed_data if x > 30]  # distractor log
metadata_flags = {'calibrated': True, 'retries': 0}  # irrelevant

final_diagnostic = analyze_readings(processed_data, threshold_map)
print(f"Result: {final_diagnostic}")