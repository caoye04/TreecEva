import math

# Simulated network node diagnostic system with red herrings and distractions
def analyze_node_health(status_str, load_factor, entropy_score):
    if 'ERR' in status_str:
        return -1
    elif 'WARN' in status_str:
        return load_factor * 0.5
    else:
        return math.log(load_factor + 1) * (1 - entropy_score / 100)

# Irrelevant helper function (decoy)
def calculate_compression_ratio(data_stream):
    base_size = len(data_stream)
    compressed_size = sum(1 for c in data_stream if c not in 'aeiou')
    return round(compressed_size / base_size, 3) if base_size else 0

def encode_routing_path(path_sequence):
    encoded = []
    for p in path_sequence:
        encoded.append(ord(p[0]) ^ len(p))
    return encoded

def decode_signal_strength(signal_code):
    # Unused complex transformation (dead path)
    return sum((signal_code[i] * (i + 1)) % 17 for i in range(len(signal_code)))

# Core data structure: simulated network nodes with mixed attributes
network_nodes = [
    {
        'id': 'N001',
        'status': 'OK',
        'load': 78.2,
        'meta': {'entropy': 43, 'flags': ['A', 'B'], 'temp': 67},
        'history': [0.81, 0.77, 'N/A', 0.83]
    },
    {
        'id': 'N002',
        'status': 'WARN',
        'load': 91.5,
        'meta': {'entropy': 61, 'flags': ['C'], 'temp': 72},
        'history': [0.65, 0.60, 0.58]
    },
    {
        'id': 'N003',
        'status': 'ERR_TIMEOUT',
        'load': 100.0,
        'meta': {'entropy': 88, 'flags': [], 'temp': 85},
        'history': []
    },
    {
        'id': 'N004',
        'status': 'OK',
        'load': 65.3,
        'meta': {'entropy': 29, 'flags': ['A'], 'temp': 54},
        'history': [0.90, 0.92]
    }
]

# Distractor variables (irrelevant accumulations)
compression_logs = [
    'data_chunk_001',
    'stream_segment_A',
    'buffer_frame_XYZ'
]

aggregate_compression = 0
for log in compression_logs:
    normalized = log.upper().replace('_', '')
    aggregate_compression += len(normalized) % 7

# Fake signal processing chain
routing_paths = [['A1', 'B2', 'C3'], ['X9', 'Y8'], ['M1']]
encoded_routes = [encode_routing_path(p) for p in routing_paths]
signal_codes = [[5, 3, 9], [2, 8], [7]]
decoded_strengths = [decode_signal_strength(code) for code in signal_codes]

# Real computation begins here — heavily buried
health_scores = []
for node in network_nodes:
    raw_status = node['status']
    current_load = node['load']
    entropy_val = node['meta']['entropy']
    
    score = analyze_node_health(raw_status, current_load, entropy_val)
    
    # Only include valid scores (non-error)
    if score >= 0:
        health_scores.append(score)

# Secondary distractor: string-based flag analysis
flag_counter = {}
for node in network_nodes:
    flags = node['meta']['flags']
    for f in flags:
        flag_counter[f] = flag_counter.get(f, 0) + 1

# Another decoy: temperature average (unused)
temp_values = [node['meta']['temp'] for node in network_nodes]
avg_temperature = sum(temp_values) / len(temp_values)

# Actual aggregation logic (target)
def aggregate_metrics(nodes):
    valid_scores = []n    total_weight = 0.0
    
    for node in nodes:
        s = node['status']
        ld = node['load']
        e = node['meta']['entropy']
        
        base_score = analyze_node_health(s, ld, e)
        
        # Only nodes with history contribute extra weight
        history_count = len([x for x in node['history'] if isinstance(x, float)])
        weight = 1 + (0.2 * history_count)
        
        if base_score >= 0:
            valid_scores.append(base_score * weight)
            total_weight += weight
    
    if total_weight == 0:
        return 0.0
    
    weighted_avg = sum(valid_scores) / total_weight
    
    # Final nonlinear correction based on number of healthy nodes
    healthy_count = len([n for n in nodes if 'ERR' not in n['status']])
    adjustment = math.sin(math.pi * healthy_count / 8)
    
    return round(weighted_avg * (1 + adjustment), 6)

# Execution point of interest
final_diagnostic = aggregate_metrics(network_nodes)

# Print result as required
print(f"Target result: {final_diagnostic}")