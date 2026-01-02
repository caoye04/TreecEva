import math

def analyze_node_load(stress_level, threshold=75):
    return 'overloaded' if stress_level > threshold else 'stable'

def compute_entropy(data_stream):
    # Irrelevant entropy calculation for distraction
    freq_map = {}
    for bit in data_stream:
        freq_map[bit] = freq_map.get(bit, 0) + 1
    entropy = 0
    total = len(data_stream)
    for count in freq_map.values():
        p = count / total
        entropy -= p * math.log2(p) if p > 0 else 0
    return round(entropy, 3)

def transform_coordinates(x, y, z):
    # Unused coordinate transformation (red herring)
    radius = math.sqrt(x**2 + y**2 + z**2)
    theta = math.atan2(y, x)
    phi = math.acos(z / radius) if radius != 0 else 0
    return (radius, theta, phi)

def evaluate_redundancy(nodes):
    # Misleading function that calculates redundancy but isn't used in final result
    pairs = [(i, j) for i in range(len(nodes)) for j in range(i+1, len(nodes))]
    duplicates = 0
    for i, j in pairs:
        if nodes[i]['signature'] == nodes[j]['signature']:
            duplicates += 1
    return duplicates

def filter_active_nodes(node_list):
    return [node for node in node_list if node['status'] == 'ACTIVE']

def calculate_health_score(node):
    base = node['performance'] * 0.6
    penalty = 0
    if node['errors'] > 5:
        penalty += node['errors'] * 2
    if node['temperature'] > 80:
        penalty += 10
    return max(base - penalty, 0)

def aggregate_metrics(node_cluster):
    active_nodes = filter_active_nodes(node_cluster)
    scores = [calculate_health_score(node) for node in active_nodes]
    
    # Real computation path
    raw_sum = sum(scores)
    adjustment_factor = 1.0
    
    # Simulate conditional logic with distractors
    high_temp_count = len([n for n in active_nodes if n['temperature'] > 85])
    if high_temp_count > 2:
        adjustment_factor *= 0.9
    elif high_temp_count == 0:
        adjustment_factor *= 1.05
    
    # Bit manipulation red herring
    bitmask = 0
    for i, score in enumerate(scores):
        if score > 40:
            bitmask |= (1 << i)
    
    # Actual answer depends on adjusted sum
    adjusted_sum = raw_sum * adjustment_factor
    
    # More distractions: unused list comprehension
    peak_moments = [i for i, s in enumerate(scores) if s > 50]
    avg_gap = sum([scores[i] - scores[i-1] for i in range(1, len(scores))]) if len(scores) > 1 else 0
    
    # Final diagnostic is rounded to nearest integer
    return int(round(adjusted_sum))

# Simulated network node data
network_nodes = [
    {
        'id': 'N001', 'status': 'ACTIVE', 'performance': 88,
        'errors': 3, 'temperature': 78, 'load_avg': 72.1,
        'signature': 'A1B2C3', 'region': 'east'
    },
    {
        'id': 'N002', 'status': 'INACTIVE', 'performance': 92,
        'errors': 6, 'temperature': 88, 'load_avg': 81.5,
        'signature': 'D4E5F6', 'region': 'west'
    },
    {
        'id': 'N003', 'status': 'ACTIVE', 'performance': 75,
        'errors': 7, 'temperature': 82, 'load_avg': 68.9,
        'signature': 'G7H8I9', 'region': 'east'
    },
    {
        'id': 'N004', 'status': 'ACTIVE', 'performance': 95,
        'errors': 2, 'temperature': 76, 'load_avg': 77.3,
        'signature': 'J1K2L3', 'region': 'central'
    },
    {
        'id': 'N005', 'status': 'ACTIVE', 'performance': 67,
        'errors': 4, 'temperature': 89, 'load_avg': 85.0,
        'signature': 'M4N5O6', 'region': 'east'
    },
    {
        'id': 'N006', 'status': 'ACTIVE', 'performance': 83,
        'errors': 5, 'temperature': 87, 'load_avg': 73.2,
        'signature': 'P7Q8R9', 'region': 'west'
    }
]

# Irrelevant pre-processing (dead code path)
data_trace = [1,0,1,1,0,0,0,1]
entropy_value = compute_entropy(data_trace)

# Unused coordinate transformation
coords = transform_coordinates(10, 20, 15)

# Real execution flow
node_redundancy = evaluate_redundancy(network_nodes)  # Computed but not used

final_diagnostic = aggregate_metrics(network_nodes)
print(f"Result: {final_diagnostic}")