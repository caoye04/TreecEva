def evaluate_performance(metrics, exceptions):
    base = 100
    penalty = 0
    
    # Irrelevant tracking (distractor)
    audit_log = set()
    temp_factor = 0
    for val in metrics:
        if val < 85:
            penalty += 5
            audit_log.add(f'low_metric_{val}')
        elif val > 95:
            temp_factor += 2  # Not used later

    # Misleading intermediate calculation
    phantom_score = base - penalty + (len(metrics) * 0.5)
    
    # Key logic: adjust based on exception patterns
    critical_flags = set([x for x in exceptions if 'critical' in x])
    warning_flags = set([x for x in exceptions if 'warning' in x])
    
    # Distractor: unused subset
    info_only = set([x for x in exceptions if 'info' in x and x not in critical_flags])

    if len(critical_flags) > 0:
        phantom_score -= 20
    elif len(warning_flags) >= 3:
        phantom_score -= 10
    else:
        phantom_score -= 5

    # Conditional expression with red herring variables
    adjustment = 15 if len(critical_flags) == 0 and sum(1 for m in metrics if m > 90) >= 4 else 0
    
    # Early return red herring (not taken due to logic)
    if phantom_score < 50:
        return 0  # Dead code path — won't trigger

    # Final score depends only on relevant paths
    final_score = phantom_score + adjustment
    
    # Print required output
    print(f'Result: {final_score}')
    return final_score

# Input data
productivity = [92, 88, 96, 91, 87]
risk_set = ['warning_load', 'warning_cache', 'warning_io', 'critical_db']

# Trigger execution
evaluate_performance(productivity, risk_set)