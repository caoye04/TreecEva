def analyze_workload(tasks):
    efficiency_metrics = []
    overhead_penalty = 0
    for task in tasks:
        base_time = task['duration']
        complexity_factor = task['complexity']
        if complexity_factor > 7:
            overhead_penalty += 1.5
        elif complexity_factor < 3:
            overhead_penalty -= 0.5
        processed_time = base_time / (complexity_factor + 1)
        efficiency_metrics.append(processed_time)
    
    avg_efficiency = sum(efficiency_metrics) / len(efficiency_metrics) if efficiency_metrics else 0
    return avg_efficiency, overhead_penalty


def validate_data_integrity(records):
    checksum = 0
    anomalies = 0
    for record in records:
        checksum ^= hash(str(record))
        if not record.get('verified', True):
            anomalies += 1
    # Irrelevant normalization
    normalized_checksum = abs(checksum) % 1000 if checksum != 0 else 0
    return normalized_checksum, anomalies

# Simulated dataset
user_sessions = [
    {'duration': 120, 'complexity': 8, 'priority': 'high'},
    {'duration': 90, 'complexity': 5, 'priority': 'medium'},
    {'duration': 150, 'complexity': 9, 'priority': 'high'},
    {'duration': 60, 'complexity': 2, 'priority': 'low'}
]

system_logs = [
    {'event': 'start', 'verified': True},
    {'event': 'process', 'verified': False},
    {'event': 'update', 'verified': True},
    {'event': 'cleanup', 'verified': True}
]

# Extraneous intermediate calculations
baseline_reference = 42.0
scaling_factor = 1.75
adjustment_curve = [i**0.5 for i in range(1, 6)]

# Core logic with distractors
avg_efficiency, penalty = analyze_workload(user_sessions)
data_checksum, issues_found = validate_data_integrity(system_logs)

# Misleading adjustment using irrelevant curve
temp_correction = sum(adjustment_curve) / scaling_factor

# Primary decision logic
if avg_efficiency < 20:
    base_rating = 50
else:
    base_rating = 80

# Apply penalty only if data issues exceed threshold
if issues_found > 1:
    final_adjustment = base_rating - penalty * 10
else:
    final_adjustment = base_rating - penalty * 5

# Red herring: unused transformation
theoretical_limit = baseline_reference * scaling_factor

# Final computation
final_score = int(final_adjustment + (data_checksum % 10))

Result: final_score