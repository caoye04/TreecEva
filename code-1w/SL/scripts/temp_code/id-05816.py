def analyze_network_topology():
    # Simulated network diagnostic tool with red herrings and complex logic
    node_ids = [101, 102, 103, 104, 105, 106, 107, 108]
    signal_strengths = {101: -42, 102: -56, 103: -38, 104: -71, 105: -45, 106: -89, 107: -33, 108: -67}
    transmission_modes = {101: 'UDP', 102: 'TCP', 103: 'UDP', 104: 'ICMP', 105: 'TCP', 106: 'UDP', 107: 'TCP', 108: 'ICMP'}
    
    # Irrelevant configuration (distractor)
    config_threshold = 40
    debug_mode = True
    max_retries = 3
    retry_delay_ms = 250
    encryption_enabled = False
    buffer_size_kb = 128

    # Decoy data structures (set operations used here)
    deprecated_nodes = {104, 106, 108}
    maintenance_nodes = {102, 105}
    critical_nodes = {101, 103, 107}
    active_nodes = set(node_ids) - deprecated_nodes

    # Misleading intermediate calculations
    avg_signal = sum(signal_strengths.values()) / len(signal_strengths)
    weak_signal_nodes = [nid for nid, strength in signal_strengths.items() if strength < -60]
    udp_over_tcp_ratio = len([m for m in transmission_modes.values() if m == 'UDP']) / len(transmission_modes)

    # Simulated packet loss (dead code path - never accessed)
    def calculate_packet_loss(base_rate, humidity):
        if humidity > 70:
            return base_rate * 1.5
        return base_rate
    
    # Unused recursive function (decoy)
    def trace_route_recursive(node, depth=0):
        if depth >= 3 or node == 101:
            return [node]
        return [node] + trace_route_recursive(node - 1, depth + 1)

    # Real processing begins here
    verified_nodes = []
    for node in node_ids:
        if node in deprecated_nodes:
            continue
        if signal_strengths[node] >= -70 and transmission_modes[node] == 'TCP':
            verified_nodes.append(node)
    
    # Secondary filter based on mode (irrelevant to final result but looks important)
    filtered_by_mode = [n for n in node_ids if transmission_modes[n] in ['UDP', 'TCP']]

    # Anomaly detection with misleading thresholds
    anomaly_count = 0
    for node in node_ids:
        if signal_strengths[node] < -85:
            anomaly_count += 1
    
    # Dead conditional block (never executes due to data)
    if 'XYZ' in transmission_modes.values():
        anomaly_count *= 2

    # Key computation variables
    base_coverage = len(active_nodes)
    mode_penalty = 0
    if 'ICMP' in [transmission_modes[n] for n in active_nodes]:
        mode_penalty = 5

    # Red herring statistical calculation
    variance = sum((v - avg_signal) ** 2 for v in signal_strengths.values()) / len(signal_strengths)
    normalized_variance = variance / 100

    # Core algorithmic chain
    if len(verified_nodes) > 2:
        correction_factor = 7
    else:
        correction_factor = 3

    anomaly_offset = anomaly_count * -12

    # Sorting irrelevant list (looks meaningful)
    sorted_signals = sorted(signal_strengths.items(), key=lambda x: x[1], reverse=True)
    top_nodes = [nid for nid, val in sorted_signals[:3]]

    # Final score calculation — this is the critical execution point
    filtration_score = len(verified_nodes) * correction_factor + anomaly_offset

    # Unused transformation pipeline
    def transform_scores(scores):
        return [s * 1.1 for s in scores if s > -60]
    
    enhanced_signals = transform_scores(list(signal_strengths.values()))

    # Output the target result
    print(f"Result: {filtration_score}")

analyze_network_topology()