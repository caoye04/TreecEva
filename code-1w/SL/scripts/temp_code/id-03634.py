import math

# System diagnostics and network analysis simulation
def analyze_node_health(node_data):
    # Irrelevant helper that looks important
    return sum(v ** 0.5 for v in node_data.values() if v > 0)


def compute_entropy(data_stream):
    # Distractor: looks critical but unused in final result
    freq = {}
    for x in data_stream:
        freq[x] = freq.get(x, 0) + 1
    total = len(data_stream)
    return -sum((count / total) * math.log2(count / total) for count in freq.values())


def detect_anomalies(reading_list):
    # Dead function - not used but plausible
    threshold = sum(reading_list) / len(reading_list)
    return [i for i, val in enumerate(reading_list) if val > 1.5 * threshold]

# Simulated network node statuses
topology_map = {
    'core': ['node_a', 'node_b', 'node_c'],
    'edge': ['node_d', 'node_e'],
    'legacy': ['node_f']
}

# Misleading intermediate metrics
diag_matrix = [
    [1, 3, 2],
    [4, 0, 1],
    [2, 2, 3]
]

# Unused statistical baseline
baseline_scores = {k: len(v) * 10 for k, v in topology_map.items()}

# Real data inputs
network_nodes = {
    'node_a': {'load': 75, 'errors': 2, 'uptime': 996},
    'node_b': {'load': 88, 'errors': 5, 'uptime': 987},
    'node_c': {'load': 62, 'errors': 1, 'uptime': 999},
    'node_d': {'load': 91, 'errors': 8, 'uptime': 970},
    'node_e': {'load': 55, 'errors': 0, 'uptime': 1000},
    'node_f': {'load': 40, 'errors': 12, 'uptime': 800}
}

system_log = [
    'ERR_CRITICAL|node_d|timeout',
    'INFO|node_a|ok',
    'WARN|node_b|high_load',
    'ERR_MINOR|node_f|retry',
    'INFO|node_e|ok'
]

# Decoy transformation
log_summary = {}
for entry in system_log:
    parts = entry.split('|')
    level = parts[0]
    node = parts[1]
    msg = parts[2]
    if level not in log_summary:
        log_summary[level] = 0
    log_summary[level] += 1

# Red herring: complex-looking but unused bitwise shift chain
obfuscated_key = 0
for char in 'diagnostics_2024':
    obfuscated_key ^= ord(char)
obfuscated_key = (obfuscated_key << 3) | (obfuscated_key >> 5)

# Real processing begins here
critical_nodes = []
for node_id, attrs in network_nodes.items():
    if attrs['load'] > 85 or attrs['errors'] >= 5:
        critical_nodes.append(node_id)

# Compute health score using uptime and error rate
health_scores = {}
for node_id, attrs in network_nodes.items():
    error_penalty = attrs['errors'] * 10
    normalized_uptime = attrs['uptime'] / 1000.0
    score = (normalized_uptime * 100) - error_penalty
    if attrs['load'] > 90:
        score -= 15  # Severe penalty
    elif attrs['load'] > 75:
        score -= 5
    health_scores[node_id] = max(score, 0)

# Extract failed nodes from logs
failed_from_log = set()
for entry in system_log:
    if 'ERR' in entry.split('|')[0]:
        failed_from_log.add(entry.split('|')[1])

# Cross-reference with health scores
compromised_score = 0
for node in failed_from_log:
    if node in health_scores:
        compromised_score += int(health_scores[node])

# Simulate dependency chain effect
dependency_multiplier = 1.0
if 'node_d' in failed_from_log and 'core' in topology_map:
    dependency_multiplier = 1.3

# Data structure transformation distraction
temp_pairs = list(health_scores.items())
sorted_pairs = sorted(temp_pairs, key=lambda x: x[1])
median_index = len(sorted_pairs) // 2
median_node_score = sorted_pairs[median_index][1]

# Another decoy: set operations that don't affect outcome
active_nodes = set(network_nodes.keys())
disabled_simulated = {'node_x', 'node_y'}
overlap_check = active_nodes & disabled_simulated  # Always empty

# Real aggregation logic buried among distractions
def aggregate_metrics(nodes, log_entries):
    total_diagnostic = 0
    
    # Step 1: Base contribution from all node uptimes
    for info in nodes.values():
        total_diagnostic += info['uptime'] // 100
    
    # Step 2: Subtract error-weighted penalties
    total_errors = sum(info['errors'] for info in nodes.values())
    total_diagnostic -= total_errors * 3
    
    # Step 3: Add bonus if majority nodes are healthy (<5 errors)
    healthy_count = sum(1 for info in nodes.values() if info['errors'] < 5)
    if healthy_count >= len(nodes) / 2:
        total_diagnostic += 25
    
    # Step 4: Adjust based on log severity pattern
    error_levels = {'ERR_CRITICAL': 5, 'ERR_MINOR': 2, 'WARN': 1}
    log_penalty = 0
    for entry in log_entries:
        level = entry.split('|')[0]
        if level in error_levels:
            log_penalty += error_levels[level]
    total_diagnostic -= log_penalty
    
    # Step 5: Apply dependency multiplier if triggered
    failed_nodes_in_log = {e.split('|')[1] for e in log_entries if 'ERR' in e.split('|')[0]}
    if 'node_d' in failed_nodes_in_log:
        critical_core = any(n in failed_nodes_in_log for n in topology_map['core'])
        if critical_core:
            total_diagnostic = int(total_diagnostic * dependency_multiplier)
    
    # Step 6: Final adjustment via slicing a computed list
    scores_only = list(health_scores.values())
    top_three_avg = sum(scores_only[-3:]) / 3 if len(scores_only) >= 3 else 0
    total_diagnostic += int(top_three_avg // 10)
    
    return total_diagnostic

# Key execution point
final_diagnostic = aggregate_metrics(network_nodes, system_log)

# Output the required result
print(f"Target result: {final_diagnostic}")