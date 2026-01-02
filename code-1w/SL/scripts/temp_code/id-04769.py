def evaluate_system_status(metrics):
    severity_weight = lambda x: 1.5 if x > 75 else 0.8
    
    base_risk = metrics['cpu_load'] * 0.3 + metrics['mem_usage'] * 0.4
    adjusted_risk = base_risk * severity_weight(metrics['error_rate'])
    
    # Irrelevant diagnostic flag (distractor)
    system_stable = adjusted_risk < 50
    
    anomaly_detected = metrics['latency_spike'] and not (metrics['recovery_mode'] or system_stable)
    
    if anomaly_detected:
        threshold_score = int(adjusted_risk * 1.75)
    else:
        threshold_score = int(adjusted_risk * 1.2)
    
    return {'status': anomaly_detected, 'score': threshold_score}

# Input metrics
data_feed = {
    'cpu_load': 68,
    'mem_usage': 72,
    'error_rate': 80,
    'latency_spike': True,
    'recovery_mode': False
}

# Execution
final_diagnostic = evaluate_system_status(data_feed)
threshold_score = final_diagnostic['score']
print(f"Result: {threshold_score}")