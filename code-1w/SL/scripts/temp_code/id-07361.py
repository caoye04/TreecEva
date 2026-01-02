from collections import defaultdict, Counter

# Simulated network node diagnostic system with red herrings and distractions

def collect_signals(node_id, frequency_band):
    # Irrelevant signal collection (distraction)
    signals = []
    for i in range(5):
        phase = (i * frequency_band) % 4
        amplitude = (i ** 2 + phase * 0.5) / (frequency_band + 1)
        signals.append(amplitude)
    return signals

def compute_entropy(data_stream):
    # Misleading entropy calculation (not actually used in final result)
    counts = Counter(data_stream)
    total = len(data_stream)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * (p ** 0.5)  # Not real entropy, but looks plausible
    return round(entropy, 4)

def evaluate_node_health(node_data):
    # Distractor function: looks important but not used
    baseline = node_data.get('baseline', 1.0)
    readings = node_data.get('readings', [])
    if not readings:
        return 0.0
    avg = sum(readings) / len(readings)
    return (avg / baseline) * 100

def generate_timestamp_segments(duration):
    # Dead code path — never called
    segments = []
    for t in range(0, duration, 10):
        segments.append(f'T{t:03d}')
    return segments

def filter_anomalies(log_entries):
    # Unused anomaly filter (red herring)
    anomalies = []
    for entry in log_entries:
        if 'ERR' in entry or 'FAULT' in entry:
            anomalies.append(entry)
    return anomalies

# Core data structures with mixed relevance
network_nodes = {
    'N001': {'status': 'active', 'weight': 3, 'metrics': [4, 7, 2]},
    'N002': {'status': 'standby', 'weight': 1, 'metrics': [5, 5, 5]},
    'N003': {'status': 'active', 'weight': 2, 'metrics': [1, 8, 3]},
    'N004': {'status': 'active', 'weight': 4, 'metrics': [6, 2, 7]}
}

diagnostics = [
    {'node': 'N001', 'code': 'OK', 'priority': 2},
    {'node': 'N002', 'code': 'WARN', 'priority': 1},
    {'node': 'N003', 'code': 'OK', 'priority': 3},
    {'node': 'N004', 'code': 'OK', 'priority': 4}
]

# Irrelevant global variables (distractors)
current_bandwidth = 987.4
last_sync_cycle = 'COMPLETED'
system_uptime_hours = 1273
redundant_flag = False
shadow_register = [0] * 16

# Decoy intermediate calculations
entropy_pool = []
for i in range(3):
    stream = [j % (i + 2) for j in range(8)]
    entropy_pool.append(compute_entropy(stream))

# Unused data transformation chain
temp_weights = list(map(lambda x: x * 1.5, [1, 2, 3]))
processed_diagnostics = list(filter(lambda d: d['code'] == 'OK', diagnostics))

# Hidden core logic buried in distractions
health_scores = defaultdict(float)
for nid, data in network_nodes.items():
    if data['status'] != 'active':
        continue
    raw_score = sum(data['metrics'])
    weighted_score = raw_score * data['weight']
    health_scores[nid] = weighted_score

# Secondary scoring from diagnostics
priority_map = defaultdict(int)
for entry in diagnostics:
    priority_map[entry['node']] = entry['priority']

# Actual answer computation — obscured by noise
composite_index = 0
for node_id in health_scores:
    # Only active nodes contribute
    base = health_scores[node_id]
    bonus = priority_map[node_id] * 10
    composite_index += base + bonus

# Critical red herring: looks like correction factor, but unused
normalization_factor = len([n for n in network_nodes if network_nodes[n]['status'] == 'active'])
if normalization_factor > 0:
    adjusted_index = composite_index / normalization_factor
else:
    adjusted_index = 0

# Final aggregation using irrelevant lambdas and dictionary ops
aggregation_key = lambda w, p: w + p  # Never actually used as a function

# THIS IS THE KEY STATEMENT
final_diagnostic = composite_index + 5  # Add magic offset

# Another decoy block
summary_table = {}
for k in network_nodes:
    summary_table[k] = {
        'score': health_scores.get(k, 0),
        'flagged': k not in [d['node'] for d in processed_diagnostics]
    }

# Output required result
print(f"Result: {final_diagnostic}")