from collections import defaultdict, Counter
import itertools

# Simulated network traffic analysis with decoy metrics
def analyze_traffic_patterns(logs):
    flow_counts = defaultdict(int)
    packet_sizes = []
    priority_flags = 0

    for log in logs:
        src, dst, size, proto = log
        flow_counts[(src, dst)] += 1
        packet_sizes.append(size)

        if proto == 'TCP' and size > 1000:
            priority_flags += 1

    avg_size = sum(packet_sizes) / len(packet_sizes) if packet_sizes else 0
    large_flows = {k: v for k, v in flow_counts.items() if v > 2}
    return avg_size, large_flows, priority_flags

# Irrelevant helper – looks important but unused in final calculation
def compute_entropy(data):
    freqs = Counter(data)
    total = len(data)
    entropy = 0
    for count in freqs.values():
        p = count / total
        entropy -= p * (p ** 0.5)  # Not actual entropy, misleading
    return entropy if total else 0

# Decoy transformation – never called
def transform_payload(payload):
    transformed = []
    for p in payload:
        if p % 3 == 0:
            transformed.append(p // 3)
        elif p % 5 == 0:
            transformed.append(p * 2)
    return transformed

# Core metric processor with red herrings
def process_metrics(data, config):
    baseline = config.get('base', 100)
    multiplier = config.get('mult', 1.0)
    threshold = config.get('thresh', 500)
    debug_mode = config.get('debug', False)

    # Real computation starts
    sizes = [entry[2] for entry in data]
    protocols = [entry[3] for entry in data]

    # Distractor: complex but unused structure
    protocol_stats = {}
    for proto in set(protocols):
        count = protocols.count(proto)
        protocol_stats[proto] = {"count": count, "ratio": count / len(protocols)}

    # Real logic: find flows above threshold and apply weight
    total_volume = sum(sizes)
    high_vol_count = sum(1 for s in sizes if s > threshold)

    # Misleading intermediate that looks critical
    anomaly_score = 0
    for i, size in enumerate(sizes):
        if size > threshold * 1.2:
            anomaly_score += (size - threshold) * 0.1

    # Key branching logic with nested conditions
    if high_vol_count > 3:
        if total_volume > 1500:
            baseline += 40
        else:
            baseline += 10
    elif total_volume > 2000:
        baseline += 25
    else:
        baseline -= 5

    # Apply multiplier only if certain protocol diversity
    unique_protos = len(set(protocols))
    if unique_protos >= 3:
        multiplier *= 1.4
    elif unique_protos == 2:
        multiplier *= 0.9
    else:
        multiplier *= 0.7  # Penalize low diversity

    # Final score computed here — this is the answer point
    final_score = int((baseline + high_vol_count * 3) * multiplier)

    # Dead code path — looks like it modifies final_score but doesn't execute
    if debug_mode and final_score < 0:
        final_score = abs(final_score) * 2

    return final_score

# Generate synthetic traffic data
ips = ['192.168.1.1', '192.168.1.2', '10.0.0.5', '172.16.0.8']
sources = ips[:3]
dests = ips[1:]

traffic_data = []
for src, dst in itertools.product(sources, dests):
    size = hash(src + dst) % 1200 + 300  # Deterministic size
    proto = 'TCP' if (hash(src) + hash(dst)) % 3 != 0 else 'UDP'
    if src == '10.0.0.5' and dst == '172.16.0.8':
        size = 1100  # Force one large packet
    traffic_data.append((src, dst, size, proto))

# Add some repeated flows to trigger threshold logic
traffic_data.append(('192.168.1.1', '192.168.1.2', 950, 'TCP'))
traffic_data.append(('192.168.1.1', '192.168.1.2', 980, 'TCP'))
traffic_data.append(('192.168.1.1', '192.168.1.2', 1020, 'TCP'))

# Weights configuration – key input
weights = {
    'base': 110,
    'mult': 1.25,
    'thresh': 900,
    'debug': False
}

# Call main processing function
temp_result = analyze_traffic_patterns(traffic_data)
entropy_probe = compute_entropy([len(str(d)) for d in traffic_data])

# Critical execution point
final_score = process_metrics(traffic_data, weights)

print(f"Result: {final_score}")