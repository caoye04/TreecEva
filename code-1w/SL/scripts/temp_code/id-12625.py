def preprocess_signals(raw_logs):
    # Irrelevant signal processing (distractor)
    filtered = []
    for log in raw_logs:
        if 'error' not in log and len(log) > 5:
            filtered.append(log.upper())
    return [f[::-1] for f in filtered]

# Unused decoy function
def compute_entropy(data):
    import math
    freq = {}
    for d in data:
        freq[d] = freq.get(d, 0) + 1
    entropy = 0
    total = len(data)
    for count in freq.values():
        p = count / total
        entropy -= p * math.log2(p)
    return entropy

# Real computation: agricultural yield simulation with noise

def generate_threshold_map(base_level):
    # Generates a nested map of tolerance thresholds (red herring)
    keys = ['A', 'B', 'C', 'D']
    subkeys = range(3)
    t_map = {k: {sk: (base_level + sk * 0.1) ** (i+1) for sk in subkeys} for i, k in enumerate(keys)}
    t_map['override'] = False
    return t_map


def evaluate_cluster_stability(cluster, config):
    score = 0
    for i, val in enumerate(cluster):
        if i % 2 == 0:
            score += val * 0.7
        else:
            score -= val * 0.3
    # Dead code path (never used)
    if config.get('strict_mode'):
        score = max(score, 0.5)
    return abs(score)

# Core logic buried in distractions
def calculate_harvest_efficiency(clusters, limits):
    results = []
    temp_cache = []
    
    # Real but obscured calculation
    for idx, cluster in enumerate(clusters):
        base = sum(x for x in cluster if x > 0)  # Only positive values matter
        offset = len([x for x in cluster if x < -5])  # Count deeply negative
        adjusted = base - offset * 2
        
        # Actual key transformation
        if idx in [0, 2]:
            adjusted *= 1.1
        elif idx == 1:
            adjusted *= 0.95
        
        # Distracting normalization
        norm_factor = max(cluster) - min(cluster) if max(cluster) != min(cluster) else 1
        normalized = adjusted / norm_factor
        temp_cache.append(normalized)
    
    # Final aggregation
    aggregate = sum(temp_cache)
    penalty = 0
    for k, v in limits.items():
        if isinstance(v, dict) and 'override' not in k:
            penalty += v[0] * 0.05  # Only uses first item of each subdict
    
    final = aggregate - penalty * 10
    return int(final)

# --- Setup Data ---
raw_monitoring_logs = [
    "sensor_7_ok", "node_reset", "flow_normal", 
    "backup_active", "sync_pending"
]

# Unused complex structure
signal_traces = preprocess_signals(raw_monitoring_logs)
entropy_profile = [compute_entropy(s) for s in signal_traces]  # Computed but unused

# Relevant input structures
cluster_data = [
    [4, -1, 6, 3],       # Cluster A
    [5, 5, -2, 8],       # Cluster B
    [-3, 7, 9, -1]       # Cluster C
]

threshold_map = generate_threshold_map(0.85)

# Simulate stability checks (irrelevant to final result)
stability_scores = [
    evaluate_cluster_stability(c, {'mode': 'relaxed'}) for c in cluster_data
]

# Key execution point
final_yield = calculate_harvest_efficiency(cluster_data, threshold_map)

# Output the required result
print(f"Result: {final_yield}")