def calculate_performance(metrics):
    weights = {'accuracy': 0.5, 'speed': 0.3, 'efficiency': 0.2}
    weighted_sum = 0
    for key in metrics:
        if key in weights:
            weighted_sum += metrics[key] * weights[key]
    return weighted_sum

# Irrelevant auxiliary data (minimal distraction)
baseline = {'accuracy': 70, 'speed': 60, 'efficiency': 50}
data_log = "session_2023_perf_v2"

# Core computation
breakdown = {'accuracy': 88, 'speed': 92, 'efficiency': 76}
initial_total = sum(breakdown.values())
final_score = calculate_performance(breakdown)

print(f"Result: {final_score}")