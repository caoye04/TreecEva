def analyze_health_status(vital_signs):
    # Irrelevant health metrics (distractors)
    heart_rate_zone = 'Normal' if 60 <= vital_signs['hr'] <= 100 else 'Elevated'
    bp_category = 'Optimal' if vital_signs['sbp'] < 120 else 'High'
    irrelevant_flag = False

    # Dummy transformation (dead code path)
    transformed = [x ** 0.5 for x in vital_signs['history'] if x > 0]
    if len(transformed) > 10:
        irrelevant_flag = True

    # Real computation buried in noise
    avg_temp = sum(vital_signs['temps']) / len(vital_signs['temps'])
    fever_present = any(t >= 38.0 for t in vital_signs['temps'])
    
    # Misleading score calculation
    base_risk = 0
    if vital_signs['age'] > 65:
        base_risk += 30
    if fever_present:
        base_risk += 25

    # This function doesn't get called but looks important
    def calculate_stress_index(logs):
        return sum(abs(a - b) for a, b in zip(logs, logs[1:])) * 1.5

    # Actual signal: respiratory stability
    rr_changes = [abs(vital_signs['rr'][i] - vital_signs['rr'][i-1]) for i in range(1, len(vital_signs['rr']))]
    stability_score = 100 - sum(rr_changes)  # Key component

    return stability_score


def evaluate_performance(metrics):
    # Distractor variables
    baseline_thresholds = {'cpu': 80, 'mem': 75, 'io': 40}
    performance_tier = None
    audit_log = []
    temp_result = {}

    # Complex conditional expression with red herring logic
    tier_code = 'A' if metrics['throughput'] > 1000 else ('B' if metrics['latency'] < 50 else 'C')
    bonus_applied = False

    # List comprehension with side-effect logging (mostly irrelevant)
    [audit_log.append(f'Event: {event["type"]}') for event in metrics['events'] if event['severity'] > 2]

    # Decoy accumulation
    fake_accumulator = 0
    for val in metrics['trace_data']:
        shifted = val << 2
        masked = shifted & 0xFF
        fake_accumulator += masked  # Never used

    # Early return trap (never triggered due to data)
    if metrics['version'] == 'legacy':
        return -1  # Dead path

    # Real logic hidden among distractions
    raw_score = metrics['base'] * 1.2
    if metrics['optimized']:
        raw_score += 42

    adjustment = 0
    if 'calibration' in metrics and metrics['calibration']:
        adjustment = sum(1 for x in metrics['factors'] if x > 0.5) * 5

    final_score = int(raw_score + adjustment)  # This is the real answer

    # Unused complex structure
    summary = {
        'score': final_score,
        'tier': tier_code,
        'flags': [k for k, v in metrics.items() if isinstance(v, bool) and v]
    }

    return final_score

# Main execution
metric_data = {
    'base': 786,
    'optimized': True,
    'throughput': 1200,
    'latency': 30,
    'version': 'latest',
    'calibration': True,
    'factors': [0.1, 0.9, 0.6, 0.3, 0.7],
    'events': [
        {'type': 'start', 'severity': 1},
        {'type': 'error', 'severity': 3},
        {'type': 'retry', 'severity': 2}
    ],
    'trace_data': [10, 20, 30, 40]
}

# Call that produces the target result
final_score = evaluate_performance(metric_data)
print(f"Result: {final_score}")