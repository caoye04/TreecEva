def analyze_efficiency(metrics):
    base_efficiency = sum(metrics) / len(metrics)
    adjustment = 0.0
    if base_efficiency > 80:
        adjustment = 12.5
    elif base_efficiency > 60:
        adjustment = 5.0
    else:
        adjustment = -10.0
    
    # Distractor: irrelevant calculation for scalability_index
    scalability_index = (max(metrics) - min(metrics)) * 0.75
    normalized_efficiency = base_efficiency + adjustment
    
    return normalized_efficiency


def calculate_risk(behavior_log):
    risk_score = 0
    for action in behavior_log:
        if action == 'error':
            risk_score += 3
        elif action == 'warning':
            risk_score += 1
    
    # Distractor: unused safety_margin
    safety_margin = 100 - risk_score if risk_score < 100 else 0
    
    return max(1, min(10, risk_score))  # Clamp between 1 and 10


def evaluate_performance(output, risk):
    performance = output * 0.7 - risk * 2.5
    bonus = 10 if performance >= 50 else 0
    
    # Use of conditional expression (Python idiom)
    penalty = 5 if 'critical' in [action for action in ['normal', 'minor', 'warning']] else 0
    
    # String method usage: distraction with log tagging
    log_tag = "PERF-{}".format("HIGH" if bonus else "LOW").lower()
    final_value = performance + bonus - penalty
    
    return int(final_value)

# Main execution
metrics_data = [85, 90, 78, 92, 88]
activity_log = ['ok', 'warning', 'ok', 'ok', 'error']

productivity = analyze_efficiency(metrics_data)
risk_factor = calculate_risk(activity_log)

# Irrelevant intermediate variables (distractors)
temp_diagnostic = f"Analysis complete: {len(metrics_data)} metrics processed."
duplicate_risk = calculate_risk(activity_log)  # Redundant call
consistency_check = temp_diagnostic.count('o')  # Useless string count

final_score = evaluate_performance(productivity, risk_factor)
print(f"Result: {final_score}")