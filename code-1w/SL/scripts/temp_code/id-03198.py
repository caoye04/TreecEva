import math

def analyze_sensor(node_id, readings):
    # Irrelevant preprocessing (distractor)
    normalized = [r / max(readings) for r in readings if r > 0]
    stats = {
        'peak': max(readings),
        'baseline': sum(readings) / len(readings),
        'variance': sum((x - sum(readings)/len(readings))**2 for x in readings) / len(readings)
    }

    # Red herring: unused function
    def calibrate(x):
        return x * 0.98 + 2.1

    # Actual relevant logic buried here
    anomalies = []
    for i in range(1, len(readings)):
        if abs(readings[i] - readings[i-1]) > 15:
            anomalies.append(i)
    return anomalies

# Decoy data structures
legacy_systems = ['sensor_v1', 'sensor_v2']
temp_cache = {k: [] for k in legacy_systems}

# Simulated telemetry input (real data)
telemetry_packets = [
    {'node': 'A7', 'type': 'thermal', 'values': [23, 24, 23, 39, 25, 26]},
    {'node': 'B2', 'type': 'thermal', 'values': [18, 19, 20, 21, 22]},
    {'node': 'A7', 'type': 'thermal', 'values': [22, 23, 24, 25, 26, 27]},
    {'node': 'C5', 'type': 'vibration', 'values': [5, 6, 7, 8, 9]}
]

# Misleading aggregation path
aggregated_stats = {}
for packet in telemetry_packets:
    key = (packet['node'], packet['type'])
    if key not in aggregated_stats:
        aggregated_stats[key] = []
    aggregated_stats[key].extend(packet['values'])

# Dead code branch with decoy logic
if any('vibration' in p['type'] for p in telemetry_packets):
    vibration_nodes = [p['node'] for p in telemetry_packets if p['type'] == 'vibration']
    # This block does nothing useful
    temp_cache['sensor_v1'].append(len(vibration_nodes))

# Core processing chain begins here
primary_node = 'A7'
system_threshold = 35

# Filter only relevant packets
filtered_data = []
for packet in telemetry_packets:
    if packet['node'] == primary_node and packet['type'] == 'thermal':
        filtered_data.extend(packet['values'])

# Another distraction: set operations (partially relevant)
unique_readings = set(filtered_data)
outlier_candidates = {x for x in unique_readings if x > system_threshold}

# Diagnostic severity mapping (core logic)
def process_readings(data, threshold):
    spikes = [i for i in range(1, len(data)) if data[i] > threshold]
    
    # Bit manipulation red herring
    encoded_flag = 0
    for s in spikes:
        encoded_flag ^= (s << 2)
    
    # Real computation hidden among distractions
    base_score = len(spikes) * 100
    penalty = 0
    
    # Multiple conditional layers (nesting level 4)
    if len(data) > 5:
        if len(spikes) > 0:
            avg_gap = 0
            valid_gaps = []
            for i in range(1, len(data)):
                if data[i] > threshold and data[i-1] <= threshold:
                    valid_gaps.append(i)
            if valid_gaps:
                avg_gap = sum(valid_gaps) / len(valid_gaps)
                if avg_gap < 3.0:
                    penalty = 25
                elif avg_gap < 5.0:
                    penalty = 15
    
    # String manipulation distractor
    status_tag = ''.join([chr(97 + min(s % 26, 25)) for s in spikes[:3]]) if spikes else 'ok'
    
    # Final diagnostic calculation
    final_diagnostic = base_score - penalty
    
    # Unused but plausible-looking logging
    log_entry = f"DIAG:{final_diagnostic}|TAG:{status_tag}|FLAG:{encoded_flag}"
    return final_diagnostic

# Key execution point
final_diagnostic = process_readings(filtered_data, system_threshold)
print(f"Result: {final_diagnostic}")