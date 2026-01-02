def calculate_performance(stability, speed):
    base = stability * 0.6
    bonus = speed ** 0.5 * 0.4
    return int(base + bonus)

# System metrics (irrelevant distractor variables included)
uptime_hours = 99.8
cpu_temp_c = 67
disk_usage_percent = 75

# Key input variables
reliability = 85
efficiency = 144

# Calculation pipeline
adjusted_efficiency = efficiency if efficiency <= 150 else 150
reliability_factor = min(reliability, 100)

# Core computation with lambda and slicing
metrics = [70, 75, 80, 85, 90]
sliced_metrics = metrics[1:4]
avg_metric = sum(sliced_metrics) / len(sliced_metrics)

weight_fn = lambda x: x * 0.1
influence = weight_fn(avg_metric)

final_score = calculate_performance(reliability_factor, adjusted_efficiency)

# Output result
print(f"Result: {final_score}")