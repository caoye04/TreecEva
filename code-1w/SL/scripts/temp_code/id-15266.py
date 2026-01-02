from collections import defaultdict, Counter

# Simulated system metrics from a distributed computing environment
timestamped_logs = [
    {'node': 'A', 'cpu': 70, 'mem': 45, 'tasks': 8, 'errors': 0},
    {'node': 'B', 'cpu': 85, 'mem': 60, 'tasks': 12, 'errors': 1},
    {'node': 'C', 'cpu': 55, 'mem': 30, 'tasks': 6, 'errors': 0},
    {'node': 'A', 'cpu': 72, 'mem': 47, 'tasks': 9, 'errors': 0},
    {'node': 'B', 'cpu': 90, 'mem': 62, 'tasks': 10, 'errors': 2},
    {'node': 'D', 'cpu': 40, 'mem': 20, 'tasks': 5, 'errors': 0}
]

# Irrelevant function - decoy for data visualization
def visualize_node_load(logs):
    node_load = defaultdict(list)
    for log in logs:
        node_load[log['node']].append(log['cpu'])
    return {k: sum(v)/len(v) for k, v in node_load.items()}

# Unused aggregation - misleading path
aggregated_cpu = visualize_node_load(timestamped_logs)
peak_nodes = [node for node, load in aggregated_cpu.items() if load > 80]

# Core metric computation (relevant)
def extract_metrics(logs):
    task_efficiency = defaultdict(list)
    error_count = 0
    total_tasks = 0
    
    for entry in logs:
        task_efficiency[entry['node']].append(entry['tasks'] / (entry['cpu'] + 1))
        error_count += entry['errors']
        total_tasks += entry['tasks']
    
    efficiency_scores = {}
    for node, efficiencies in task_efficiency.items():
        efficiency_scores[node] = round(sum(efficiencies) / len(efficiencies), 3)
    
    # Distractor variables
    avg_error_rate = error_count / len(logs) if logs else 0
    redundancy_factor = total_tasks % 7  # unused
    
    return efficiency_scores, total_tasks, error_count

# Secondary processing with set operations
legacy_nodes = {'A', 'C'}
active_nodes = {log['node'] for log in timestamped_logs}
supported_nodes = active_nodes - legacy_nodes  # {'B', 'D'}

# Another red herring: string-based node validation (never used)
valid_node_pattern = ''.join(sorted(supported_nodes))
if valid_node_pattern.startswith('B'):
    compliance_flag = 2 * len(valid_node_pattern)
else:
    compliance_flag = 0

# Real data transformation chain
efficiency_map, total_task_count, total_errors = extract_metrics(timestamped_logs)

# Simulated benchmark thresholds
baseline_efficiency = 0.11
penalty_per_error = 0.05
bonus_for_high_volume = 0.02

# Decoy list comprehension - computes nothing useful
idle_predictions = [\n    (n, eff * 0.1) for n, eff in efficiency_map.items() if n not in supported_nodes
]

# Core scoring logic
raw_score_components = []
for node in supported_nodes:
    if node in efficiency_map:
        base = efficiency_map[node]
        if base > baseline_efficiency:
            raw_score_components.append(base + bonus_for_high_volume)
        else:
            raw_score_components.append(base)

# Misleading intermediate calculation (not final)
average_raw = sum(raw_score_components) / len(raw_score_components) if raw_score_components else 0
temp_adjustment = len(supported_nodes) * 0.01

# Critical distraction: complex but unused formula
theoretical_max = (total_task_count / (total_errors + 1)) * average_raw
impact_weights = defaultdict(float)
for i, node in enumerate(supported_nodes):
    impact_weights[node] = (i + 1) * 0.05  # never applied

# Actual final evaluation logic
metric_set = set(efficiency_map.keys())  # {'A', 'B', 'C', 'D'}
benchmark_data = {
    'target_nodes': supported_nodes,  # {'B', 'D'}
    'base_multiplier': 100,
    'threshold': 0.12
}

def evaluate_performance(nodes_of_interest, config):
    target_nodes = config['target_nodes']
    score = 0.0
    for node in nodes_of_interest:
        if node in efficiency_map and node in target_nodes:
            eff = efficiency_map[node]
            if eff >= config['threshold']:
                score += eff * config['base_multiplier']
            else:
                score += eff * config['base_multiplier'] * 0.5
    # Additional logic based on global state
    if total_errors == 0:
        score *= 1.1
    return round(score, 4)

# Execution point of interest
final_score = evaluate_performance(metric_set, benchmark_data)

# Print result as required
print(f"Target result: {final_score}")