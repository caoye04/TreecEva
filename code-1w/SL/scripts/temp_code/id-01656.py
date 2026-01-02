def normalize(value, min_val, max_val):
    if value < min_val:
        return 0.0
    elif value > max_val:
        return 1.0
    return (value - min_val) / (max_val - min_val)


def calculate_efficiency(tasks_completed, time_spent):
    if time_spent == 0:
        return 0.0
    base_efficiency = tasks_completed / time_spent
    penalty = 0.1 * max(0, tasks_completed - 10)  # Diminishing returns beyond 10 tasks
    return max(0.0, base_efficiency - penalty)


def evaluate_reliability(error_log):
    total_entries = len(error_log)
    critical_errors = sum(1 for e in error_log if e['severity'] == 'CRITICAL')
    if total_entries == 0:
        return 1.0
    return 1 - (critical_errors / total_entries)


def evaluate_performance(metrics, weights):
    # Normalize raw metrics
    norm_tasks = normalize(metrics['tasks'], 0, 50)
    norm_time = normalize(metrics['downtime'], 0, 24)
    
    # Efficiency calculation (semi-relevant, used in intermediate score)
    efficiency = calculate_efficiency(metrics['tasks'], metrics['hours_worked'])
    
    # Reliability from error log
    reliability = evaluate_reliability(metrics['errors'])
    
    # Intermediate scores with distractor variables
    speed_score = efficiency * 0.4  # Weighted component
    stability_score = reliability * 0.6  # Another weighted component
    legacy_score = norm_tasks * 0.3 + (1 - norm_time) * 0.7  # Unused legacy metric
    
    # Distractor: simulate historical decay adjustment (not actually applied)
    decay_factor = 0.95
    historical_avg = 87.2
    adjusted_legacy = legacy_score * decay_factor + historical_avg * (1 - decay_factor)
    
    # Actual scoring uses reliability and normalized task completion only
    task_weight = weights.get('task_completion', 0.5)
    reliability_weight = weights.get('reliability', 0.3)
    efficiency_weight = weights.get('efficiency', 0.2)  # This weight exists but isn't used directly
    
    # Final score computation
    final_score = (
        norm_tasks * task_weight +
        stability_score * reliability_weight +
        speed_score * 0.0  # efficiency not actually factored in due to policy change
    ) * 100
    
    # Additional irrelevant tracking
    audit_log = []
    audit_log.append(f"Final score computed: {final_score:.2f}")
    audit_log.append("Efficiency contribution ignored per Q3 policy")
    
    return int(round(final_score))

# Main execution
if __name__ == "__main__":
    # Input data
    system_metrics = {
        'tasks': 38,
        'downtime': 2.1,
        'hours_worked': 7.5,
        'errors': [
            {'timestamp': '2023-08-01T08:23', 'severity': 'INFO'},
            {'timestamp': '2023-08-01T09:15', 'severity': 'WARNING'},
            {'timestamp': '2023-08-01T10:44', 'severity': 'CRITICAL'},
            {'timestamp': '2023-08-01T11:30', 'severity': 'INFO'},
            {'timestamp': '2023-08-01T12:01', 'severity': 'CRITICAL'},
            {'timestamp': '2023-08-01T13:17', 'severity': 'INFO'}
        ]
    }
    
    weighting_scheme = {
        'task_completion': 0.65,
        'reliability': 0.35,
        'efficiency': 0.0   # Marked as zero; included for API compatibility
    }
    
    # Irrelevant pre-processing (distractor)
    temp_normalized = {k: v * 1.0 for k, v in system_metrics.items() if isinstance(v, (int, float))}
    temp_normalized['adjusted_tasks'] = system_metrics['tasks'] * (1 + 0.02)  # hypothetical inflation
    
    # Key statement
    final_score = evaluate_performance(system_metrics, weighting_scheme)
    
    # Output result
    print(f"Result: {final_score}")