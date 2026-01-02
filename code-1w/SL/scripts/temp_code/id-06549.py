from collections import defaultdict

# System diagnostics for a distributed sensor network
def analyze_sensor_readings(readings):
    stats = defaultdict(int)
    anomalies = 0
    total_power = 0.0

    for node_id, data in readings.items():
        stats['nodes_seen'] += 1
        node_power = 0
        
        for reading in data['values']:
            if abs(reading) > 95:
                anomalies += 1
            node_power += abs(reading) * 0.85
        
        total_power += node_power
        
        if node_power < 10:
            stats['low_power_nodes'] += 1

    avg_power = total_power / len(readings) if readings else 0
    return stats, avg_power, anomalies

# Energy capacity modeling
sensors = {
    'A1': {'values': [23, -45, 67, 89], 'status': 'active'},
    'B2': {'values': [12, 18, 5, -3], 'status': 'standby'},
    'C3': {'values': [78, 91, -88, 47], 'status': 'active'},
    'D4': {'values': [9, 4, 2, 1], 'status': 'maintenance'}
}

# Irrelevant diagnostic logs (distractor)
log_buffer = []
for i in range(3):
    log_buffer.append(f'Diagnostic pass {i+1}: nominal')

# Primary energy computation
base_units = [120, 150, 90, 200]
efficiency_map = {'A1': 0.88, 'B2': 0.75, 'C3': 0.92, 'D4': 0.60}

# Simulate intermediate processing
processing_offset = 0
for unit in base_units:
    if unit > 100:
        processing_offset += unit * 0.02

# Map units to nodes (semi-relevant)
unit_mapping = {}
for idx, unit in enumerate(base_units):
    unit_mapping[chr(65 + idx) + str(idx + 1)] = unit

# Red herring: unused transformation
transformed = [u ** 0.5 * 3 for u in base_units if u > 90]

# Core logic masked by distractions
def calculate_remaining_capacity(units, efficiency_map):
    capacity = 0
    adjustment_factor = 1.1
    
    # Real computation buried with noise
    for i, unit in enumerate(units):
        node_key = chr(65 + i) + str(i + 1)
        efficiency = efficiency_map.get(node_key, 0.7)
        
        # Actual contribution
        contribution = unit * efficiency
        
        # Conditional boost
        if unit > 100:
            contribution *= adjustment_factor
        
        capacity += contribution
    
    # Final adjustment based on system health
    diagnostics = analyze_sensor_readings(sensors)
    anomaly_count = diagnostics[2]
    
    if anomaly_count > 5:
        capacity *= 0.9
    
    return int(capacity)

# Execution point of interest
final_capacity = calculate_remaining_capacity(base_units, efficiency_map)

# Print result as required
print(f"Target result: {final_capacity}")