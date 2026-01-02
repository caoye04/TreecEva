def evaluate_performance(data, weights):
    base = sum(data[metric] * weights.get(metric, 0) for metric in data)
    adjustment = (lambda x: x ** 0.5 if x > 0 else 0)(base - 50)
    return int(base + adjustment)

# Irrelevant auxiliary variable (minimal distraction)
threshold_config = {"min_val": 5, "max_val": 100}

metrics = {
    "accuracy": 85,
    "latency": 12,
    "throughput": 30,
    "reliability": 90
}

weight_map = {
    "accuracy": 0.4,
    "latency": -0.1,
    "throughput": 0.3,
    "reliability": 0.35
}

final_score = evaluate_performance(metrics, weight_map)
print(f"Result: {final_score}")