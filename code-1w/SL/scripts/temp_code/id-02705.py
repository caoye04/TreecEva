from collections import defaultdict

# Simulate sensor data aggregation and weighted anomaly detection
def collect_readings():
    raw_data = [
        {'sensor': 'temp', 'zone': 'A', 'value': 23.5},
        {'sensor': 'pressure', 'zone': 'B', 'value': 101.2},
        {'sensor': 'temp', 'zone': 'A', 'value': 24.1},
        {'sensor': 'humidity', 'zone': 'C', 'value': 45.0},
        {'sensor': 'temp', 'zone': 'B', 'value': 22.8},
        {'sensor': 'pressure', 'zone': 'A', 'value': 100.8},
        {'sensor': 'humidity', 'zone': 'A', 'value': 47.3},
        {'sensor': 'temp', 'zone': 'C', 'value': 25.6}
    ]
    return raw_data

# Group readings by sensor type and zone
def group_by_source(data):
    grouped = defaultdict(lambda: defaultdict(list))
    for entry in data:
        grouped[entry['sensor']][entry['zone']].append(entry['value'])
    return grouped

# Calculate average per sensor-zone pair
def compute_averages(grouped_data):
    averages = defaultdict(dict)
    for sensor, zones in grouped_data.items():
        for zone, values in zones.items():
            avg = sum(values) / len(values)
            averages[sensor][zone] = round(avg, 2)
    return averages

# Identify anomalies based on threshold deviation (dummy logic for distraction)
def detect_anomalies(averages):
    anomalies = []
    thresholds = {'temp': 25.0, 'pressure': 102.0, 'humidity': 50.0}
    for sensor, zones in averages.items():
        for zone, avg in zones.items():
            if avg > thresholds.get(sensor, 999):
                anomalies.append((sensor, zone, avg))
    return anomalies

# Apply weighting schema to prioritize certain sensor types and zones
def apply_weighting_schema(averages):
    weights = defaultdict(float)
    weight_map = {'temp': 1.5, 'pressure': 1.2, 'humidity': 0.8}
    zone_factor = {'A': 1.1, 'B': 1.0, 'C': 0.9}
    
    for sensor, zones in averages.items():
        for zone, avg in zones.items():
            base_weight = weight_map[sensor]
            location_bonus = zone_factor[zone]
            # Irrelevant transformation (distractor)
            temp_adjustment = (avg * 0.01) ** 0.5 if avg > 0 else 0
            final_weight = base_weight * location_bonus
            weights[(sensor, zone)] = round(final_weight, 3)
    return weights

# Main processing function with composite metric calculation
def process_metrics(data, weights):
    grouped = group_by_source(data)
    averages = compute_averages(grouped)
    anomalies = detect_anomalies(averages)  # Computed but not used (distractor)
    
    # Dummy string manipulation to increase cognitive load
    report_id = "RPT-" + "metrics".upper() + "-2024"
    report_parts = report_id.split('-')
    version = int(report_parts[-1]) % 100
    scaling_hint = len(report_parts)  # Unused
    
    total_weighted_sum = 0.0
    total_normalization = 0.0
    
    for entry in data:
        sensor = entry['sensor']
        zone = entry['zone']
        value = entry['value']
        key = (sensor, zone)
        
        # Use latest average for normalization reference (simplified)
        avg_val = averages[sensor][zone]
        normalized_contribution = value / avg_val if avg_val != 0 else 0
        weight = weights.get(key, 1.0)
        
        total_weighted_sum += normalized_contribution * weight
        total_normalization += weight
    
    # Final composite score
    composite_score = total_weighted_sum / total_normalization if total_normalization != 0 else 0
    
    # Additional irrelevant computation (dead path)
    debug_checksum = 0
    for c in report_id:
        debug_checksum += ord(c) % 7
    debug_checksum = debug_checksum % 13  # Not used
    
    # Key result variable
    final_score = int(round(composite_score * 100))
    return final_score

# Execution flow
data = collect_readings()
weights = apply_weighting_schema(compute_averages(group_by_source(data)))
final_score = process_metrics(data, weights)
print(f"Result: {final_score}")