from itertools import compress, cycle

# Simulated sensor array data from environmental monitoring station
timestamps = [1648753200, 1648753260, 1648753320, 1648753380, 1648753440]
humidity_readings = [45.2, 47.8, 53.1, 58.9, 49.4]
temperature_readings = [22.5, 23.1, 24.0, 23.8, 22.9]
co2_levels = [415, 423, 435, 442, 419]
pressure_readings = [1013.25, 1012.89, 1012.45, 1012.78, 1013.01]

# Auxiliary metadata (partially irrelevant)
device_ids = ['SNSR-001', 'SNSR-002', 'SNSR-003', 'SNSR-004', 'SNSR-005']
location_grid = [(1,1), (1,2), (2,1), (2,2), (3,1)]
status_flags = [True, True, False, True, True]  # One faulty sensor

# Misleading preprocessing: normalization (not used in final path)
norm_humidity = [h / max(humidity_readings) for h in humidity_readings]
norm_temp = [t / max(temperature_readings) for t in temperature_readings]

# Actual processing begins: filter out invalid sensors using status flags
valid_readings_mask = [flag and temp > 22.0 for flag, temp in zip(status_flags, temperature_readings)]
filtered_timestamps = list(compress(timestamps, valid_readings_mask))
filtered_humidity = list(compress(humidity_readings, valid_readings_mask))
filtered_co2 = list(compress(co2_levels, valid_readings_mask))
filtered_pressure = list(compress(pressure_readings, valid_readings_mask))

# Bitwise diagnostic key generation (only one bit matters)
diag_key = 0
for i, (h, t) in enumerate(zip(filtered_humidity, [23.1, 24.0, 23.8, 22.9])):
    if h > 48.0:
        diag_key |= (1 << i)
diag_key ^= 0b1010  # Apply fixed mask

# Construct threshold map with red herring entries
threshold_map = {
    'humidity_high': 50.0,
    'humidity_low': 40.0,
    'temp_critical': 25.0,
    'co2_warning': 450,
    'pressure_stable': 1012.5,
    'dummy_payload': sum(norm_humidity) * 1000  # unused distractor
}

# Prepare composite dataset using zip and enumerate
sensor_data = []
for idx, (ts, h, c, p) in enumerate(zip(filtered_timestamps, filtered_humidity, filtered_co2, filtered_pressure)):
    record = {
        'index': idx,
        'ts': ts,
        'hum': h,
        'co2': c,
        'pr': p,
        'alert': (h > threshold_map['humidity_high']) or (c > threshold_map['co2_warning'])
    }
    sensor_data.append(record)

# Secondary filtering based on alert state (creates intermediate subset)
alert_records = [r for r in sensor_data if r['alert']]
safe_records = [r for r in sensor_data if not r['alert']]

# Spurious statistical computation (distractor)
avg_deviation = 0.0
if len(alert_records) > 0:
    hum_deviations = [ar['hum'] - threshold_map['humidity_high'] for ar in alert_records]
    avg_deviation = sum(hum_deviations) / len(hum_deviations)

# Core logic: count high-risk conditions using multiple criteria
def process_readings(data, thresholds):
    risk_count = 0
    co2_baseline = thresholds['co2_warning'] - 30
    hum_band = thresholds['humidity_high'] - thresholds['humidity_low']
    
    # Use enumerate to track position and zip to pair consecutive readings
    for i, current in enumerate(data):
        if i == 0:
            continue  # Skip first
        prev = data[i-1]
        
        # Compound condition involving multiple metrics and bitwise check
        condition_a = current['hum'] > prev['hum'] + 1.5
        condition_b = current['co2'] > co2_baseline and prev['co2'] < co2_baseline
        condition_c = (current['pr'] < thresholds['pressure_stable']) != (prev['pr'] < thresholds['pressure_stable'])  # XOR-like
        
        # Only triggers when all three met (rare)
        if condition_a and condition_b and condition_c:
            risk_count += 1
    
    # Final adjustment based on diagnostic key (only lowest bit used)
    modifier = 2 if diag_key & 0b1 else -2
    return risk_count * modifier

# Critical execution point
final_diagnostic = process_readings(sensor_data, threshold_map)

print(f"Result: {final_diagnostic}")