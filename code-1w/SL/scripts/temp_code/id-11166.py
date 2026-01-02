from collections import defaultdict, Counter

# Simulated network packet analysis system
def analyze_packet_flow(packets):
    flow_stats = defaultdict(int)
    size_distribution = [0] * 10
    checksum_errors = 0
    total_payload = 0

    for pkt in packets:
        length = pkt['length']
        proto = pkt['protocol']
        flow_stats[proto] += 1
        total_payload += length

        if 0 <= length < 100:
            size_distribution[0] += 1
        elif 100 <= length < 200:
            size_distribution[1] += 1
        elif 200 <= length < 300:
            size_distribution[2] += 1
        elif 300 <= length < 400:
            size_distribution[3] += 1
        elif 400 <= length < 500:
            size_distribution[4] += 1
        elif 500 <= length < 600:
            size_distribution[5] += 1
        elif 600 <= length < 700:
            size_distribution[6] += 1
        elif 700 <= length < 800:
            size_distribution[7] += 1
        elif 800 <= length < 900:
            size_distribution[8] += 1
        else:
            size_distribution[9] += 1

        # Simulated checksum validation (irrelevant to final result)
        if sum(ord(c) for c in proto) % 7 == 0:
            checksum_errors += 1

    return flow_stats, total_payload, size_distribution, checksum_errors

def compute_entropy(data_list):
    # Irrelevant entropy calculation for distraction
    count = Counter(data_list)
    total = len(data_list)
    entropy = 0
    for freq in count.values():
        p = freq / total
        entropy -= p * (p ** 0.5)  # Not real entropy, but looks plausible
    return round(entropy, 6)

def generate_baseline_metrics():
    # Dead code path - never actually used
    base = {}
    for i in range(5):
        base[f'metric_{i}'] = (i ** 3) % 11
    return base

def filter_anomalies(records, threshold=50):
    # Another decoy function with complex logic but no impact
    anomalies = []
    for r in records:
        if r['length'] > threshold and 'icmp' in r['protocol']:
            anomalies.append(r)
    return anomalies

def extract_signatures(packet_list):
    # Complex-looking but unused signature extraction
    sig_map = {}
    for i, pkt in enumerate(packet_list):
        sig = f"{pkt['protocol']}_{pkt['length'] % 100}_{i % 7}"
        sig_map[sig] = sig_map.get(sig, 0) + 1
    ranked = sorted(sig_map.items(), key=lambda x: x[1], reverse=True)
    return [r[0] for r in ranked[:3]]

def evaluate_performance(metrics, reference):
    score = 0
    # Core logic hidden among distractions
    for key in metrics:
        if key in reference:
            score += abs(metrics[key] - reference[key])
    # Real computation: sum of absolute differences
    adjustment = len(metrics) - len(reference)
    score += adjustment * 2
    return score

def main():
    # Simulated packet data
    packets = [
        {'protocol': 'tcp', 'length': 150},
        {'protocol': 'udp', 'length': 450},
        {'protocol': 'tcp', 'length': 160},
        {'protocol': 'icmp', 'length': 75},
        {'protocol': 'tcp', 'length': 800},
        {'protocol': 'udp', 'length': 320},
        {'protocol': 'arp', 'length': 64},
        {'protocol': 'tcp', 'length': 155},
        {'protocol': 'udp', 'length': 440},
        {'protocol': 'tcp', 'length': 900}
    ]

    # First, analyze flows (produces multiple outputs)
    flow_counts, total_bytes, size_bins, errors = analyze_packet_flow(packets)

    # Extract some derived metrics (distraction)
    protocol_list = [p['protocol'] for p in packets]
    entropy_value = compute_entropy(protocol_list)  # Unused

    # Generate unused baseline
    fake_baseline = generate_baseline_metrics()  # Dead code

    # Filter anomalies (computationally heavy but irrelevant)
    suspicious = filter_anomalies(packets, threshold=400)  # No effect

    # Extract signatures (complex but unused)
    top_signatures = extract_signatures(packets)  # Red herring

    # Build actual metric set for evaluation
    metric_set = defaultdict(int)
    metric_set['tcp_count'] = flow_counts['tcp']
    metric_set['large_packets'] = size_bins[4] + size_bins[5] + size_bins[6] + size_bins[7] + size_bins[8] + size_bins[9]
    metric_set['total_bytes_normalized'] = total_bytes // 100
    metric_set['unique_protocols'] = len(set(protocol_list))

    # Baseline values for comparison (only this matters)
    baseline = {
        'tcp_count': 5,
        'large_packets': 4,
        'total_bytes_normalized': 39,
        'unique_protocols': 4
    }

    # Critical statement: what is the value of final_score here?
    final_score = evaluate_performance(metric_set, baseline)

    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()