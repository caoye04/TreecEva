def analyze_signal_strength(signal: str) -> int:
    """ Irrelevant utility function for signal analysis (dead code path). """
    return sum(ord(c) for c in signal if c.isupper())


def encrypt_key(data: int) -> int:
    """ Distractor: Bit manipulation with no effect on main logic. """
    temp_key = data ^ 0xFFFF
    temp_key = (temp_key << 3) | (temp_key >> 29)
    return temp_key & 0x7FFFFFFF

# Global decoy constants (misleading)
MAX_BUFFER_SIZE = 1024
ERROR_THRESHOLD = 0.85
RETRY_LIMIT = 3

# Simulated system telemetry
system_load = [0.65, 0.72, 0.58, 0.91, 0.49, 0.77, 0.83]
system_flags = {"debug": False, "trace": True, "verbose": "low"}

# Network node configurations (mixed relevant and irrelevant data)
network_nodes = [
    {"id": "N1", "status": "active", "latency": 45, "bandwidth": 95, "version": "2.1"},
    {"id": "N2", "status": "inactive", "latency": 120, "bandwidth": 40, "version": "1.9"},
    {"id": "N3", "status": "active", "latency": 67, "bandwidth": 78, "version": "2.1"},
    {"id": "N4", "status": "active", "latency": 33, "bandwidth": 99, "version": "2.2"},
    {"id": "N5", "status": "failed", "latency": 300, "bandwidth": 5, "version": "1.7"}
]

# Decoy data structure (unused)
cached_results = {
    "checksum": 56342,
    "timestamp": "2023-11-05T10:30:00Z",
    "data": [encrypt_key(i * 17) for i in range(5)]
}

# Auxiliary function with string processing (partially relevant)
def parse_version(v: str) -> float:
    """ Extract version number from string using string methods. """
    if '.' in v:
        parts = v.split('.')
        major = parts[0]
        minor = parts[1].lstrip('0') or '0'
        return float(f"{major}.{minor}")
    return 0.0

# Complex aggregation with multiple distractions
def filter_active_nodes(nodes):
    active = []
    performance_scores = []
    for node in nodes:
        # Irrelevant check
        if len(node['id']) < 2:
            continue
        
        # Misleading intermediate calculation
        raw_score = node['bandwidth'] - node['latency']
        adjusted = raw_score + (10 if '2.' in node['version'] else 0)
        
        # Actual filtering logic buried
        if node['status'] == 'active':
            active.append(node)
            performance_scores.append(adjusted)
    
    # Dead return branch
    if not performance_scores and system_flags['trace']:
        return [], [0]
    
    return active, performance_scores

# Heavily distracted metric computation
def calculate_health_index(metrics: list, load_profile: list) -> float:
    base = sum(metrics) / len(metrics)
    
    # Distractor: unused transformation
    inverted = [1.0 / (x + 1) for x in load_profile if x > 0]
    avg_inverted = sum(inverted) / len(inverted) if inverted else 0.0
    
    # Red herring normalization
    normalized_load = max(min(sum(load_profile) / len(load_profile), 1.0), 0.0)
    
    # Core logic
    penalty = 0
    for load in load_profile:
        if load > 0.8:
            penalty += 15
    
    result = base - penalty
    return round(result, 4)

# Main aggregation with string-based version filtering distraction
def aggregate_metrics(nodes, load):
    # Step 1: Filter active nodes
    active_nodes, perf_scores = filter_active_nodes(nodes)
    
    # Step 2: Version-based weight (string method usage)
    v_weights = []
    for node in active_nodes:
        ver = parse_version(node['version'])
        # Only versions >= 2.1 get bonus
        weight = 1.1 if ver >= 2.1 else 1.0
        v_weights.append(weight)
    
    # Step 3: Apply weights to performance scores
    weighted_scores = [score * w for score, w in zip(perf_scores, v_weights)]
    
    # Step 4: Calculate base health
    base_metric = calculate_health_index(weighted_scores, load)
    
    # Step 5: Final adjustment using irrelevant global constant
    # (ERROR_THRESHOLD looks important but isn't used)
    final_value = base_metric + 10.5  # Fixed calibration offset
    
    # Step 6: Unrelated string operation (distraction)
    log_entry = f"Diagnostic run on {len(active_nodes)} nodes."
    log_entry = log_entry.replace("run", "execution").upper()
    
    # Step 7: Spurious bit operation (no effect)
    magic_offset = (17 << 2) ^ 5
    magic_offset = magic_offset & ~magic_offset  # becomes zero
    
    # Final result
    final_diagnostic = base_metric + 10.5
    return final_diagnostic

# Key execution point
final_diagnostic = aggregate_metrics(network_nodes, system_load)
print(f"Target result: {final_diagnostic}")