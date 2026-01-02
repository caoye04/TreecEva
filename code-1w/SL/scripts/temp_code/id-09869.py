def analyze_efficiency(metrics):
    base_effort = sum([m * 1.5 for m in metrics if m > 2])
    adjustment = len(metrics) // 2
    return int(base_effort - adjustment)

metrics_data = [3, 4, 1, 5, 2, 4]

# Irrelevant transformation chain (distractor)
temp_transform = [x ** 2 for x in metrics_data]
normalized = [t / max(temp_transform) for t in temp_transform]
scaled_metrics = [int(n * 10) for n in normalized]

# Real usage
efficiency = analyze_efficiency(metrics_data)

productivity = efficiency + 10

# Simulate risk assessment using set operations
task_ids = {1, 2, 3, 4, 5, 6, 7, 8}
failed_tasks = {2, 5, 7}
completed_tasks = task_ids - failed_tasks
risk_set = {x for x in failed_tasks if x % 2 == 1}  # Only odd-numbered failed tasks

# Dummy string processing (distractor)
diagnostic_log = "Error: Task failure detected in module"
error_count = diagnostic_log.count("Task")
severity_flag = diagnostic_log.upper().startswith("ERROR")
formatted_msg = f"[{error_count}] {diagnostic_log.replace('detected', 'identified')}"

# Core logic masked by distractions
def evaluate_performance(output, risk):    
    base_score = output * 3
    penalty = 0
    if len(risk) > 0:
        penalty = sum([r * 10 for r in risk])
    
    # Additional distraction: unused helper calculation
    avg_risk = sum(risk) / len(risk) if risk else 0
    buffer_zone = {x + 1 for x in risk}
    overlap = buffer_zone & task_ids  # semi-relevant but not used
    
    final_raw = base_score - penalty
    
    # Apply rounding based on logical condition
    if final_raw > 100 and severity_flag:
        final_raw = int(final_raw * 0.95)
    else:
        final_raw = int(final_raw * 1.05)  # slight boost
    
    return final_raw

# Key assignment point
current_state = "active"
final_score = evaluate_performance(productivity, risk_set)

# Print result as required
print(f"Target result: {final_score}")