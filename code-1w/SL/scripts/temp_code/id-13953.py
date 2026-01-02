from collections import defaultdict, Counter

# Simulated sensor network data with metadata
def fetch_sensor_streams():
    return [
        {'id': 'S1', 'type': 'temp', 'readings': [23.4, 24.1, 25.0, 26.2, 25.8], 'calibrated': True},
        {'id': 'S2', 'type': 'humid', 'readings': [45, 47, 50, 52, 49], 'calibrated': False},
        {'id': 'S3', 'type': 'temp', 'readings': [22.8, 23.1, 24.0, 25.5, 26.0], 'calibrated': True},
        {'id': 'S4', 'type': 'pressure', 'readings': [1013, 1015, 1012, 1010, 1008], 'calibrated': True},
        {'id': 'S5', 'type': 'temp', 'readings': [30.2, 31.0, 29.8, 32.1, 31.5], 'calibrated': True}
    ]

# Irrelevant utility: converts readings to string format (dead path)
def stringify_readings(data):
    result = []
    for entry in data:
        result.append({
            'id': entry['id'],
            'values': ','.join(map(str, entry['readings']))
        })
    return result

# Misleading transformation: applies arbitrary scaling (not used in final logic)
def scale_readings(data, factor=1.0):
    scaled = []
    for entry in data:
        scaled.append({
            'id': entry['id'],
            'scaled_readings': [round(r * factor, 2) for r in entry['readings']]
        })
    return scaled

# Decoy function: looks important but unused
# Analyzes volatility without contributing to result
def analyze_volatility(streams):
    volatility = {}
    for s in streams:
        diffs = [abs(s['readings'][i] - s['readings'][i-1]) for i in range(1, len(s['readings']))]
        volatility[s['id']] = round(sum(diffs) / len(diffs), 3)
    return volatility

# Real processing begins here
sensor_data = fetch_sensor_streams()

# Extract only calibrated temperature sensors (key filtering)
temp_sensors = [s for s in sensor_data if s['type'] == 'temp' and s['calibrated']]

# Compute average per sensor
averages = []
for sensor in temp_sensors:
    avg = sum(sensor['readings']) / len(sensor['readings'])
    averages.append(round(avg, 2))

# Aggregate all temperature readings from valid sensors
all_temp_readings = []
for sensor in temp_sensors:
    all_temp_readings.extend(sensor['readings'])

# Calculate global stats (some are distractors)
global_mean = sum(all_temp_readings) / len(all_temp_readings)
global_min = min(all_temp_readings)
global_max = max(all_temp_readings)
global_std_dev = (sum((x - global_mean) ** 2 for x in all_temp_readings) / len(all_temp_readings)) ** 0.5

# Define thresholds using lambda (relevant)
threshold_rules = {
    'high_risk': lambda x: x > global_mean + 1.5 * global_std_dev,
    'moderate_risk': lambda x: global_mean + 0.5 * global_std_dev < x <= global_mean + 1.5 * global_std_dev,
    'normal': lambda x: x <= global_mean + 0.5 * global_std_dev
}

# Count risk distribution using Counter (relevant)
risk_levels = []
for val in all_temp_readings:
    if threshold_rules['high_risk'](val):
        risk_levels.append('high_risk')
    elif threshold_rules['moderate_risk'](val):
        risk_levels.append('moderate_risk')
    else:
        risk_levels.append('normal')

counts = Counter(risk_levels)

# Build threshold map (used later)
threshold_map = {
    'high': global_mean + 1.5 * global_std_dev,
    'moderate': global_mean + 0.5 * global_std_dev,
    'count_high': counts['high_risk'],
    'count_normal': counts['normal']
}

# Filtered data for final processing
filtered_data = [round(x, 2) for x in all_temp_readings if x > global_mean]

# Secondary decoy structure: unused device registry
device_registry = defaultdict(lambda: 'unknown')
device_registry.update({s['id']: s['type'] for s in sensor_data})

# Another red herring: builds a set of unique rounded values (computed but unused)
unique_rounded = {round(temp, 0) for temp in all_temp_readings}
spike_set = {t for t in all_temp_readings if t > global_max - 0.5}

# Core diagnostic processor (uses filtered_data and threshold_map)
def process_readings(readings, thresholds):
    # Nested logic with multiple steps
    high_risk_count = 0
    cumulative_score = 0.0
    
    for val in readings:
        if val > thresholds['high']:
            high_risk_count += 1
            cumulative_score += (val - thresholds['high']) * 2.5
        elif val > thresholds['moderate']:
            cumulative_score += (val - thresholds['moderate']) * 1.2
    
    # Additional logic layer
    base_penalty = 0
    if high_risk_count > 2:
        base_penalty = 15
    elif high_risk_count == 1 or high_risk_count == 2:
        base_penalty = 8
    
    # Distractor variables inside function
    synthetic_index = len(readings) + sum(1 for v in readings if v > thresholds['moderate'])
    stability_factor = (thresholds['count_normal'] / len(all_temp_readings)) * 100
    
    # Final computation chain
    intermediate = cumulative_score * (1 + thresholds['count_high'] * 0.1)
    adjusted = intermediate - base_penalty
    final_score = round(adjusted * 1.07, 2)  # Final adjustment
    
    return int(round(final_score))

# Execution point of interest
final_diagnostic = process_readings(filtered_data, threshold_map)

# Print result as required
print(f"Result: {final_diagnostic}")