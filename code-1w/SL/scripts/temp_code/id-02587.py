def calculate_performance(base, logs):
    adjustment = len(list(filter(lambda x: x > base, logs)))
    scaling_factor = 1.5 if adjustment > 2 else 1.0
    return round(base * scaling_factor + sum(logs) / len(logs), 3)

# System baseline measurement
temp_data = [23.1, 34.2, 45.3, 56.4, 67.5]
baseline = sum(temp_data) / len(temp_data)

# Performance metrics from recent runs
metrics = [30, 42, 38, 55, 47]

# Irrelevant string processing (minimal distraction)
diagnostic_log = "System check passed at all nodes"
node_count = len(diagnostic_log.split())

final_score = calculate_performance(baseline, metrics)
print(f"Result: {final_score}")