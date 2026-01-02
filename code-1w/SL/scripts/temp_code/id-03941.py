def analyze_efficiency(metrics):
    adjusted = [m * 1.2 for m in metrics if m > 5]
    return sum(adjusted) // len(adjusted) if adjusted else 0


def calculate_stress_level(hours, deadlines):
    stress_index = 0
    for h in hours:
        if h > 8:
            stress_index += (h - 8) * 2
    for d in deadlines:
        stress_index += d
    return stress_index


def evaluate_performance(output, risk):
    base = sum(output)
    penalty = 0
    if risk > 15:
        penalty = base * 0.3
    elif risk > 10:
        penalty = base * 0.15
    return int(base - penalty)

# Simulated dataset
productivity = [8, 12, 15, 7, 10]
time_logs = [7, 9, 10, 12, 6]
deadline_count = [3, 5, 4]

# Irrelevant preprocessing (distractor)
avg_time = sum(time_logs) / len(time_logs)
peak_hours = [t for t in time_logs if t >= 9]
efficiency_ratio = avg_time / max(time_logs) if time_logs else 0

# Unused helper (dead code path)
def normalize_data(data):
    max_val = max(data)
    return [d / max_val for d in data]

# Secondary metric with partial relevance
workload_intensity = len(time_logs) * sum(deadline_count)
stress_level = calculate_stress_level(time_logs, deadline_count)

# Core logic embedded in distractions
baseline_metrics = [p + 2 for p in productivity if p < 14]
efficiency_score = analyze_efficiency(baseline_metrics)

# Noise variables
phantom_threshold = efficiency_score * 0.75
shadow_adjustment = workload_intensity % 7

# Key computational chain
risk_factor = stress_level + (workload_intensity // 10)
final_score = evaluate_performance(productivity, risk_factor)

print(f"Result: {final_score}")