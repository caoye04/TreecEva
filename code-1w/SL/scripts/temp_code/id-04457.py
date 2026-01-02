from collections import defaultdict, Counter
import math

# Simulated sensor data from a distributed environmental monitoring system
time_series_data = [
    {'temp': 23.4, 'humidity': 65, 'co2': 410, 'pm25': 12, 'node': 'A1'},
    {'temp': 24.1, 'humidity': 63, 'co2': 425, 'pm25': 14, 'node': 'A2'},
    {'temp': 22.9, 'humidity': 67, 'co2': 405, 'pm25': 11, 'node': 'A1'},
    {'temp': 25.3, 'humidity': 59, 'co2': 460, 'pm25': 18, 'node': 'B1'},
    {'temp': 24.8, 'humidity': 60, 'co2': 445, 'pm25': 16, 'node': 'B2'},
    {'temp': 23.7, 'humidity': 66, 'co2': 412, 'pm25': 13, 'node': 'A1'},
    {'temp': 26.0, 'humidity': 57, 'co2': 480, 'pm25': 21, 'node': 'B1'},
    {'temp': 22.5, 'humidity': 69, 'co2': 398, 'pm25': 10, 'node': 'C1'}
]

# Irrelevant statistical counters (distractor)
decoy_counter = Counter()
for entry in time_series_data:
    decoy_counter[entry['node']] += 1

# Node calibration offsets (some irrelevant, some used)
calibration_offsets = {
    'A1': -1.2, 'A2': -0.9, 'B1': 1.5, 'B2': 1.1, 'C1': 0.3, 'C2': -0.7, 'D1': 2.0
}

# Aggregation containers
raw_readings = defaultdict(list)
valid_nodes = set()
systematic_bias_map = {}

# Process and group valid sensor readings by node
for record in time_series_data:
    node_id = record['node']
    if node_id not in calibration_offsets:
        continue  # Skip uncalibrated nodes
    
    # Extract and adjust readings
    adjusted_co2 = record['co2'] + calibration_offsets[node_id]
    adjusted_pm25 = record['pm25'] * 1.08  # Empirical correction factor
    temperature_flag = record['temp'] > 24.0
    
    # Store raw adjusted values for later processing
    raw_readings[node_id].append({
        'co2': adjusted_co2,
        'pm25': adjusted_pm25,
        'flag': temperature_flag
    })
    valid_nodes.add(node_id)

# Compute per-node average pollution index (intermediate distractor)
pollution_index_summary = {}
for node, readings in raw_readings.items():
    avg_co2 = sum(r['co2'] for r in readings) / len(readings)
    avg_pm25 = sum(r['pm25'] for r in readings) / len(readings)
    index = (avg_co2 / 400) * 50 + (avg_pm25 / 35) * 100
    pollution_index_summary[node] = round(index, 2)

# Historical baseline (unused legacy values - red herring)
historical_averages = {
    'A1': 98.2, 'A2': 96.5, 'B1': 112.3, 'B2': 105.7, 'C1': 88.9
}

# Compute dynamic threshold based on data distribution (used only partially)
all_pm25_values = []
for readings in raw_readings.values():
    all_pm25_values.extend([r['pm25'] for r in readings])

sorted_pm25 = sorted(all_pm25_values)
median_pm25 = sorted_pm25[len(sorted_pm25)//2]
extreme_threshold = median_pm25 * 1.75

# Determine high-risk events (dead code path - never used later)
high_risk_events = 0
for readings in raw_readings.values():
    for r in readings:
        if r['pm25'] > extreme_threshold and r['co2'] > 450:
            high_risk_events += 1

# System-wide health scoring logic
aggregate_health_score = 0.0
anomaly_count = 0

for node, data in raw_readings.items():
    for sample in data:
        # Weighted health impact calculation
        co2_impact = max(0, (sample['co2'] - 400) / 10)
        pm25_impact = max(0, (sample['pm25'] - 10) * 1.5)
        
        reading_score = 100 - (co2_impact * 0.8 + pm25_impact * 1.2)
        reading_score = max(10, min(100, reading_score))  # Clamp to range
        
        aggregate_health_score += reading_score
        
        if sample['flag']:
            anomaly_count += 1

# Apply count-based adjustment (neutralized - red herring)
anomaly_adjustment = 0
if anomaly_count > 5:
    anomaly_adjustment = -anomaly_count * 0.5

# Calculate systematic bias from calibration drift (actual relevant correction)
bias_accumulator = 0.0
for node in raw_readings.keys():
    offset = calibration_offsets.get(node, 0)
    if offset > 0:
        bias_accumulator += offset * 0.7
    else:
        bias_accumulator -= abs(offset) * 0.3

system_bias_correction = -bias_accumulator * 1.25

# Final diagnostic score computation (target statement)
final_diagnostic = aggregate_health_score + system_bias_correction

# Decoy final calculations (irrelevant)
consistency_score = len(pollution_index_summary) * 10 - abs(bias_accumulator)
validation_metric = (sum(calibration_offsets[n] for n in valid_nodes if n in calibration_offsets) + 10) ** 0.5

print(f"Result: {final_diagnostic}")