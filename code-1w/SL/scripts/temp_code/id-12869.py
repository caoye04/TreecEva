import math

def analyze_node_health(node_data, threshold=0.75):
    # Irrelevant helper function (dead code path)
    return sum(node_data) / len(node_data) > threshold

def compute_entropy(data):
    # Distractor: Used in decoy logic
    total = sum(data)
    entropy = 0
    for x in data:
        p = x / total
        if p > 0:
            entropy -= p * math.log(p)
    return round(entropy, 4)

def evaluate_signal_integrity(signal_stream):
    # Unused function – red herring
    window_size = 3
    anomalies = 0
    for i in range(len(signal_stream) - window_size + 1):
        window = signal_stream[i:i+window_size]
        if window[0] > window[1] < window[2]:
            anomalies += 1
    return anomalies

def filter_active_nodes(nodes):
    # Relevant but indirect: filters nodes with active status and even id
    return {k: v for k, v in nodes.items() if v['status'] == 'active' and k % 2 == 0}

def integrate_diagnostic_readings(readings_list):
    # Processes sensor readings using zip and enumerate (actual usage)
    cumulative_index = 0
    for idx, readings in enumerate(readings_list):
        weighted_sum = 0
        for i, val in enumerate(readings):
            weighted_sum += val * (i + 1)
        cumulative_index += weighted_sum * (idx + 1)
    return int(cumulative_index % 97)

def aggregate_metrics(nodes, load_profile):
    # Core function – computes final result through multiple steps
    
    # Step 1: Filter relevant nodes
    active_even_nodes = filter_active_nodes(nodes)
    
    # Step 2: Extract diagnostic arrays
    diagnostics = [node['diagnostics'] for node in active_even_nodes.values()]
    
    # Step 3: Use enumerate and zip to align and weight diagnostic streams
    transposed = list(zip(*diagnostics))  # Transpose to process by time step
    trend_scores = []
    for t, obs in enumerate(transposed):
        sorted_obs = sorted(obs)
        median = sorted_obs[len(sorted_obs)//2]
        # Weight by time index and deviation from mean
        mean = sum(obs) / len(obs)
        deviation_penalty = sum(abs(x - mean) for x in obs)
        score = (median * (t + 1)) - (deviation_penalty / len(obs))
        trend_scores.append(score)
    
    # Step 4: Accumulate trend scores with modular arithmetic
    raw_integral = sum(trend_scores)
    normalized_integral = int(abs(raw_integral)) % 10000
    
    # Step 5: Combine with load profile using set operations (distractor vs real use)
    peak_loads = {i for i, x in enumerate(load_profile) if x > 0.8}
    low_loads = {i for i, x in enumerate(load_profile) if x < 0.3}
    stability_windows = len(peak_loads.intersection({i+1 for i in low_loads}))
    
    # Step 6: Apply combinatorics-based adjustment (real contribution)
    n = len(diagnostics)
    k = len(transposed)
    if n > 1:
        binom_adjust = math.factorial(n) // (math.factorial(k) * math.factorial(n - k)) if k <= n else 1
    else:
        binom_adjust = 1
    
    # Step 7: Final computation
    intermediate = normalized_integral + stability_windows * 100
    final_diagnostic = intermediate - binom_adjust * 17
    
    # Distractor variables (no impact)
    entropy_test = compute_entropy([1, 2, 3, 4])
    anomaly_count = evaluate_signal_integrity([1, 0, 1, 0, 1])
    health_flag = analyze_node_health([0.8, 0.9, 0.7])
    
    return final_diagnostic

# Main execution block
if __name__ == '__main__':
    # Simulated network node data
    network_nodes = {
        0: {'status': 'active', 'diagnostics': [3, 1, 4, 1]},
        1: {'status': 'inactive', 'diagnostics': [5, 9, 2, 6]},
        2: {'status': 'active', 'diagnostics': [5, 3, 5, 8]},
        3: {'status': 'active', 'diagnostics': [9, 7, 9, 3]},
        4: {'status': 'active', 'diagnostics': [2, 3, 4, 2]}
    }
    
    system_load = [0.85, 0.25, 0.92, 0.15, 0.70, 0.88, 0.20]
    
    # Irrelevant pre-processing (distractor)
    node_ids = list(network_nodes.keys())
    status_list = [node['status'] for node in network_nodes.values()]
    zipped_data = list(zip(node_ids, status_list))
    indexed_items = dict(enumerate(zipped_data))
    
    # Key statement
    final_diagnostic = aggregate_metrics(network_nodes, system_load)
    
    # Output result
    print(f"Result: {final_diagnostic}")