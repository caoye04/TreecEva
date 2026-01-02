import math

def analyze_phase_shift(frequency, amplitude):
    # Irrelevant signal analysis function (dead end)
    return (amplitude * math.sin(frequency)) ** 2

def compute_entropy(data_stream):
    # Distractor: computes information entropy but not used in main logic
    entropy = 0.0
    for byte in data_stream:
        prob = byte / 256.0
        if prob > 0:
            entropy -= prob * math.log2(prob)
    return round(entropy, 4)

def filter_anomalies(log_series):
    # Misleading preprocessing: looks important but unused
    filtered = []
    for val in log_series:
        if abs(val - sum(log_series) / len(log_series)) < 2 * math.sqrt(sum((x - sum(log_series)/len(log_series))**2 for x in log_series)/len(log_series)):
            filtered.append(val)
    return set(filtered)

def validate_checksum(node_id_list):
    # Decoy validation function with complex logic
    checksum = 0
    for nid in node_id_list:
        temp = (nid ^ 0xABCD) & 0xFFFF
        checksum ^= temp
        checksum = (checksum << 3 | checksum >> 13) & 0xFFFF
    return checksum == 0xCAFE

def aggregate_metrics(nodes, load_profile):
    # Core logic hidden among distractions
    base_power = sum(n['capacity'] for n in nodes if n['active'])
    peak_util = max(load_profile) // len(nodes)  # integer division
    efficiency_ratio = base_power / (sum(n['capacity'] for n in nodes) or 1)
    
    # Bit manipulation red herring
    magic_flag = (0xFACE ^ 0xB00C) >> 4
    intermediate = (magic_flag + len(nodes)) & 0xFF
    
    # Real computation path
    sorted_load = sorted(load_profile, reverse=True)
    top_quartile_avg = sum(sorted_load[:len(sorted_load)//4]) / (len(sorted_load)//4 or 1)
    
    # Set operation to meet language feature requirement
    active_ids = {n['node_id'] for n in nodes if n['active']}
    reference_set = {1001, 1002, 1003, 1004, 1005}
    overlap_score = len(active_ids & reference_set)
    
    # Multiple concepts combined: arithmetic, logic, sorting, sets, bit ops
    diagnostic_weight = 0.8 if top_quartile_avg > 75 else 0.4
    stability_bias = 1 + (overlap_score * 0.05)
    
    # Final computation
    raw_diagnostic = (efficiency_ratio * diagnostic_weight * stability_bias * 1000)
    final_diagnostic = int(round(raw_diagnostic))
    
    # Dead code path
    if final_diagnostic < 0:
        fallback = math.gamma(final_diagnostic)
        return fallback
        
    return final_diagnostic

# Simulated system state
network_nodes = [
    {'node_id': 1001, 'capacity': 250, 'active': True},
    {'node_id': 1002, 'capacity': 300, 'active': True},
    {'node_id': 1003, 'capacity': 150, 'active': False},
    {'node_id': 1004, 'capacity': 400, 'active': True},
    {'node_id': 1005, 'capacity': 200, 'active': True}
]

system_load = [88, 92, 76, 81, 95, 89, 77, 85, 90, 83, 79, 87, 93, 84, 80, 91]

# Unused variables and computations to increase interference
baseline_metric = compute_entropy([65, 89, 72, 53, 91])
data_log = [120, 85, 94, 78, 110, 68, 92]
anomaly_filter = filter_anomalies(data_log)
phase_result = analyze_phase_shift(3.14159, 1.5)

# Key execution point
final_diagnostic = aggregate_metrics(network_nodes, system_load)

# Print result as required
print(f"Target result: {final_diagnostic}")