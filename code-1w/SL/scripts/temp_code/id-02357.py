from collections import defaultdict, Counter
import math

def analyze_node_load(node_data):
    # Irrelevant analysis function (dead code path)
    load_summary = defaultdict(int)
    for node, stats in node_data.items():
        if stats['load'] > 75:
            load_summary['overloaded'] += 1
        elif stats['load'] < 25:
            load_summary['underused'] += 1
    return load_summary

def validate_checksum(data_stream):
    # Distractor: checksum validation not used in main logic
    checksum = 0
    for byte in data_stream:
        checksum ^= byte
    return checksum == 0xFF

def compute_entropy(values):
    # Red herring function: computes entropy but not used in final result
    freq = Counter(values)
    total = len(values)
    entropy = 0.0
    for count in freq.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 4)

def extract_signals(raw_input, threshold=0.65):
    # Signal extraction with irrelevant transformations
    filtered = [x for x in raw_input if abs(x) >= threshold]
    normalized = [(x + 1) / 2 for x in filtered]
    categorized = {'strong': 0, 'weak': 0}
    for val in normalized:
        if val > 0.8:
            categorized['strong'] += 1
        else:
            categorized['weak'] += 1
    return categorized

def aggregate_performance(state, metrics):
    # Core logic buried in distractions
    base_weight = 0.7
    bonus_factor = 1.25
    penalty_rate = 0.03

    # Real computation starts here
    active_nodes = 0
    total_latency = 0.0
    for node_id, props in state.items():
        if props.get('active', False):
            active_nodes += 1
            total_latency += props['response_time']

    avg_latency = total_latency / active_nodes if active_nodes else 0

    # Metrics processing
    throughput_score = metrics['throughput'] * 0.01
    error_ratio = metrics['errors'] / metrics['attempts'] if metrics['attempts'] > 0 else 0

    # Real answer calculation (well-hidden among distractors)
    raw_performance = (throughput_score - error_ratio * 100) * base_weight
    if avg_latency < 15:
        raw_performance *= bonus_factor
    elif avg_latency > 50:
        raw_performance -= penalty_rate * 100

    # Final transformation using set operations (required feature)
    critical_flags = set(metrics['flags'])
    known_warnings = {'timeout', 'retry', 'throttle'}
    warning_count = len(critical_flags & known_warnings)
    final_score = int(raw_performance - warning_count * 2.5)

    # Additional noise
    debug_snapshot = {k: v for k, v in enumerate(zip([1,2,3], ['a','b','c']))}
    temp_result = sum(math.sin(i) for i in range(1,6))

    return final_score

# Simulated input data with many decoy fields
network_state = {
    'node_01': {'active': True, 'response_time': 12, 'load': 80},
    'node_02': {'active': True, 'response_time': 18, 'load': 45},
    'node_03': {'active': False, 'response_time': 25, 'load': 10},  # inactive
    'node_04': {'active': True, 'response_time': 10, 'load': 90},
    'node_05': {'active': True, 'response_time': 22, 'load': 60},
}

efficiency_metrics = {
    'throughput': 876,
    'errors': 12,
    'attempts': 95,
    'flags': ['retry', 'compression'],  # one matching warning
    'checksum': [0xAA, 0x12, 0xBC, 0xFF],
    'timestamp': 1712345678
}

# Unused variables (distractors)
data_stream = [0x1A, 0x2B, 0x3C, 0x4D, 0x5E]
raw_sensor_data = [-0.7, 0.85, 0.92, -0.1, 0.68]
redundant_summary = extract_signals(raw_sensor_data)
entropy_value = compute_entropy([1,2,2,3,3,3,4,4,4,4])

# Key execution point
final_score = aggregate_performance(network_state, efficiency_metrics)

# Print result as required
print(f"Target result: {final_score}")