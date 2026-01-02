def analyze_productivity(logs):
    total_entries = len(logs)
    valid_entries = [e for e in logs if e['status'] == 'completed']
    completion_rate = len(valid_entries) / total_entries if total_entries else 0

    # Irrelevant distraction: idle time analysis (not used later)
    idle_times = [e['duration'] for e in logs if e['status'] == 'idle']
    avg_idle = sum(idle_times) / len(idle_times) if idle_times else 0
    efficiency_ratio = (1 - avg_idle / 3600) if avg_idle else 1  # unused red herring

    # Distractor: fake normalization function
    normalize = lambda x: max(0.1, min(x, 1.0))
    fake_normalized = [normalize(e['duration']/3600) for e in valid_entries]

    return completion_rate


def evaluate_stress_level(workload):
    stress_index = 0
    for task in workload:
        if task['priority'] > 2:
            stress_index += task['complexity'] * task['priority']
    # Dead code path — never called
    def adjust_for_overtime(s):
        return s * 1.5 if s > 100 else s
    return stress_index if stress_index > 0 else 50

# Unused auxiliary data structure
historical_data = {
    'Q1': {'output': 85, 'errors': 3},
    'Q2': {'output': 92, 'errors': 1},
    'Q3': {'output': 78, 'errors': 5}
}

# Real input data
current_logs = [
    {'status': 'completed', 'duration': 1800, 'type': 'dev'},
    {'status': 'completed', 'duration': 2700, 'type': 'dev'},
    {'status': 'idle', 'duration': 3600, 'type': 'break'},
    {'status': 'completed', 'duration': 1500, 'type': 'review'},
    {'status': 'idle', 'duration': 7200, 'type': 'downtime'}
]

workload_snapshot = [
    {'priority': 3, 'complexity': 4},
    {'priority': 1, 'complexity': 2},
    {'priority': 4, 'complexity': 5}
]

# Key processing chain begins here
base_metric_a = analyze_productivity(current_logs)
synthetic_metric_b = evaluate_stress_level(workload_snapshot)

# Decoy transformation (looks important but unused)
adjusted_stress = synthetic_metric_b * 0.85
temp_scaling = [x*0.1 for x in [synthetic_metric_b] if x > 60]

# Core metrics dictionary with meaningful and irrelevant entries
metrics = {
    'completion': base_metric_a,
    'latency_avg': 2400.0,  # distractor
    'error_count': 0,       # irrelevant
    'stress': synthetic_metric_b,
    'throughput': 3         # unused
}

# Weight mapping – only 'completion' and 'stress' are actually used
weights = {
    'completion': 0.6,
    'stress': 0.4,
    'latency_avg': 0.0,   # explicitly zero-weighted (misleading)
    'throughput': 0.0     # red herring
}

# Critical aggregation function
def aggregate_performance(met, wgt):
    score = 0.0
    # Only two keys have non-zero weights
    for key in met:
        if wgt.get(key, 0) > 0:
            score += met[key] * wgt[key]
    
    # Additional logic to obscure the path
    if 'error_count' in met and met['error_count'] == 0:
        score *= 1.1  # bonus condition (technically relevant but already known)
    
    # Fake correction factor based on nonexistent config
    config_mode = 'standard'  # decoy constant
    if config_mode == 'aggressive':
        score = min(score, 75)
    elif config_mode == 'conservative':
        score = max(score, 25)
    
    return round(score, 4)

# Execution point of interest
final_score = aggregate_performance(metrics, weights)

# Output result as required
print(f"Target result: {final_score}")