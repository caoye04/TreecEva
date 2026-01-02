import math

# Simulated system metrics from a distributed computing environment
task_completion = [0.92, 0.87, 0.96, 0.78, 1.0]
node_latency = [120, 200, 95, 300, 150]  # in ms
error_rates = [0.01, 0.03, 0.005, 0.1, 0.02]
throughput = [450, 320, 510, 200, 390]  # requests/sec

# Irrelevant auxiliary data (distractor)
dummy_logs = [{'id': i, 'status': 'OK' if i % 2 == 0 else 'FAIL'} for i in range(len(task_completion))]
scaling_factors = {i: 1 + 0.1 * i for i in range(5)}

# Weight configuration for performance evaluation (critical input)
weights = {
    'completion': 0.4,
    'latency': 0.3,
    'errors': -0.2,  # negative weight: lower is better
    'throughput': 0.1
}

# Preprocessing with list comprehensions and lambda functions
normalized_latency = [(300 - lat) / 200 for lat in node_latency]  # inverted and scaled
normalized_errors = [max(0, 1 - 10 * err) for err in error_rates]

# Complex metric transformation using dictionary and lambda
transformations = {
    'linear': lambda x: x,
    'square': lambda x: x ** 2,
    'root': lambda x: math.sqrt(x),
    'logit': lambda x: math.log(x / (1 - x)) if x < 1 and x > 0 else 0
}

# Apply non-linear transform (only some are used)
applied_xform = [transformations['square'](val) for val in task_completion]
applied_lat = [transformations['root'](norm) for norm in normalized_latency]

# Dead code path - never executed (red herring)
def deprecated_eval(data):
    return sum(data) / len(data) if data else 0

# Unused recursive function (decoy)
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

# Simulated historical baselines (irrelevant)
historical_avg = {
    'completion': 0.85,
    'latency_norm': 0.65,
    'error_norm': 0.88,
    'throughput': 380
}

# Core evaluation logic
metrics = {
    'completion': sum(applied_xform) / len(applied_xform),
    'latency': sum(applied_lat) / len(applied_lat),
    'errors': sum(normalized_errors) / len(normalized_errors),
    'throughput': sum(throughput) / max(throughput)  # normalized average
}

# Misleading intermediate calculation (not final)
temp_score = 0
for k in metrics:
    temp_score += metrics[k] * 0.25  # equal-weighted (incorrect method)

# Final evaluation using correct weights
final_score = 0
for key in weights:
    if key in metrics:
        final_score += metrics[key] * weights[key]

# Additional distraction: set operation with no impact
critical_nodes = {i for i, err in enumerate(error_rates) if err > 0.02}
redundant_set = {i for i in range(5) if task_completion[i] > 0.9}
intersection_flag = len(critical_nodes & redundant_set) > 0

# Print result for inspection
print(f"Result: {final_score}")