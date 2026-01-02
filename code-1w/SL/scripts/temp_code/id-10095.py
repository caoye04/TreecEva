def analyze_network_topology():
    # Simulated network node diagnostics with mixed data processing
    node_ids = [101, 102, 103, 104, 105, 106, 107]
    signal_strengths = {101: 85, 102: 90, 103: 78, 104: 92, 105: 88, 106: 76, 107: 83}
    firewall_status = {101: True, 102: False, 103: True, 104: True, 105: False, 106: True, 107: True}
    packet_loss = [0.5, 1.2, 0.3, 2.1, 0.9, 1.8, 0.4]

    # Irrelevant statistical transform (distractor)
    normalized_loss = [round((x - min(packet_loss)) / (max(packet_loss) - min(packet_loss)), 4) for x in packet_loss]
    avg_normalized = sum(normalized_loss) / len(normalized_loss)

    # Decoy function - never called
    def calculate_entropy(data):
        from math import log2
        total = sum(data)
        probabilities = [x / total for x in data if x > 0]
        return -sum(p * log2(p) for p in probabilities)

    # Identify high-performing nodes based on signal
    high_signal_nodes = {k for k, v in signal_strengths.items() if v > 85}

    # Misleading intermediate calculation (dead-end)
    throughput_estimates = {}
    for nid in node_ids:
        base = signal_strengths[nid]
        penalty = 0.5 if firewall_status[nid] else 1.5
        estimated_tput = (base / 10) ** penalty
        throughput_estimates[nid] = round(estimated_tput, 3)

    # Unused sorting operation (distractor)
    sorted_by_throughput = sorted(throughput_estimates.items(), key=lambda x: x[1], reverse=True)

    # Core logic: find secure and stable nodes
    stability_criteria = [loss < 1.0 for loss in packet_loss]
    stable_nodes = set()
    for i, is_stable in enumerate(stability_criteria):
        if is_stable:
            stable_nodes.add(node_ids[i])

    secure_nodes = {k for k, v in firewall_status.items() if v}

    # Cross-reference to find nodes that are both secure and stable
    robust_nodes = secure_nodes.intersection(stable_nodes)

    # Secondary filter: must have above-average signal
    avg_signal = sum(signal_strengths.values()) / len(signal_strengths)
    final_robust_set = {nid for nid in robust_nodes if signal_strengths[nid] > avg_signal}

    # Red herring: complex but unused bit manipulation
    bitmask = 0
    for nid in node_ids:
        bitmask ^= nid << 1
    derived_key = bitmask & 0xFFFF

    # Decoy list comprehension with side-effect-free mutation
    diagnostic_flags = ['ERR' if signal_strengths[nid] < 80 else 'OK' for nid in node_ids]
    flag_summary = ''.join(diagnostic_flags[:3])  # Unused

    # Actual critical computation chain
    base_score = 0
    for nid in final_robust_set:
        base_score += signal_strengths[nid]

    adjustment_factor = len(secure_nodes) - len(high_signal_nodes)
    aggregate_score = base_score * (1 + adjustment_factor * 0.1)

    # Key statement
    final_diagnostic = aggregate_score + len(secure_nodes)

    print(f"Result: {final_diagnostic}")

analyze_network_topology()