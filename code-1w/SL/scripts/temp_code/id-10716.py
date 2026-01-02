from collections import defaultdict, Counter
import math

# Simulated system telemetry data
telemetry_stream = [
    {'node': 'A', 'load': 0.4, 'temp': 32, 'errors': 2},
    {'node': 'B', 'load': 0.8, 'temp': 45, 'errors': 1},
    {'node': 'A', 'load': 0.6, 'temp': 34, 'errors': 0},
    {'node': 'C', 'load': 0.3, 'temp': 29, 'errors': 3},
    {'node': 'B', 'load': 0.7, 'temp': 47, 'errors': 0},
    {'node': 'C', 'load': 0.9, 'temp': 51, 'errors': 1}
]

# Irrelevant helper function (decoy)
def calculate_fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b

# Unused transformation map (red herring)
transform_map = {
    'low': lambda x: x * 0.5,
    'medium': lambda x: x * 1.2,
    'high': lambda x: x * 1.8
}

# Fake aggregation (distractor)
fake_aggregate = 0
for entry in telemetry_stream:
    fake_aggregate += entry['temp'] ** 0.5

# Real processing begins here
def extract_node_loads(data):
    node_loads = defaultdict(list)
    for record in data:
        node_loads[record['node']].append(record['load'])
    return node_loads

# Misleading intermediate calculation (irrelevant)
avg_temp_by_node = {}
total_temps = 0
for item in telemetry_stream:
    total_temps += item['temp']
avg_temp_overall = total_temps / len(telemetry_stream)

# Decoy statistical function
def compute_entropy(values):
    counts = Counter(values)
    total = len(values)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return entropy

# Core logic disguised among noise
critical_nodes = set()
for record in telemetry_stream:
    if record['load'] > 0.75 and record['temp'] > 44:
        critical_nodes.add(record['node'])

# Another distraction: string-based node classification (unused)
node_class = {}
for node in ['A','B','C']:
    if node in critical_nodes:
        node_class[node] = 'RED'
    else:
        node_class[node] = 'GREEN'

# Actual signal extraction
error_count_per_node = defaultdict(int)
for r in telemetry_stream:
    error_count_per_node[r['node']] += r['errors']

# Construct log data for real processing
log_data = []
for record in telemetry_stream:
    status_flag = 1 if record['load'] > 0.65 else 0
    temp_factor = math.exp((record['temp'] - 30) / 10)
    combined_score = record['load'] * temp_factor + status_flag * 0.1
    log_data.append({
        'node': record['node'],
        'score': round(combined_score, 4),
        'initial_flag': status_flag
    })

# Red herring: unused list comprehension
dummy_scores = [x['score'] * 0.95 for x in log_data if x['node'] == 'X']  # No such node

# Threshold logic buried in complexity
system_baseline = 0
weight_sum = 0
for entry in log_data:
    contribution = entry['score'] * (1 + entry['initial_flag'])
    system_baseline += contribution
    weight_sum += (1 + entry['initial_flag'])

if weight_sum > 0:
    system_baseline /= weight_sum

# Secondary decoy: recursive traversal (never called)
def traverse_nodes(node_set, path=[]):
    if not node_set:
        return [path]
    results = []
    for n in node_set:
        results.extend(traverse_nodes(node_set - {n}, path + [n]))
    return results

# Key threshold determined from data patterns
system_threshold = 0.45 + (len(critical_nodes) * 0.15)

# Real processing function with embedded logic
def process_metrics(metrics, threshold):
    high_risk_count = 0
    total_adjusted = 0.0
    
    # First pass: identify high-risk entries
    for m in metrics:
        if m['score'] > threshold:
            high_risk_count += 1
        
    # Second pass: conditional accumulation
    for m in metrics:
        base = m['score']
        if m['initial_flag'] == 1:
            base *= 1.25
        if high_risk_count >= 2:
            base *= 1.1
        total_adjusted += base
    
    # Third phase: normalization and correction
    if high_risk_count > 0:
        total_adjusted /= high_risk_count
    else:
        total_adjusted = 0.0
    
    # Final adjustment based on error history (cross-concept linkage)
    global error_count_per_node
    penalty_factor = 1.0
    for entry in metrics:
        node = entry['node']
        if error_count_per_node.get(node, 0) > 1:
            penalty_factor += 0.05
    
    final_value = total_adjusted * penalty_factor
    return round(final_value, 6)

# Execution point of interest
final_diagnostic = process_metrics(log_data, system_threshold)

# Print result as required
print(f"Result: {final_diagnostic}")