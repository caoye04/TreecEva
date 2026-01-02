def analyze_throughput(bandwidth, latency):
    if bandwidth <= 0:
        return 0
    throughput = (bandwidth * 1000) / (latency + 1)
    adjustment_factor = 0.85 if throughput > 5000 else 0.6
    return throughput * adjustment_factor


def validate_node_security(node_id, firewall_active, encryption_level):
    security_score = 0
    if firewall_active:
        security_score += 30
    if encryption_level >= 2:
        security_score += 50
    if node_id % 3 == 0 and encryption_level < 1:
        security_score -= 20
    return security_score >= 60


def compute_stability_index(temperature, vibration, threshold=75):
    base_stability = 100 - temperature
    if vibration > 10:
        base_stability -= vibration * 1.5
    elif vibration > 5:
        base_stability -= vibration
    return max(base_stability, 0) >= threshold


def evaluate_packet_loss(packet_count, lost_count):
    if packet_count == 0:
        return 100.0
    loss_rate = (lost_count / packet_count) * 100
    return round(loss_rate, 4)


def aggregate_metrics(nodes, load):
    total_weighted_score = 0
    active_count = 0
    critical_nodes = set()
    auxiliary_data = []

    for idx, node in enumerate(nodes):
        node_id = node.get('id')
        bw = node.get('bandwidth', 0)
        lat = node.get('latency', 0)
        temp = node.get('temp', 30)
        vib = node.get('vibration', 0)
        p_sent = node.get('packets_sent', 0)
        p_lost = node.get('packets_lost', 0)
        fw = node.get('firewall', False)
        enc = node.get('encryption', 0)

        # Irrelevant diagnostic flag (distractor)
        debug_flag = (idx + bw) % 7 == 0

        throughput_score = analyze_throughput(bw, lat)
        security_valid = validate_node_security(node_id, fw, enc)
        stable = compute_stability_index(temp, vib)
        loss_rate = evaluate_packet_loss(p_sent, p_lost)

        # Misleading intermediate metric (unused)
        hypothetical_capacity = bw * 1.5 if lat < 5 else bw * 0.7

        # Only process nodes that meet all criteria
        if security_valid and stable and loss_rate < 15.0:
            weight = 1.0
            if bw >= 100:
                weight *= 1.4
            if lat <= 3:
                weight *= 1.2
            total_weighted_score += throughput_score * weight
            active_count += 1
            if node_id % 5 == 0:
                critical_nodes.add(node_id)
        else:
            # Dead code path - appears meaningful but unused
            fallback_metric = (throughput_score * 0.5) + (bw / 10)
            auxiliary_data.append(fallback_metric)

        # Decoy accumulation (distractor)
        redundant_sum = sum([bw, lat, temp, vib]) * 0.1

    # Additional irrelevant transformation
    if len(critical_nodes) > 0:
        adjusted_critical = {nid * 2 + 1 for nid in critical_nodes}
    else:
        adjusted_critical = set()

    # Real computation path
    if active_count == 0:
        final_raw_score = 0.0
    else:
        avg_weighted = total_weighted_score / active_count
        load_factor = 1.0 if load < 80 else 0.7
        final_raw_score = avg_weighted * load_factor

    # Secondary decoy calculation (never used)
    ghost_score = sum(adjusted_critical) / len(adjusted_critical) if adjusted_critical else 0

    # Key assignment point
    final_diagnostic = int(round(final_raw_score))

    # Red herring: another variable that looks important
    meta_diagnostic = final_diagnostic * 1.05 if ghost_score > 0 else final_diagnostic

    return final_diagnostic

# Simulated network data
network_nodes = [
    {'id': 101, 'bandwidth': 120, 'latency': 2, 'temp': 68, 'vibration': 3, 'packets_sent': 1000, 'packets_lost': 12, 'firewall': True, 'encryption': 2},
    {'id': 102, 'bandwidth': 90, 'latency': 4, 'temp': 76, 'vibration': 12, 'packets_sent': 800, 'packets_lost': 5, 'firewall': True, 'encryption': 3},
    {'id': 105, 'bandwidth': 150, 'latency': 1, 'temp': 65, 'vibration': 2, 'packets_sent': 1200, 'packets_lost': 8, 'firewall': True, 'encryption': 2},
    {'id': 108, 'bandwidth': 80, 'latency': 6, 'temp': 80, 'vibration': 8, 'packets_sent': 600, 'packets_lost': 100, 'firewall': False, 'encryption': 1},
    {'id': 110, 'bandwidth': 200, 'latency': 2, 'temp': 70, 'vibration': 1, 'packets_sent': 1500, 'packets_lost': 10, 'firewall': True, 'encryption': 3}
]
system_load = 72

# Execute main logic
final_diagnostic = aggregate_metrics(network_nodes, system_load)
print(f"Result: {final_diagnostic}")