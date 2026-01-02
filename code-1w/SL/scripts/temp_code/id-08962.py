from collections import defaultdict, Counter
import math

# Simulated agricultural zone data with noise and auxiliary structures
def generate_zone_profile():
    profile = defaultdict(lambda: 'unknown')
    for i in range(3):
        profile[f'zone_{i+1}'] = 'active'
    return profile

def analyze_soil_composition(sensor_data):
    # Irrelevant analysis branch - dead end
    elements = ['N', 'P', 'K', 'Mg', 'Ca']
    traces = {el: sensor_data.count(el) * 0.01 for el in elements}
    return sum(traces.values())

def compute_root_depth(zones):
    # Misleading calculation - not used in final result
    depth_map = {}
    for z in zones:
        depth_map[z] = (len(z) * 1.5) if '3' in z else 0.7
    return depth_map

def extract_growth_patterns(data_stream):
    # Distractor function with partial relevance
    patterns = []
    for line in data_stream:
        tokens = line.split(',')
        if len(tokens) > 2 and tokens[1] == 'GROW':
            patterns.append(int(tokens[2]))
    return patterns

def calculate_harvest_efficiency(clusters, log_entries):
    # Core logic begins
    efficiency = 0
    adjustment_factor = 0.85
    
    # Real data processing
    event_count = defaultdict(int)
    for entry in log_entries:
        parts = entry.split('|')
        zone = parts[0]
        action = parts[1]
        event_count[zone] += 1
        
        if action == 'IRRIGATE' and 'X' in zone:
            efficiency -= 5
    
    # Critical accumulation path
    base_yield = 0
    for cluster_id, members in clusters.items():
        member_score = 0
        for member in members:
            if member.startswith('node'):
                idx = int(member.split('_')[1])
                member_score += idx % 4
        base_yield += member_score * len(members)
    
    # Secondary modifier from logs
    valid_logs = [e for e in log_entries if 'STATUS' in e]
    status_boost = 0
    for log in valid_logs:
        _, _, level_str = log.split('|')
        level = int(level_str)
        status_boost += int(math.sqrt(level))
    
    # Red herring: complex but unused transformation
    decoy_matrix = [[i*j for j in range(3)] for i in range(len(clusters))]
    checksum = sum(sum(row) for row in decoy_matrix) % 100
    
    # Another irrelevant bit manipulation chain
    flags = 0b1010
    for _ in range(status_boost % 5):
        flags = (flags << 1) | (flags >> 3)
        flags &= 0b1111
    
    # Actual answer computation
    intermediate = base_yield + status_boost
    final_adjustment = adjustment_factor if intermediate > 30 else 0.7
    final_yield = int(intermediate * final_adjustment)
    
    # Unused diagnostic output (misleading)
    diagnostics = {"score": final_yield + 100, "flag_check": flags}
    
    return final_yield

# Setup realistic input data
cluster_map = {
    'A': ['node_2', 'node_3', 'aux_1'],
    'B': ['node_1', 'node_4'],
    'C': ['node_0', 'node_5', 'node_2']
}

metrics_log = [
    'zone_1|IRRIGATE|50',
    'zone_X|IRRIGATE|60',
    'zone_2|STATUS|16',
    'zone_A|STATUS|25',
    'zone_X|IRRIGATE|70',
    'zone_C|STATUS|36'
]

# Simulate sensor inputs (unused but plausible)
sensor_readings = ['N,N,P,K','K,Ca,Mg','N,N,N','P,K,Ca']
sensor_trace_level = analyze_soil_composition(sensor_readings)

# Dead code path invocation
zone_profiles = generate_zone_profile()
root_depths = compute_root_depth(zone_profiles.keys())

data_stream = ['GROW,100', 'STOP,200', 'GROW,144']
growth_sequence = extract_growth_patterns(data_stream)

# Key execution point
final_yield = calculate_harvest_efficiency(cluster_map, metrics_log)
print(f"Result: {final_yield}")