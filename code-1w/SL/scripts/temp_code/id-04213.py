import math

def analyze_phase_shift(frequency, amplitude, phase):
    # Irrelevant signal processing helper
    return amplitude * math.sin(2 * math.pi * frequency + phase)

def compute_entropy(data_stream):
    # Dead code path - never called
    entropy = 0.0
    for byte in data_stream:
        prob = byte / 256.0
        if prob > 0:
            entropy -= prob * math.log2(prob)
    return entropy

def validate_checksum(record):
    # Distractor function: looks important but unused
    return sum(record) % 256 == record[-1]

def transform_coordinates(x, y, z):
    # Unused geometric transformation
    radius = math.sqrt(x**2 + y**2 + z**2)
    theta = math.atan2(y, x)
    phi = math.acos(z / radius) if radius != 0 else 0
    return radius, theta, phi

def filter_anomalies(log_entries):
    # Misleading preprocessing step
    filtered = []
    for entry in log_entries:
        if entry['severity'] > 3:
            filtered.append(entry['timestamp'])
    return filtered

def aggregate_metrics(nodes, load_profile):
    # Core logic begins
    base_score = 0
    temp_buffer = []
    
    for node in nodes:
        if node['status'] != 'active':
            continue
            
        # Extract performance slices
        history = node['metrics'][-5:]  # slicing operation
        recent_avg = sum(history) / len(history)
        
        # Bit manipulation red herring
        diagnostic_flag = (node['id'] & 7) ^ 3
        if diagnostic_flag == 4:
            base_score -= 2
        
        # String-based distractor
        node_type = node['model'].upper().strip()
        if 'Z' in node_type:
            base_score += 1
        
        # Actual key computation
        stability = node['stability_factor']
        if stability > 0.85:
            base_score += int(recent_avg * stability)
        
        temp_buffer.append(diagnostic_flag)
    
    # Secondary calculation with dictionary
    load_map = {i: val for i, val in enumerate(load_profile)}
    adjustment = 0
    for k in load_map:
        if k % 3 == 0 and load_map[k] > 50:
            adjustment += 5
    
    # Decoy accumulation (never used)
    dummy_accum = 0
    for i in range(len(temp_buffer)):
        dummy_accum += temp_buffer[i] * (i + 1)
    
    # Final aggregation using relevant parts only
    final_score = base_score + adjustment
    
    # Extra distraction: unused sorting and grouping
    sorted_load = sorted(load_profile, reverse=True)
    groups = {'high': [], 'low': []}
    for x in sorted_load:
        groups['high'].append(x) if x > 75 else groups['low'].append(x)
    
    return final_score

# Simulated system state
network_nodes = [
    {
        'id': 12,
        'status': 'active',
        'model': 'NX-9000',
        'metrics': [85, 87, 89, 90, 84, 88, 86],
        'stability_factor': 0.91
    },
    {
        'id': 19,
        'status': 'inactive',  # will be skipped
        'model': 'MX-7B',
        'metrics': [70, 72, 68, 74, 75],
        'stability_factor': 0.78
    },
    {
        'id': 25,
        'status': 'active',
        'model': 'TX-Z3',
        'metrics': [60, 66, 63, 68, 65],
        'stability_factor': 0.87
    },
    {
        'id': 30,
        'status': 'active',
        'model': 'LX-550',
        'metrics': [95, 92, 94, 93, 91, 90],
        'stability_factor': 0.93
    }
]

system_load = [45, 52, 60, 78, 85, 50, 90, 30]

# Trigger key computation
final_diagnostic = aggregate_metrics(network_nodes, system_load)

# Print result as required
print(f"Result: {final_diagnostic}")