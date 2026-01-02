def analyze_efficiency(metrics):
    adjusted = list(map(lambda x: x * 1.1 if x < 50 else x * 0.95, metrics))
    return [val for val in adjusted if val > 40]

# Simulate employee performance tracking with mixed metrics
task_completion = [85, 90, 78, 92]
error_rate = [12, 8, 15, 10]

productivity = []
for i in range(len(task_completion)):
    raw = task_completion[i] - error_rate[i]
    productivity.append(raw)

# Apply efficiency analysis (distractor function - not directly used)
efficiency_metrics = analyze_efficiency(productivity)

baseline_threshold = 70
risk_factor = 0
for p in productivity:
    if p < baseline_threshold:
        risk_factor += 1

# Misleading intermediate calculation (semi-relevant but not final)
penalty_adjustment = sum([p // 10 for p in productivity if p > 60])
risk_factor *= penalty_adjustment // 2 if penalty_adjustment > 0 else 1

# Core evaluation logic
def evaluate_performance(perf_list, risk):
    base_score = sum(perf_list)
    adjustment = 1 - (risk * 0.05)
    return int(base_score * adjustment)

# Key statement
final_score = evaluate_performance(productivity, risk_factor)

# Additional irrelevant string processing (adds interference)
diagnostic_log = "Performance review completed on Q3 metrics"
diagnostic_code = diagnostic_log.upper().replace(" ", "_").split('_')
checksum = len(diagnostic_code) + len(''.join(diagnostic_code))

# Print result as required
print(f"Result: {final_score}")