import math

# Simulated network diagnostic tool with decoy analytics and red herrings
def analyze_packet_flow(flow_data, threshold=1.5):
    if len(flow_data) == 0:
        return 0
    avg_load = sum(flow_data) / len(flow_data)
    peak_load = max(flow_data)
    stability_index = peak_load / (avg_load + 1e-9)
    
    # Irrelevant computation - red herring
    theoretical_capacity = 10 ** (math.log(len(flow_data) + 1, 2) + 1) if flow_data else 0
    efficiency_ratio = (avg_load / theoretical_capacity) * 100 if theoretical_capacity else 0
    
    # Distractor: unused function call result
    jitter_analysis = [abs(flow_data[i] - flow_data[i-1]) for i in range(1, len(flow_data))] if len(flow_data) > 1 else []
    smoothed_jitter = sum(jitter_analysis) / len(jitter_analysis) if jitter_analysis else 0
    
    return stability_index if stability_index > threshold else 0

# Legacy system compatibility layer (mostly dead code)
def legacy_checksum(data_str):
    checksum = 0
    for char in data_str:
        checksum += ord(char) * 31
    return checksum % 65537

# Unused but plausible-looking helper
def calculate_entropy(sequence):
    from collections import Counter
    counts = Counter(sequence)
    total = len(sequence)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return entropy

# Core diagnostic logic with embedded distractors
def evaluate_node_integrity(node_config, runtime_trace):
    config_hash = sum(ord(c) for c in node_config.get('id', ''))
    base_score = len(runtime_trace) * 2
    
    # Real logic path
    error_count = runtime_trace.count('ERROR')
    warning_count = runtime_trace.count('WARN')
    
    # Decoy metrics
    temp_timestamps = [ts for ts in runtime_trace if 'TIMESTAMP' in ts]
    duplicate_check = len(temp_timestamps) != len(set(temp_timestamps))
    
    # Real impact factors
    risk_penalty = error_count * 8 + warning_count * 3
    
    # Fake aggregation
    nominal_throughput = node_config.get('throughput_gbps', 10)
    expected_load_factor = math.sin(nominal_throughput)  # Never actually used
    
    return base_score - risk_penalty + (config_hash % 10)

# Main system health aggregator
def aggregate_metrics(log_entries, health_map):
    cumulative = 0
    anomaly_counter = 0
    
    # Dictionary operations (required feature)
    severity_weights = {'CRITICAL': 10, 'ERROR': 5, 'WARN': 2, 'INFO': 0}
    category_tally = {key: 0 for key in severity_weights.keys()}
    
    for entry in log_entries:
        level = entry.get('level', 'INFO')
        service = entry.get('service', 'unknown')
        
        if level in category_tally:
            category_tally[level] += 1
            
        # Real scoring logic
        if level == 'CRITICAL' and service == 'auth_gateway':
            anomaly_counter += 15
        
        # Distractor: complex unused transformation
        metadata_string = "".join([f"{k}{v}" for k, v in entry.items() if k != 'payload'])
        compressed_key = hash(metadata_string) & 0xFFFF
        lookup_value = math.sqrt(compressed_key) if compressed_key > 1000 else 0
        
        # Another red herring
        bit_pattern = bin(compressed_key).count('1')
        if bit_pattern > 8:
            cumulative += 1  # Misleading contribution
    
    # Real contribution to result
    cumulative += category_tally['CRITICAL'] * 12
    cumulative += category_tally['ERROR'] * 4
    cumulative += anomaly_counter
    
    # Tuple unpacking (suggested paradigm)
    weights = list(severity_weights.values())
    w_critical, w_error, w_warn, w_info = tuple(weights)
    
    # Dead code branch - never executed due to logic
    if w_info > 100:
        dummy_adjustment = sum(math.tan(i + 1) for i in range(50))
        cumulative -= int(dummy_adjustment)
    
    # Final adjustment based on health map
    for node_id, status in health_map.items():
        if status == 'degraded':
            cumulative += 7
        elif status == 'failed':
            cumulative += 20
    
    return cumulative

# Character counting distraction
def extract_signatures(event_log):
    unique_chars = set()
    total_chars = 0
    for event in event_log:
        cleaned = ''.join(c.lower() for c in event if c.isalnum())
        unique_chars.update(cleaned)
        total_chars += len(cleaned)
    diversity_score = len(unique_chars) / (total_chars + 1)
    return diversity_score

# --- Simulation Setup ---
if __name__ == "__main__":
    # Simulated inputs
    network_packets = [1.2, 1.8, 0.9, 2.1, 1.4, 3.0, 0.7, 1.3, 1.9, 2.2]
    packet_risk = analyze_packet_flow(network_packets, threshold=1.4)
    
    # Logs with mixed relevance
    network_state_log = [
        {'timestamp': 'T1', 'level': 'INFO', 'service': 'dns_resolver', 'payload': 'ok'},
        {'timestamp': 'T2', 'level': 'WARN', 'service': 'load_balancer', 'payload': 'high latency'},
        {'timestamp': 'T3', 'level': 'ERROR', 'service': 'db_proxy', 'payload': 'timeout'},
        {'timestamp': 'T4', 'level': 'CRITICAL', 'service': 'auth_gateway', 'payload': 'breach detected'},
        {'timestamp': 'T5', 'level': 'ERROR', 'service': 'cache_layer', 'payload': 'eviction storm'}
    ]
    
    # Health mapping
    system_health = {
        'node-alpha': 'active',
        'node-beta': 'degraded',
        'node-gamma': 'failed',
        'node-delta': 'active'
    }
    
    # Node evaluation (distractor chain)
    sample_config = {'id': 'beta_7', 'version': '3.4.1', 'throughput_gbps': 40}
    trace_events = ['NORMAL', 'WARN', 'NORMAL', 'ERROR', 'ERROR', 'WARN', 'NORMAL']
    integrity_score = evaluate_node_integrity(sample_config, trace_events)
    
    # Anomaly score from another source (partially relevant)
    raw_events = ["LOGIN_ATTEMPT", "FILE_ACCESS", "ADMIN_PRIVILEGE", "DATA_EXPORT"]
    entropy_metric = extract_signatures(raw_events)  # Computed but not used directly
    anomaly_score = int(packet_risk * 100) + 5  # Feeds into final result
    
    # Key statement containing answer
    final_diagnostic = aggregate_metrics(network_state_log, system_health) + anomaly_score
    
    # Print target result
    print(f"Result: {final_diagnostic}")