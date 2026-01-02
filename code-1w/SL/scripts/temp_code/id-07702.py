from itertools import combinations

# System performance evaluation with multiple metrics
def analyze_response_times(times):
    avg = sum(times) / len(times)
    variance = sum((t - avg) ** 2 for t in times) / len(times)
    return avg, variance

def generate_thresholds(base_value):
    # Generates irrelevant thresholds for distraction
    return [base_value * i for i in range(1, 5)]

def filter_outliers(data, limit=3):
    mean = sum(data) / len(data)
    filtered = [x for x in data if abs(x - mean) < limit * mean / 10]
    return filtered  # Not actually used in final logic

def compute_entropy(values):
    from math import log
    total = sum(values)
    probabilities = [v / total for v in values]
    entropy = -sum(p * log(p) for p in probabilities if p > 0)
    return entropy  # Computed but not used directly

def evaluate_performance(metrics):
    base = metrics['throughput']
    latency_factor = 1 / (metrics['latency'] + 1)
    error_penalty = 0.95 if metrics['error_rate'] < 0.05 else 0.8

    # Irrelevant combinatorial analysis (distractor)
    pairs = list(combinations([base, latency_factor, error_penalty], 2))
    pair_products = [a * b for a, b in pairs]

    # Core scoring logic
    raw_score = base * latency_factor * error_penalty
    adjustment = 0.1 * metrics.get('jitter', 0.1)  # Small adjustment
    adjusted_score = raw_score - adjustment

    # Additional unused state tracking
    status_flags = {"stable": True, "optimized": False}
    if adjusted_score > 2.0:
        status_flags["optimized"] = True

    return round(adjusted_score, 4)

# Simulated system telemetry data
telemetry_stream = [120, 115, 118, 130, 125, 119, 117]
response_avg, response_var = analyze_response_times(telemetry_stream)

# Generate unused threshold set for interference
dynamic_thresholds = generate_thresholds(response_avg)

# Compute auxiliary metric that won't be used
entropy_metric = compute_entropy([50, 30, 20])

# Define main metric set
metric_set = {
    'throughput': 150,
    'latency': 2.0,
    'error_rate': 0.03,
    'jitter': 0.15
}

# Filtered data (calculated but not used)
filtered_durations = filter_outliers(telemetry_stream)

# Evaluate final performance score
final_score = evaluate_performance(metric_set)

# Print result as required
print(f"Result: {final_score}")