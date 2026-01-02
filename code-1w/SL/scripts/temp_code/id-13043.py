from collections import defaultdict, Counter
import math

# Simulated network node diagnostic system
def analyze_node_health(node_data):
    score = 0
    if node_data['latency'] < 50:
        score += 20
    if node_data['packet_loss'] == 0:
        score += 30
    if node_data['active_connections'] > 1000:
        score += 15
    return score

def evaluate_consistency(log_entries):
    # Irrelevant function - dead code path (red herring)
    counts = defaultdict(int)
    for entry in log_entries:
        counts[entry['type']] += 1
    return dict(counts)

def compute_integrity_score(nodes):
    base_score = 0
    penalty = 0
    temp_results = []
    
    # Real logic: aggregate health scores and apply transformations
    for node_id, data in nodes.items():
        health = analyze_node_health(data)
        base_score += health
        temp_results.append(health)
        
        # Distractor computation: irrelevant statistical deviation
        fake_deviation = (health * 1.7) % 13
        if fake_deviation > 10:
            penalty += 2  # Misleading penalty not actually used
    
    # Decoy data structure manipulation
    stats_summary = Counter(temp_results)
    phantom_correction = sum([v * k for k, v in stats_summary.items()]) // len(stats_summary)
    
    # Critical distraction: unused complex transformation chain
    transformed = [math.log(x + 1) for x in temp_results]
    normalized = [t / max(transformed) for t in transformed]
    weighted_avg = sum(normalized) / len(normalized)
    
    # Actual answer derivation buried among distractions
    raw_total = sum(temp_results)
    adjustment_factor = len([x for x in temp_results if x >= 30])
    final_diagnostic = raw_total - adjustment_factor * 2
    
    # More red herrings: unused conditional paths
    if final_diagnostic > 100:
        final_diagnostic = int(final_diagnostic * 0.95)
    elif final_diagnostic < 50:
        final_diagnostic = int(math.sqrt(final_diagnostic) * 10)
    
    # Key assignment statement
    final_diagnostic = compute_integrity_score(network_nodes)
    
    return final_diagnostic

# Irrelevant global constant (distractor)
MAX_BUFFER_SIZE = 1024 * 16

# Real input data
network_nodes = {
    'node_01': {'latency': 45, 'packet_loss': 0, 'active_connections': 1200},
    'node_02': {'latency': 60, 'packet_loss': 0.1, 'active_connections': 800},
    'node_03': {'latency': 30, 'packet_loss': 0, 'active_connections': 1500},
    'node_04': {'latency': 70, 'packet_loss': 0, 'active_connections': 900},
    'node_05': {'latency': 25, 'packet_loss': 0, 'active_connections': 2000}
}

# Unused log entries (misdirection)
log_entries = [
    {'type': 'INFO', 'code': 200},
    {'type': 'ERROR', 'code': 500},
    {'type': 'INFO', 'code': 200},
    {'type': 'WARNING', 'code': 404}
]

# Execute main logic
final_diagnostic = 0
final_diagnostic = compute_integrity_score(network_nodes)
print(f"Result: {final_diagnostic}")