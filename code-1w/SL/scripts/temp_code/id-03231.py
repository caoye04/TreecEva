from collections import defaultdict, Counter

# Simulated sensor array data with metadata
def fetch_sensor_data():
    raw_data = [
        {'id': 'S1', 'readings': [0.45, 0.47, 0.53, 0.61], 'type': 'thermal', 'active': True},
        {'id': 'S2', 'readings': [1.21, None, 1.19, 1.23], 'type': 'pressure', 'active': True},
        {'id': 'S3', 'readings': [0.88, 0.85, 0.82, 0.79], 'type': 'thermal', 'active': False},
        {'id': 'S4', 'readings': [2.05, 2.07, 2.03], 'type': 'flow', 'active': True},
        {'id': 'S5', 'readings': [None, None, 1.99], 'type': 'flow', 'active': True}
    ]
    return raw_data

def clean_readings(sensor_list):
    cleaned = []
    null_count = 0
    for sensor in sensor_list:
        readings = sensor['readings']
        valid_readings = [r for r in readings if r is not None]
        null_count += len(readings) - len(valid_readings)
        if len(valid_readings) > 0:
            avg = sum(valid_readings) / len(valid_readings)
            # Misleading normalization (not used later)
            normalized_avg = avg * 0.98 if sensor['type'] == 'thermal' else avg
            sensor['avg'] = avg
            sensor['cleaned_count'] = len(valid_readings)
        else:
            sensor['avg'] = 0.0
        cleaned.append(sensor)
    # Dead code path - never accessed
    if null_count > 100:
        raise RuntimeError("Excessive nulls")
    return cleaned

def classify_sensors_by_type(sensor_data):
    groups = defaultdict(list)
    for s in sensor_data:
        groups[s['type']].append(s)
    return groups

def calculate_system_health(metrics):
    # Irrelevant health metric calculation (distractor)
    total_sensors = len(metrics)
    active_sensors = len([m for m in metrics if m.get('active')])
    if total_sensors == 0:
        return 0.0
    return (active_sensors / total_sensors) * 100

def filter_active_thermal_sensors(data):
    # Only active thermal sensors are relevant
    filtered = []
    for entry in data:
        if entry['type'] == 'thermal' and entry['active']:
            filtered.append(entry)
    return filtered

def analyze_trend(values):
    if len(values) < 2:
        return 'stable'
    diffs = [values[i+1] - values[i] for i in range(len(values)-1)]
    trend_sum = sum(diffs)
    return 'increasing' if trend_sum > 0 else 'decreasing' if trend_sum < 0 else 'stable'

def process_readings(valid_sensors, factor):
    combined_readings = []    
    type_counter = Counter()
    for s in valid_sensors:
        type_counter[s['type']] += 1
        combined_readings.extend(s['readings'])
    
    # Real computation path
    base_value = sum(r for r in combined_readings if r is not None)
    adjusted = base_value * factor
    
    # Distractor: complex unused transformation
    transformed = [((x ** 2) + 1.5) / 3.7 for x in combined_readings if x > 0.5]
    summary_score = len(transformed) * 0.7
    
    # Multiple layers of irrelevant logic
    status_map = {'increasing': 1, 'decreasing': -1, 'stable': 0}
    trend = analyze_trend(combined_readings)
    trend_index = status_map[trend]
    
    # Final result built from correct path only
    result = int(adjusted + trend_index * 100)
    
    # Dead assignment
    final_weighted_score = summary_score + result * 0.1  
    
    return result

# --- Execution Flow ---
data_pool = fetch_sensor_data()
processed_sensors = clean_readings(data_pool)

# Irrelevant grouping (distractor)
sensor_categories = classify_sensors_by_type(processed_sensors)
health_metric = calculate_system_health(processed_sensors)  # Not used

# Critical filtering step
working_thermal_units = filter_active_thermal_sensors(processed_sensors)

calibration_factor = 1.85

# Key execution point
final_diagnostic = process_readings(working_thermal_units, calibration_factor)

print(f"Result: {final_diagnostic}")