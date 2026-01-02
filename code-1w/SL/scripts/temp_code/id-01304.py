from collections import defaultdict, Counter

# Simulated system telemetry data
technical_logs = [
    {'node': 'A', 'load': 85, 'errors': 3, 'priority': 'high'},
    {'node': 'B', 'load': 45, 'errors': 0, 'priority': 'medium'},
    {'node': 'C', 'load': 92, 'errors': 7, 'priority': 'high'},
    {'node': 'D', 'load': 60, 'errors': 1, 'priority': 'low'},
    {'node': 'E', 'load': 78, 'errors': 5, 'priority': 'medium'}
]

# Irrelevant auxiliary mapping (red herring)
status_weights = {'critical': 10, 'high': 7, 'medium': 4, 'low': 1}

# Distractor computation: node stability index (not used in final result)
stability_index = {}
for log in technical_logs:
    node = log['node']
    stability_index[node] = (100 - log['load']) * (1 + log['errors'])

# Core metric extraction (relevant path)
normalized_loads = [log['load'] / 100 for log in technical_logs]
error_counts = [log['errors'] for log in technical_logs]

# Fake aggregation (dead code path)
total_weighted_priority = 0
for log in technical_logs:
    total_weighted_priority += status_weights.get(log['priority'], 0)

# Real processing begins: categorize nodes by error frequency
error_frequency = Counter(error_counts)
high_error_nodes = len([e for e in error_counts if e >= 5])

# Load distribution analysis
load_categories = defaultdict(int)
for load in normalized_loads:
    if load > 0.8:
        load_categories['overloaded'] += 1
    elif load > 0.5:
        load_categories['moderate'] += 1
    else:
        load_categories['light'] += 1

# Decoy transformation (irrelevant list comprehension)
transformed_metrics = [
    round((load ** 0.5) * 10, 2) 
    for load in normalized_loads 
    if load > 0.7
]

# Simulated threshold calibration (misleading intermediate)
calibration_factor = sum(transformed_metrics) / (high_error_nodes + 1) if high_error_nodes else 0
dynamic_thresholds = {cat: base + calibration_factor for cat, base in load_categories.items()}

# Actual summary structure used in final step
log_summary = {
    'total_nodes': len(technical_logs),
    'avg_load': sum(normalized_loads) / len(normalized_loads),
    'high_error_count': high_error_nodes,
    'category_balance': abs(load_categories['overloaded'] - load_categories['light'])
}

# Threshold map with decoy entries
threshold_map = {
    'critical_load': 0.85,
    'tolerance_window': 0.15,
    'baseline_stability': 0.65,
    'decoy_offset': calibration_factor,  # unused but looks important
    'node_requirement': 3
}

# Redundant validation function (never called)
def validate_system_integrity(data):
    return all(d['errors'] < 10 for d in data) and len(data) > 0

# Unused recursive helper (distraction)
def calculate_robustness_score(nodes, idx=0):
    if idx == len(nodes):
        return 0
    score = nodes[idx]['load'] * 0.8
    if nodes[idx]['priority'] == 'high':
        score *= 1.2
    return score + calculate_robustness_score(nodes, idx + 1)

# Key processing function
def process_metrics(summary, thresholds):
    # Direct computation using only specific fields
    base_score = summary['total_nodes'] * 100
    adjustment = int(summary['avg_load'] * 200)
    penalty = summary['high_error_count'] * 50
    balance_bonus = 30 if summary['category_balance'] <= 1 else 0
    
    # Conditional boost (depends on threshold)
    if summary['total_nodes'] >= thresholds['node_requirement']:
        base_score += 75
    
    # Final formula
    result = base_score + adjustment - penalty + balance_bonus
    
    # Irrelevant bit manipulation (looks complex but unused)
    masked_result = result & 0xFFFF
    shifted = (masked_result << 3) ^ 0xAA
    
    return result  # Only 'result' matters

# Execution point of interest
final_diagnostic = process_metrics(log_summary, threshold_map)
print(f"Target result: {final_diagnostic}")