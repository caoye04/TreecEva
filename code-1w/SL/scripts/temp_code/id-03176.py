from collections import defaultdict
import math

def analyze_readings(sensor_log):
    readings_count = defaultdict(int)
    total_entries = 0
    anomalies = []

    for entry in sensor_log:
        sensor_id = entry['sensor']
        value = entry['value']
        readings_count[sensor_id] += 1
        total_entries += 1

        if value < 10 or value > 90:
            anomalies.append((sensor_id, value))

    return readings_count, len(anomalies)

def preprocess_data(raw_log):
    cleaned = []
    null_count = 0
    for item in raw_log:
        if item['value'] is None:
            null_count += 1
            continue
        if str(item['value']).strip() == '':
            null_count += 1
            continue
        cleaned.append(item)
    
    # Distraction: unused transformation
    temp_shift = [math.sin(x['value'] * 0.1) for x in cleaned if x['value'] > 0]
    scaling_factor = sum(temp_shift) / len(temp_shift) if temp_shift else 1.0

    return cleaned

def calculate_efficiency(data):
    base_score = 100.0
    penalty = 0
    warning_flags = 0

    for record in data:
        val = record['value']
        if val > 80:
            penalty += 3
        elif val < 20:
            penalty += 5
        else:
            base_score += 0.1  # Minor reward

        category = record.get('type', 'unknown')
        if category == 'critical' and val > 50:
            warning_flags += 1

    adjustment = math.log(penalty + 1) * warning_flags
    return int(base_score - penalty - adjustment)

# Simulated sensor input
raw_sensor_data = [
    {'sensor': 'A1', 'value': 5, 'type': 'critical'},
    {'sensor': 'A1', 'value': 15, 'type': 'normal'},
    {'sensor': 'B2', 'value': 85, 'type': 'normal'},
    {'sensor': 'B2', 'value': 95, 'type': 'critical'},
    {'sensor': 'C3', 'value': 40, 'type': 'normal'},
    {'sensor': 'C3', 'value': 60, 'type': 'normal'},
    {'sensor': 'A1', 'value': None, 'type': 'normal'},
    {'sensor': 'D4', 'value': 50, 'type': 'critical'},
    {'sensor': 'D4', 'value': 25, 'type': 'normal'}
]

# Step 1: Preprocess to remove invalid entries
filtered_data = preprocess_data(raw_sensor_data)

# Step 2: Analyze distribution (partially relevant)
data_counts, anomaly_count = analyze_readings(filtered_data)

# Misleading intermediate calculation
average_per_sensor = sum(data_counts.values()) / len(data_counts) if data_counts else 0
threshold_adjustment = average_per_sensor * 0.2

# Key processing step: derive efficiency score
processed_data = filtered_data  # For clarity

# --- KEY STATEMENT ---
efficiency_score = calculate_efficiency(processed_data)

# Final output
print(f"Result: {efficiency_score}")