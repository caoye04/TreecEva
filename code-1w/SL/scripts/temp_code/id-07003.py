import itertools

# System diagnostics simulator with interference

def analyze_node_health(node_data, baseline):
    return sum(abs(a - b) for a, b in zip(node_data, baseline)) < 1.5

def compute_bandwidth_score(config):
    # Irrelevant scoring function (red herring)
    score = 0
    for c in config:
        if c.isdigit():
            score += int(c) * 0.7
    return round(score, 2)

def evaluate_latency_pattern(latency_stream):
    # Unused diagnostic path (dead code path)
    peaks = [latency_stream[i] for i in range(1, len(latency_stream)-1)
             if latency_stream[i] > latency_stream[i-1] and latency_stream[i] > latency_stream[i+1]]
    return len(peaks)

def generate_combinations(elements):
    # Distractor: generates unused combinations
    combs = []
    for r in range(1, 4):
        combs.extend(itertools.combinations(elements, r))
    return combs  # Never used

def validate_checksum(signal):
    # Seemingly important but irrelevant validation
    total = 0
    for i, val in enumerate(signal):
        total += val * (i + 1)
    return total % 17 == 0

def normalize_readings(readings):
    min_val, max_val = min(readings), max(readings)
    if max_val == min_val:
        return [0.5 for _ in readings]
    return [(x - min_val) / (max_val - min_val) for x in readings]

def filter_anomalies(dataset, threshold=0.1):
    avg = sum(dataset) / len(dataset)
    return [x for x in dataset if abs(x - avg) / avg < threshold]

def derive_phase_shift(sequence):
    # Misleading transformation
    shifted = [(sequence[i] + sequence[(i+1)%len(sequence)]) % 8 for i in range(len(sequence))]
    return shifted

def aggregate_metrics(nodes):
    weights = [0.3, 0.5, 0.7, 1.0, 0.4]
    contribution = 0.0
    
    for idx, node in enumerate(nodes):
        # Real computation begins
        raw_metrics = node['telemetry']
        processed = normalize_readings(raw_metrics)
        filtered = filter_anomalies(processed)
        
        # Key intermediate value (not final)
        base_index = sum(filtered) * weights[idx % len(weights)]
        
        # Conditional inclusion based on health check
        healthy = analyze_node_health(node['telemetry'], [0.5]*6)
        if not healthy:
            continue
            
        # Only healthy nodes contribute
        adjustment_factor = 1.0
        if node['mode'] == 'turbo':
            adjustment_factor = 1.25
        elif node['mode'] == 'economy':
            adjustment_factor = 0.85
            
        contribution += base_index * adjustment_factor
    
    # Final nonlinear scaling
    final_score = (contribution ** 2) / (1 + contribution * 0.1)
    return int(final_score * 100) / 100.0

# Simulated network node data (mixed states)
network_nodes = [
    {
        'id': 'N001',
        'telemetry': [0.45, 0.52, 0.49, 0.53, 0.47, 0.51],
        'mode': 'normal',
        'config': 'B7X9m',
        'signal': [3, 1, 4, 1, 5]
    },
    {
        'id': 'N002',
        'telemetry': [0.88, 0.91, 0.85, 0.89, 0.92, 0.87],  # Unhealthy due to high deviation
        'mode': 'turbo',
        'config': 'Z2P8q',
        'signal': [2, 7, 1, 8, 2]
    },
    {
        'id': 'N003',
        'telemetry': [0.48, 0.50, 0.51, 0.49, 0.52, 0.50],
        'mode': 'economy',
        'config': 'T5R3n',
        'signal': [9, 9, 5, 0, 2]
    },
    {
        'id': 'N004',
        'telemetry': [0.10, 0.11, 0.09, 0.12, 0.10, 0.11],  # Healthy but low
        'mode': 'normal',
        'config': 'K8M4p',
        'signal': [3, 4, 2, 7, 4]
    }
]

# Dead code execution (distractor block)
config_strings = [node['config'] for node in network_nodes]
all_chars = ''.join(config_strings)
digit_count = sum(1 for c in all_chars if c.isdigit())
checksum_valid_flags = [validate_checksum(node['signal']) for node in network_nodes]

# Generate unused combinatorial space
element_pool = ['A', 'B', 'C', 'D']
combination_set = generate_combinations(element_pool)

# Latency evaluation never used
latencies = [0.12, 0.15, 0.11, 0.23, 0.14, 0.19, 0.10, 0.13]
peak_count = evaluate_latency_pattern(latencies)

# Real execution path starts here
baseline_reference = [0.5] * 6
active_nodes = [n for n in network_nodes if analyze_node_health(n['telemetry'], baseline_reference)]

# Bandwidth scores calculated but not used (red herring)
bandwidth_diagnostics = [compute_bandwidth_score(n['config']) for n in network_nodes]

# Phase shift derivation - looks important but unused
phase_shifted_signals = [derive_phase_shift(n['signal']) for n in network_nodes]

# Core metric aggregation
final_diagnostic = aggregate_metrics(network_nodes)

# Output result
print(f"Result: {final_diagnostic}")