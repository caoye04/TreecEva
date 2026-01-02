from collections import defaultdict

# Simulate system performance metrics over time
def collect_metrics(duration_hours):
    metrics = defaultdict(int)
    temp_data = []
    for hour in range(1, duration_hours + 1):
        workload = (hour * 7) % 53
        efficiency = (workload ** 2) % 41
        anomalies = (efficiency * 3) % 19
        
        # Real-time logging (distraction)
        log_entry = f"[LOG] Hour {hour}: W={workload}, E={efficiency}"
        temp_data.append(log_entry)
        
        metrics['total_work'] += workload
        metrics['total_efficiency'] += efficiency
        metrics['anomalies_detected'] += anomalies

    # Dummy post-processing (irrelevant)
    avg_log_length = sum(len(entry) for entry in temp_data) / len(temp_data) if temp_data else 0
    metrics['avg_log_len'] = avg_log_length

    return dict(metrics)

def calculate_baseline(work_days):
    # Unrelated calculation (distractor)
    total_breaks = 0
    for day in range(work_days):
        for _ in range((day % 3) + 1):
            total_breaks += 1
    return total_breaks * 15

def normalize(value, min_val, max_val):
    if max_val == min_val:
        return 0.5
    return (value - min_val) / (max_val - min_val)

def evaluate_performance(metrics, threshold):
    work = metrics.get('total_work', 0)
    efficiency = metrics.get('total_efficiency', 0)
    anomalies = metrics.get('anomalies_detected', 0)
    
    # Normalize components
    norm_work = normalize(work, 100, 500)
    norm_eff = normalize(efficiency, 150, 600)
    
    # Heuristic scoring
    raw_score = (norm_work * 0.6 + norm_eff * 0.4) * 100
    
    # Penalty system
    anomaly_penalty = min(anomalies * 1.5, 30)
    adjusted_score = raw_score - anomaly_penalty
    
    # Threshold scaling (critical path)
    if adjusted_score >= threshold:
        final_score = int(adjusted_score * 1.1)
    else:
        final_score = int(adjusted_score * 0.9)
    
    # Dead code branch (misleading)
    if work < 0:
        final_score = -1  # Never reached
    
    return final_score

# Main execution
base_threshold = 75
operation_days = 8
daily_metrics = collect_metrics(operation_days)
baseline_breaks = calculate_baseline(operation_days)  # Computed but unused

# Irrelevant data transformation
processed_data = [v**0.5 for v in daily_metrics.values() if isinstance(v, (int, float)) and v > 0]

# Key computation
final_score = evaluate_performance(daily_metrics, base_threshold)

# Extraneous adjustment (no effect due to reassignment later)
final_score = final_score // 1  # Identity operation

# Final result output
print(f"Result: {final_score}")