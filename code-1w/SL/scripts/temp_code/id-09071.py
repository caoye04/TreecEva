import math

# Simulated sensor network diagnostics with data filtering and transformation

def collect_readings(raw_data, threshold=3.5):
    filtered = [x for x in raw_data if abs(x) > threshold]
    return filtered[::2] if len(filtered) > 4 else filtered[::-1]


def amplify_signal(signal_list, factor=2.1):
    amplified = []
    for val in signal_list:
        if val > 0:
            amplified.append(val ** factor)
        else:
            amplified.append(-((-val) ** 1.9))
    return amplified


def align_phase(readings):
    adjusted = []
    for i, r in enumerate(readings):
        phase_shift = math.sin(i * math.pi / 4)
        adjusted.append(r + phase_shift * 0.75)
    return adjusted


def compute_entropy(data):
    # Irrelevant function - decoy for information theory analysis
    total = sum(abs(x) for x in data)
    if total == 0:
        return 0
    probabilities = [abs(x) / total for x in data]
    return -sum(p * math.log2(p) for p in probabilities if p > 0)


def validate_integrity(nodes):
    # Dead code path - never actually used in final computation
    checksum = 0
    for idx, node in enumerate(nodes):
        if isinstance(node, dict) and 'status' in node:
            checksum ^= len(node['status']) + idx
    return checksum == 15


def extract_metrics(node_array):
    metrics = []
    for node in node_array:
        if 'diagnostics' in node:
            raw = node['diagnostics']
            cleaned = collect_readings(raw)
            enhanced = amplify_signal(cleaned)
            aligned = align_phase(enhanced)
            summary = sum(math.cos(x) for x in aligned[:len(aligned)//2 + 1])
            metrics.append(round(summary, 4))
    return metrics


def transform_coordinates(x, y):
    # Distractor function: looks important but unused
    radius = math.sqrt(x*x + y*y)
    angle = math.atan2(y, x)
    return radius * math.cos(2*angle), radius * math.sin(2*angle)


def aggregate_measurements(node_list):
    results = extract_metrics(node_list)
    
    # Apply moving average filter (slicing and list comprehension)
    smoothed = [sum(results[i:i+3]) / 3 for i in range(len(results) - 2)] if len(results) >= 3 else results
    
    # Secondary transformation
    processed = []
    for val in smoothed:
        if val != 0:
            processed.append(math.log(abs(val)) * 100)
        else:
            processed.append(0)
    
    # Final integration step
    accumulator = 0
    for i, p in enumerate(processed):
        weight = math.cos(i * math.pi / 6)
        accumulator += p * weight
    
    # Key result
    final_diagnostic = int(round(accumulator))
    
    # Red herring computations below
    outlier_count = sum(1 for r in results if abs(r) > 5)
    baseline = sum(results) / len(results) if results else 0
    deviation_score = sum((x - baseline)**2 for x in results) if results else 0
    
    # Unused nested structure
    audit_trail = {
        'version': '2.1',
        'nodes_processed': len(node_list),
        'outliers': outlier_count,
        'final_raw': accumulator,
        'timestamp': 1719865234,
        'signature': hex(hash(tuple(results)))[:10]
    }
    
    # This print is irrelevant to the actual answer
    # print(f"Validation: {validate_integrity(node_list)}")
    
    return final_diagnostic

# Simulated network node data (real input)
network_nodes = [
    {'id': 'N001', 'status': 'active', 'diagnostics': [-6.2, 4.8, -7.1, 3.9, 8.3, -5.4, 2.1]},
    {'id': 'N002', 'status': 'standby', 'diagnostics': [4.5, -6.7, 5.2, -8.9, -3.4, 7.6]},
    {'id': 'N003', 'status': 'active', 'diagnostics': [-5.5, 6.3, -4.9, 7.7, -6.8, 5.1, 8.2]},
    {'id': 'N004', 'status': 'active', 'diagnostics': [3.7, -4.2, 5.8, -6.1, 4.9, -5.7]},
    {'id': 'N005', 'status': 'error', 'diagnostics': [-7.3, 8.1, -6.5, 7.9, -8.7, 6.4]}
]

# Trigger the main computation
final_diagnostic = aggregate_measurements(network_nodes)

# Output the target result
print(f"Target result: {final_diagnostic}")