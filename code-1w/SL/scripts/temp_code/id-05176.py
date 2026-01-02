from collections import defaultdict, Counter
from itertools import combinations, chain

# Simulated system telemetry data
telemetry_stream = [
    {'node': 'A', 'load': 0.4, 'temp': 32, 'uptime': 120},
    {'node': 'B', 'load': 0.8, 'temp': 45, 'uptime': 95},
    {'node': 'C', 'load': 0.6, 'temp': 38, 'uptime': 110},
    {'node': 'D', 'load': 0.9, 'temp': 52, 'uptime': 80},
    {'node': 'E', 'load': 0.3, 'temp': 29, 'uptime': 130}
]

# Irrelevant auxiliary function (decoy)
def analyze_bandwidth(nodes):
    total = 0
    for node in nodes:
        if node['load'] > 0.7:
            total += node['uptime'] * 0.1
    return round(total, 2)

# Dead code path (never called)
def deprecated_normalization(data):
    return [d * 0.95 for d in sorted(data, reverse=True) if d > 0.2]

# Unused transformation map
transform_map = {
    'low': lambda x: x * 0.8,
    'medium': lambda x: x * 1.0,
    'high': lambda x: x * 1.2
}

# Misleading intermediate calculation (not used in final result)
candidate_ranks = []
for entry in telemetry_stream:
    score = entry['load'] * 100
    if entry['temp'] > 40:
        score -= 10
    candidate_ranks.append(score)

# Dummy aggregation using irrelevant logic
temp_buckets = defaultdict(list)
for t in telemetry_stream:
    bucket = 'high' if t['temp'] > 40 else 'normal'
    temp_buckets[bucket].append(t['load'])

# Unused combinatorial analysis (red herring)
possible_pairs = list(combinations([t['node'] for t in telemetry_stream], 2))
edge_count = len(possible_pairs)

# Real processing begins here
baseline = {'threshold': 0.5, 'weight_temp': 0.1, 'penalty_factor': 2}

# Core metrics extraction (relevant)
metrics = []
for record in telemetry_stream:
    metric = {
        'id': record['node'],
        'efficiency': (1 - record['load']) * record['uptime'],
        'overheat': record['temp'] > 40
    }
    metrics.append(metric)

# Secondary derived features (some relevant, some not)
feature_matrix = []
for m in metrics:
    row = {}
    row['base_eff'] = m['efficiency']
    row['flagged'] = m['overheat']
    row['adj_eff'] = m['efficiency'] * 0.9 if m['overheat'] else m['efficiency']
    feature_matrix.append(row)

# Aggregation with distractor variables
aggregated = 0
max_efficiency = 0
overheated_nodes = 0
for fm in feature_matrix:
    aggregated += fm['adj_eff']
    if fm['adj_eff'] > max_efficiency:
        max_efficiency = fm['adj_eff']
    if fm['flagged']:
        overheated_nodes += 1

# Another decoy variable (misleading intermediate)
avg_load_sim = sum(t['load'] for t in telemetry_stream) / len(telemetry_stream)

# Real evaluation function
prev_results = []  # Unused but declared to distract

def evaluate_performance(perf_metrics, config):
    total = 0.0
    penalty = 0.0
    
    # Primary computation
    for pm in perf_metrics:
        if pm['efficiency'] > config['threshold'] * 100:
            total += pm['efficiency']
        if pm['overheat']:
            penalty += config['penalty_factor']
    
    # Additional filtering based on efficiency quartiles (real logic)
    efficiencies = sorted([pm['efficiency'] for pm in perf_metrics])
    q1 = efficiencies[len(efficiencies)//4]
    
    bonus = 0
    for pm in perf_metrics:
        if pm['efficiency'] > q1 * 1.5:
            bonus += 5
    
    # Final formula
    result = (total - penalty * 10) + bonus
    
    # Distractor operation (no effect)
    temp_offset = sum(1 for p in perf_metrics if p['overheat']) * 0.5
    
    return int(round(result))

# Key execution point
final_score = evaluate_performance(metrics, baseline)

# Output required format
print(f"Result: {final_score}")