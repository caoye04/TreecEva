def analyze_productivity(logs):
    total_entries = len(logs)
    valid_records = [entry for entry in logs if entry.get('status') == 'completed']
    completion_rate = len(valid_records) / total_entries if total_entries > 0 else 0

    # Irrelevant aggregation
    durations = [entry['duration'] for entry in valid_records if 'duration' in entry]
    avg_duration = sum(durations) / len(durations) if durations else 0

    error_flags = sum(1 for entry in logs if entry.get('error'))
    severity_weight = 0.5 if error_flags > 2 else 1.0

    return completion_rate, avg_duration, severity_weight


def compute_efficiency(data):
    # Semi-relevant transformation
    transform = lambda x: (x * 1.5) ** 0.5
    processed = [transform(v) for v in data if v > 0]
    efficiency = sum(processed) / len(processed) if processed else 0
    return efficiency

# Simulated system metrics
task_log = [
    {'status': 'completed', 'duration': 120, 'error': False, 'priority': 1},
    {'status': 'failed', 'duration': 60, 'error': True, 'priority': 2},
    {'status': 'completed', 'duration': 95, 'error': False, 'priority': 1},
    {'status': 'completed', 'duration': 130, 'error': False, 'priority': 3},
    {'status': 'completed', 'duration': 80, 'error': True, 'priority': 2}
]

durations_only = [t['duration'] for t in task_log]
baseline_effort = sum(durations_only) / len(durations_only)

# Auxiliary computation with partial relevance
effort_metric = compute_efficiency(durations_only)
completion_ratio, avg_time, weight = analyze_productivity(task_log)

# Threshold heuristics
thresholds = {
    'min_completion': 0.6,
    'max_avg_duration': 120,
    'critical_errors': 1
}

metrics = {
    'completion': completion_ratio,
    'efficiency': effort_metric,
    'error_count': sum(1 for t in task_log if t.get('error')),
    'avg_duration': avg_time,
    'total_tasks': len(task_log)
}

# Misleading intermediate calculations
temp_scaling = (metrics['efficiency'] + baseline_effort) * 0.1
dummy_score = (metrics['completion'] * 100) + temp_scaling

# Core evaluation logic
penalty = 0
if metrics['error_count'] > thresholds['critical_errors']:
    penalty += 15
if metrics['avg_duration'] > thresholds['max_avg_duration']:
    penalty += 10
if metrics['completion'] < thresholds['min_completion']:
    penalty += 20

bonus = 5 if metrics['completion'] > 0.7 and metrics['efficiency'] > 10 else 0

# Final scoring with distractor influence
base_value = (metrics['completion'] * 100) + (metrics['efficiency'] * 0.8)
adjusted_score = base_value - penalty + bonus

# Additional red herring: unused function
def calculate_risk(profile):
    risk_factors = sum(1 for k, v in profile.items() if v > 5)
    return risk_factors * 2.5

# Another distraction: irrelevant list processing
priorities = [t['priority'] for t in task_log]
concentration = len([p for p in priorities if p == max(priorities)]) / len(priorities)

scaling_factor = concentration * 100 if concentration > 0.3 else 50

# Critical statement
final_score = int(adjusted_score)

print(f"Result: {final_score}")