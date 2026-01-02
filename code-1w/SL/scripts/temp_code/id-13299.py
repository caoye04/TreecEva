import math

# Simulated network diagnostic system with decoy calculations

def analyze_bandwidth(data_stream):
    # Irrelevant function - dead code path
    return sum([x ** 0.5 for x in data_stream if x > 10])

def encrypt_payload(key, payload):
    # Misleading function involving bit manipulation but unused
    return (key << 3) ^ payload & 0xFF

def compute_stability_index(load_values, flags):
    # Core relevant logic buried among distractions
    base_score = 0
    adjustment_factor = 1.75
    
    # Red herring: complex flag analysis with partial usage
    flagged_nodes = [i for i, f in enumerate(flags) if f == 1]
    critical_count = len([f for f in flags if f == 2])
    
    # Decoy calculation with intermediate results
    entropy_proxy = 0.0
    for val in load_values:
        if val > 0:
            entropy_proxy += val * math.log(val + 1e-5)
    
    # Actual key computation chain (8-12 steps)
    raw_moment = sum(load_values) / len(load_values)
    variance_proxy = sum((x - raw_moment) ** 2 for x in load_values) / len(load_values)
    normalized_dispersion = math.sqrt(variance_proxy) / (raw_moment + 1e-3)
    
    # Apply non-linear transformation based on system rules
    stability_metric = 100 / (1 + math.exp(-normalized_dispersion * 10))
    
    # Modify using sparse node information (only index 0 matters)
    if len(flagged_nodes) > 0 and flagged_nodes[0] % 2 == 0:
        stability_metric *= 0.9
    
    # Final adjustment via modular weighting
    cycle_weight = (len(load_values) % 7) * 0.1
    stability_metric += cycle_weight * 15
    
    # Hidden rounding convention
    return int(round(stability_metric))

# Distractor variables and irrelevant data structures
network_trace = [12, 15, 8, 22, 7, 33, 14, 19]
security_codes = {101: 'ENCRYPTED', 205: 'PENDING'}
packet_headers = [(1, 'TCP'), (2, 'UDP')]

data_integrity_map = set()
for i in range(10):
    data_integrity_map.add(i * i % 17)

timestamp_buffer = list(map(lambda t: t * 1.003, [100, 200, 300]))

# Relevant input data (obscured among others)
network_load = [45, 60, 52, 48, 55, 50, 53]
security_flags = [1, 0, 2, 1, 0, 0, 2]  # Two types of flags present

# Dead code assignments to mislead
baseline_diagnostic = analyze_bandwidth(network_trace)
cipher_result = encrypt_payload(0xABC, 255)

# Key statement - answer depends on this execution
temporal_anchor = sum(timestamp_buffer) // len(timestamp_buffer)
diagnostic_log = {"start": temporal_anchor}

filtration_threshold = compute_stability_index(network_load, security_flags)

# Output requirement
print(f"Target result: {filtration_threshold}")