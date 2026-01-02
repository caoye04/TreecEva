def analyze_efficiency(data, threshold=0.75):
    """Irrelevant helper function analyzing efficiency (dead code path)."""
    return [x for x in data if x > threshold]


def normalize_vector(v):
    """Another decoy function not used in main logic."""
    norm = sum(x ** 2 for x in v) ** 0.5
    return [x / norm for x in v] if norm else v

# Simulated system metrics from distributed task execution
task_durations = [120, 85, 93, 110, 97, 88]
resource_usage = [0.65, 0.78, 0.82, 0.71, 0.69, 0.85]
error_rates = [0.02, 0.01, 0.03, 0.02, 0.01, 0.04]

# Misleading intermediate aggregations (distractors)
avg_duration = sum(task_durations) / len(task_durations)
peak_usage = max(resource_usage)
total_errors = sum(error_rates)

# Unused transformation pipeline (red herring)
smoothed_errors = [e * 0.9 + 0.01 for e in error_rates]
adjusted_durations = [d if d < 100 else 100 + (d - 100) ** 0.5 for d in task_durations]

# Weight configuration for evaluation (only this matters)
weights = {
    'latency': 0.4,
    'throughput': 0.3,
    'stability': 0.2,
    'reliability': 0.1
}

# Derived metrics with slicing and transformations
completion_rate = len([d for d in task_durations if d <= 100]) / len(task_durations)
throughput_metric = completion_rate * 100
latency_metric = 100 - ((avg_duration - 90) * 2)  # Base latency score

# Hidden reliability calculation using bit manipulation (key hidden logic)
error_ints = [int(e * 100) for e in error_rates]
reliability_word = 0
for val in error_ints:
    reliability_word ^= val  # Bitwise XOR accumulation
reliability_score = 100 - (reliability_word % 25)

# Stability via variance approximation without using import (clever distractor)
m_dev = sum(abs(x - 0.75) for x in resource_usage) / len(resource_usage)
stability_score = 100 - (m_dev * 40)

# Dictionary of final metrics (core input to answer)
metrics = {
    'latency': max(1, min(100, latency_metric)),
    'throughput': max(1, min(100, throughput_metric * 10)),
    'stability': max(1, min(100, stability_score)),
    'reliability': max(1, min(100, reliability_score))
}

# Unused complex data structure (decoy)
class PerformanceNode:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.children = []

# Critical function that computes the answer
def evaluate_performance(met, wgt):
    """Compute weighted performance score from metrics and weights."""
    raw_score = 0.0
    for key in wgt:
        if key in met:
            raw_score += wgt[key] * met[key]
    # Final nonlinear adjustment based on minimum metric
    min_component = min(met[k] for k in wgt if k in met)
    adjustment = 1 + (min_component - 50) / 1000
    return int(raw_score * adjustment)

# Execution point of interest
final_score = evaluate_performance(metrics, weights)

# Irrelevant list operations (extra distraction)
duplicate_check = [x for x in task_durations if task_durations.count(x) > 1]
usage_segments = resource_usage[::2] + resource_usage[1::2]

# Output required result
print(f"Target result: {final_score}")