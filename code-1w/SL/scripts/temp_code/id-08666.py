from collections import defaultdict, Counter
import math

# Simulated system metrics from a distributed task scheduler
task_logs = [
    {'node': 'A', 'status': 'success', 'duration': 120, 'retries': 0, 'priority': 3},
    {'node': 'B', 'status': 'failure', 'duration': 80, 'retries': 3, 'priority': 5},
    {'node': 'C', 'status': 'success', 'duration': 200, 'retries': 1, 'priority': 4},
    {'node': 'A', 'status': 'success', 'duration': 90, 'retries': 0, 'priority': 2},
    {'node': 'D', 'status': 'failure', 'duration': 150, 'retries': 2, 'priority': 5},
    {'node': 'B', 'status': 'success', 'duration': 110, 'retries': 0, 'priority': 1}
]

# Irrelevant statistical counters (distractors)
status_counter = Counter([log['status'] for log in task_logs])
frequency_by_node = Counter([log['node'] for log in task_logs])

# Fake risk assessment model (dead code path)
def compute_risk_factor(node):
    base = 1.5
    if node == 'A':
        return base * 0.8
    elif node == 'B':
        return base * 1.1
    else:
        return base * 1.3

# Unused transformation (red herring)
transformed_durations = [round(d['duration'] ** 0.5, 2) for d in task_logs]

# Simulated weight configuration (some values are misleading)
weights = {
    'success_rate': 0.4,
    'avg_duration': -0.3,  # Negative weight: shorter is better
    'retry_penalty': -0.5,
    'priority_bonus': 0.2,
    'fake_metric': 0.0  # Unused weight (distractor)
}

# Node-specific metadata (partially used)
node_profiles = defaultdict(dict)
for log in task_logs:
    node = log['node']
    if 'first_seen' not in node_profiles[node]:
        node_profiles[node]['first_seen'] = log['duration']
    node_profiles[node]['last_duration'] = log['duration']

# Core processing function

def aggregate_node_metrics(logs):
    node_data = defaultdict(list)
    
    for entry in logs:
        node = entry['node']
        node_data[node].append(entry)
    
    results = {}
    for node, entries in node_data.items():
        successes = [e for e in entries if e['status'] == 'success']
        failures = [e for e in entries if e['status'] == 'failure']
        
        success_rate = len(successes) / len(entries)
        avg_duration = sum(e['duration'] for e in successes) / len(successes) if successes else float('inf')
        total_retries = sum(e['retries'] for e in entries)
        avg_priority = sum(e['priority'] for e in entries) / len(entries)
        
        results[node] = {
            'success_rate': success_rate,
            'avg_duration': avg_duration,
            'total_retries': total_retries,
            'avg_priority': avg_priority,
            'performance_flag': success_rate >= 0.5 and avg_duration < 150
        }
    
    return results

# Secondary scoring with bit manipulation red herring

def apply_bitwise_offset(value, level=3):
    # This function is called but offset discarded in main logic
    if value <= 0:
        return int(value)
    shifted = value << 1
    masked = shifted & 0xFF
    return masked ^ level

# Another decoy function (never called in critical path)
def validate_consistency(data_map):
    for k, v in data_map.items():
        if v['total_retries'] > 5 and v['success_rate'] < 0.3:
            return False
    return True

# Main evaluation logic

def evaluate_performance(metrics, weights):
    score = 0.0
    
    # Intermediate accumulators (some used, some not)
    temp_values = defaultdict(float)
    debug_flags = []
    
    for node, data in metrics.items():
        local_score = 0
        
        # Relevant scoring components
        local_score += data['success_rate'] * weights['success_rate']
        if data['avg_duration'] != float('inf'):
            local_score += (1 / math.log(data['avg_duration'] + 1)) * weights['avg_duration']
        
        retry_factor = 1 / (1 + data['total_retries'])
        local_score += retry_factor * abs(weights['retry_penalty'])  # Corrected sign usage
        
        local_score += data['avg_priority'] * weights['priority_bonus']
        
        # Dead computation: bitwise distraction
        dummy_offset = apply_bitwise_offset(int(local_score * 100), 3)
        temp_values[f'{node}_offset'] = dummy_offset  # Stored but unused
        
        # Flag recording (irrelevant to final score)
        if data['performance_flag']:
            debug_flags.append(f'{node}_pass')
        
        score += local_score
    
    # Global adjustment based on system-wide characteristics
    all_avg_prios = [d['avg_priority'] for d in metrics.values()]
    system_balance = 1 + (max(all_avg_prios) - min(all_avg_prios)) * 0.1
    
    # Final non-linear transformation
    adjusted_score = (score * system_balance) + 10  # Base uplift
    
    # Spurious string-based check (distractor)
    node_names = ''.join(sorted(metrics.keys()))
    if 'ABCD' in node_names + 'CDAB':
        adjusted_score += 1.5  # Misleading bump
    
    return round(adjusted_score, 6)

# Execute core pipeline
aggregated = aggregate_node_metrics(task_logs)
final_score = evaluate_performance(aggregated, weights)

# Print result as required
print(f"Result: {final_score}")