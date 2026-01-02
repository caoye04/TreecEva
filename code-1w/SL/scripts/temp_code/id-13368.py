import math

# System diagnostics simulation with heavy distractions
def analyze_node_health(node_data, threshold=0.75):
    if not node_data:
        return False
    avg_load = sum(node_data) / len(node_data)
    peak_spike = max(node_data) - avg_load
    stability_score = avg_load / (peak_spike + 1e-5)
    return stability_score > threshold

# Irrelevant helper - distractor function
def calculate_entropy(s: str) -> float:
    from collections import Counter
    counts = Counter(s)
    total = len(s)
    entropy = 0.0
    for k in counts:
        p = counts[k] / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

def encode_routing_key(index, mode='hex'):
    base = f"NODE_{index % 127}_CHK"
    if mode == 'hex':
        return base + hex(index * 31)[2:]
    return base.lower().replace('_', '-')

# Unused recursive path - dead code path
def trace_route_recursive(path, depth=0):
    if depth > 5 or not path:
        return 0
    return path[0] ** 2 + trace_route_recursive(path[1:], depth + 1)

# Core data processing with mixed operations
def extract_signal_features(raw_samples):
    filtered = [x for x in raw_samples if abs(x - 512) < 256]
    normalized = [(x - 256) / 255 for x in filtered]
    power_levels = [abs(math.sin(x)) * 1.5 for x in normalized]
    return {
        'count': len(power_levels),
        'average_power': sum(power_levels) / len(power_levels) if power_levels else 0,
        'peak': max(power_levels) if power_levels else 0
    }

# Distractor: complex string processing with no impact on final result
def generate_diagnostics_report(nodes):
    report_lines = []
    for idx, nd in enumerate(nodes):
        key = encode_routing_key(idx)
        health_flag = 'STABLE' if analyze_node_health(nd.get('load_history', [])) else 'UNSTABLE'
        summary = f"[{key}] Node {idx}: {health_flag}"
        if 'temp_log' in nd:
            last_temp = nd['temp_log'][-1] if nd['temp_log'] else 0
            status_word = 'OVERHEAT' if last_temp > 85 else 'NORMAL'
            # Use of string method - required feature
            summary += " | Temp: " + status_word.lower().capitalize()
        summary = summary.ljust(60, '.')
        entropy_val = calculate_entropy(summary.replace('.', ''))
        summary += f" [ENT:{entropy_val:.2f}]"
        report_lines.append(summary)
    return '\n'.join(report_lines)

# Real computation buried in noise
def compute_resilience_index(config_matrix):
    resilience = 0
    for row in config_matrix:
        for val in row:
            resilience ^= (val * 17) & 255  # Bit manipulation
    return resilience + 100

# Key function - but obscured by context
def aggregate_metrics(nodes, load_profile):
    # Extract relevant signal data
    all_samples = []
    for node in nodes:
        if 'signal_trace' in node and isinstance(node['signal_trace'], list):
            all_samples.extend(node['signal_trace'])
    
    features = extract_signal_features(all_samples)
    
    # Irrelevant aggregation
    total_nodes = len(nodes)
    degraded_count = 0
    for n in nodes:
        hist = n.get('load_history', [])
        if hist and sum(h > 0.9 for h in hist) > 2:
            degraded_count += 1
    degradation_rate = degraded_count / total_nodes if total_nodes else 0

    # Fake resilience calculation (unused)
    fake_matrix = [[i*j % 13 for j in range(8)] for i in range(total_nodes)]
    fake_resilience = compute_resilience_index(fake_matrix)

    # Actual critical computation
    raw_metric = features['average_power'] * 1000
    adjustment_factor = 1.0
    if features['peak'] > 1.2:
        adjustment_factor *= 0.8
    if degradation_rate > 0.5:
        adjustment_factor *= 0.9
    
    # The real answer derivation (non-obvious)
    temp_buffer = [math.floor(features['average_power'] * 100)] * 3
    temp_buffer[1] = int(load_profile * 10) % 7
    checksum = sum((i+1)*v for i, v in enumerate(temp_buffer))  # Linear weighting
    final_diagnostic = int(raw_metric + checksum * 10)

    # Dead code - misleading continuation
    if final_diagnostic > 2000:
        fallback = 0
        for x in temp_buffer:
            fallback = (fallback << 1) ^ x
        final_diagnostic = min(final_diagnostic, fallback + 500)
    
    return final_diagnostic

# Simulation data with red herrings
network_nodes = [
    {
        'id': 'A101',
        'load_history': [0.8, 0.85, 0.92, 0.76, 0.88],
        'temp_log': [78, 82, 86, 88, 84],
        'signal_trace': [512, 600, 400, 700, 550, 480]
    },
    {
        'id': 'B202',
        'load_history': [0.6, 0.65, 0.7, 0.75, 0.8],
        'temp_log': [75, 77, 79, 80, 81],
        'signal_trace': [520, 490, 530, 480]
    },
    {
        'id': 'C303',
        'load_history': [0.95, 0.96, 0.97, 0.98, 0.99],
        'temp_log': [85, 87, 90, 92, 95],
        'signal_trace': [600, 650, 700, 500, 400, 300, 350]
    },
    {
        'id': 'D404',
        'load_history': [0.5, 0.55, 0.6, 0.62, 0.58],
        'signal_trace': [510, 515, 505]
    }
]

system_load = 0.73

# Execution point of interest
final_diagnostic = aggregate_metrics(network_nodes, system_load)

# Print required output
print(f"Target result: {final_diagnostic}")