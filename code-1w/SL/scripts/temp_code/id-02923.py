import math

# Simulated network telemetry data
def collect_telemetry(nodes):
    signal_strength = {}
    for node in nodes:
        raw = (hash(node) % 100) + 1
        normalized = abs(math.sin(raw)) * 100
        signal_strength[node] = round(normalized, 2)
    return signal_strength

# Legacy function – not used but looks relevant
def deprecated_aggregation(data):
    return sum(v ** 0.5 for v in data.values()) // len(data)

# Redundant transformation (distractor)
def transform_readings(readings):
    adjusted = {}
    for k, v in readings.items():
        if v < 30:
            adjusted[k] = v * 1.8
        elif v < 70:
            adjusted[k] = v * 1.2
        else:
            adjusted[k] = v * 0.9
    return adjusted

# Misleading diagnostic with similar name
def compute_health_score(entity_map):
    total = 0
    for key in entity_map:
        if 'backup' in key:
            total += 15
        elif 'primary' in key:
            total += 25
    return total * len(entity_map)

# Core logic disguised among distractors
def filter_critical_nodes(node_data, threshold=65.0):
    critical = []
    for node, strength in node_data.items():
        if strength > threshold and 'test' not in node:
            critical.append(node)
    return set(critical)

def calculate_entropy(values):
    total = sum(values)
    probs = [v / total for v in values if v > 0]
    entropy = -sum(p * math.log2(p) for p in probs)
    return round(entropy, 4)

# Key function: aggregates metrics using multiple concepts
def aggregate_metrics(nodes, load_profile):
    telemetry = collect_telemetry(nodes)
    
    # Distractor: transform but result unused
    transformed_telemetry = transform_readings(telemetry)
    
    # Actual path: find critical nodes above threshold
    critical_set = filter_critical_nodes(telemetry, 65.0)
    
    # Simulate load distribution across nodes
    base_load = sum(load_profile) / len(load_profile)
    peak_load = max(load_profile)
    
    # Use set difference to exclude test nodes (bit manipulation red herring below)
    operational_nodes = critical_set - {n for n in critical_set if 'temp' in n}
    
    # Decoy bitwise operation (irrelevant to final result)
    decoy_flag = 0
    for i, node in enumerate(operational_nodes):
        decoy_flag ^= hash(node) & 0xF
        decoy_flag += i * 2
    
    # Real computation begins: extract telemetry values for operational nodes
    op_values = [telemetry[n] for n in operational_nodes]
    
    # Another red herring: dictionary reversal that does nothing
    reversed_map = {v: k for k, v in telemetry.items()}
    
    # Compute entropy of operational node signals
    signal_entropy = calculate_entropy(op_values)
    
    # Accumulate secondary metric: count of high-load periods
    high_load_count = sum(1 for x in load_profile if x > base_load)
    
    # Final formula: combines entropy, count, and fixed offset
    # This is where the answer is determined
    final_value = int((signal_entropy * 1000) + high_load_count * 10) + 50
    
    return final_value

# Setup realistic input data
network_nodes = [
    'primary_gateway_01', 'backup_relay_x9', 'test_stub_alpha',
    'primary_gateway_02', 'sensor_hub_m7', 'temp_node_debug',
    'primary_gateway_03'
]

system_load = [85, 92, 78, 96, 88, 76, 91, 83, 89, 95]

# Dead code path – never called, but looks important
def generate_diagnostic_report():
    return {"status": "inactive", "code": -1}

# Irrelevant list processing (unused)
buffer_pool = [i * 3 + 2 for i in range(15) if i % 4 != 0]
buffer_pool = [b for b in buffer_pool if b < 40]

# Key execution point
final_diagnostic = aggregate_metrics(network_nodes, system_load)

# Output result as required
print(f"Result: {final_diagnostic}")