from collections import defaultdict, Counter
import math

# Simulate a distributed network node monitoring system
node_logs = [
    {'id': 'A', 'status': 'active', 'pings': [1, 1, 0, 1], 'latency_ms': [45, 67, 0, 52]},
    {'id': 'B', 'status': 'inactive', 'pings': [0, 0, 0], 'latency_ms': [0, 0, 0]},
    {'id': 'C', 'status': 'active', 'pings': [1, 1, 1, 1], 'latency_ms': [34, 41, 38, 40]},
    {'id': 'D', 'status': 'active', 'pings': [1, 0, 1], 'latency_ms': [55, 0, 50]},
    {'id': 'E', 'status': 'active', 'pings': [1, 1, 1], 'latency_ms': [29, 33, 31]}
]

# Irrelevant statistical artifact (distractor)
def compute_entropy(values):
    counts = Counter(values)
    total = len(values)
    return -sum((count / total) * math.log2(count / total) for count in counts.values())

# Misleading health check with dead logic path
def assess_node_health(ping_list, response_times):
    if sum(ping_list) == 0:
        return 0.0
    availability = sum(ping_list) / len(ping_list)
    avg_response = sum(t for t in response_times if t > 0) / len([t for t in response_times if t > 0])
    if avg_response < 35:
        performance_bonus = 1.1
    else:
        performance_bonus = 1.0
    # Dead code branch — never reached due to logic structure (red herring)
    if availability == 1.0 and False:
        performance_bonus *= 1.25
    return availability * performance_bonus

# Decoy function that calculates but is unused
def calculate_jitter(timestamps):
    if len(timestamps) < 2:
        return 0
    differences = [abs(timestamps[i] - timestamps[i+1]) for i in range(len(timestamps)-1)]
    return max(differences) - min(differences)

# Auxiliary irrelevant transformation
def shift_cipher(text, shift=3):
    return ''.join(chr((ord(c) - 97 + shift) % 26 + 97) if c.islower() else c for c in text)

# Core data aggregation with meaningful computation buried in noise
def extract_metrics(nodes):
    metrics = defaultdict(dict)
    total_pings = 0
    total_active_nodes = 0
    cumulative_latency = 0

    for node in nodes:
        node_id = node['id']
        status = node['status']
        pings = node['pings']
        latencies = node['latency_ms']

        # Real metric collection
        successful_pings = sum(pings)
        total_pings += len(pings)
        if status == 'active':
            total_active_nodes += 1
            if successful_pings > 0:
                avg_latency = sum(latencies) / successful_pings
                cumulative_latency += avg_latency

        # Store intermediate values including decoys
        metrics[node_id]['base_score'] = successful_pings * 10
        metrics[node_id]['raw_stability'] = compute_entropy(pings + [1, 0]) if len(set(pings)) > 1 else 0.0
        metrics[node_id]['cipher_tag'] = shift_cipher(node_id.lower(), 13)  # Irrelevant encoding

    # Real derived values
    overall_success_rate = total_pings and (sum(sum(n['pings']) for n in nodes) / total_pings)
    average_network_latency = total_active_nodes and (cumulative_latency / total_active_nodes)

    # Fake normalization factor (unused)
    normalization_constant = math.log(1 + len(nodes)) or 1

    return metrics, overall_success_rate, average_network_latency

# Complex transformation with multiple layers
def evaluate_resilience(metrics_dict, base_rate, avg_lat):
    resilience_score = 0
    bonus_tracker = defaultdict(int)
    penalty_factor = 0

    for node_id, attrs in metrics_dict.items():
        score = attrs['base_score']
        stability = attrs['raw_stability']

        # Real scoring logic
        resilience_score += score * (1 + stability * 0.05)

        # Red herring: tracking unused bonuses
        if 'cipher_tag' in attrs and attrs['cipher_tag'].startswith('n'):
            bonus_tracker[node_id] += 5

        # Actual penalty application
        if score < 30:
            penalty_factor += 0.05

    # Apply real adjustment
    final_resilience = resilience_score * (1 - penalty_factor)

    # Artificial complexity: bitwise masking on ID characters (irrelevant)
    masked_influence = 0
    for char in str(base_rate)[:3]:
        if char.isdigit():
            masked_influence ^= int(char) << 2

    # Final integration with primary signal
    adjusted_score = final_resilience + (avg_lat * 100 if avg_lat else 0)
    return adjusted_score

# Aggregation function containing the critical execution point
def aggregate_performance(nodes):
    parsed_metrics, success_rate, net_latency = extract_metrics(nodes)
    detailed_analysis = {}

    # Nested analysis with dummy breakdowns
    for k, v in parsed_metrics.items():
        detailed_analysis[k] = {key: val * 0.9 for key, val in v.items() if isinstance(val, (int, float))}

    # Heavily obscured but correct propagation
    initial_eval = evaluate_resilience(parsed_metrics, success_rate, net_latency)

    # Secondary distortion layer (neutralized)
    temp_offset = sum(len(v) for v in parsed_metrics.values()) * 0.1
    draft_score = initial_eval - temp_offset

    # Final calibration using bit manipulation (some relevant, mostly smoke)
    flag_mask = 0b1010
    calibrator = (flag_mask & int(net_latency)) or 7
n
    final_score = int(draft_score // 2) + calibrator * 10

    # This print must be here — required output format
    print(f"Target result: {final_score}")
    return final_score

# Execution entry point
if __name__ == "__main__":
    network_nodes = node_logs
    final_score = aggregate_performance(network_nodes)
