from collections import defaultdict, Counter
import math

# Simulate system telemetry data (irrelevant but plausible)
telemetry_log = [
    {'timestamp': 1, 'cpu': 78, 'mem': 45, 'disk': 200},
    {'timestamp': 2, 'cpu': 85, 'mem': 50, 'disk': 190},
    {'timestamp': 3, 'cpu': 90, 'mem': 60, 'disk': 180}
]

# Dead function - looks important but unused in main logic
def analyze_telemetry(logs):
    stats = defaultdict(int)
    for entry in logs:
        stats['avg_cpu'] += entry['cpu']
        stats['avg_mem'] += entry['mem']
    stats['avg_cpu'] /= len(logs)
    stats['avg_mem'] /= len(logs)
    return stats

# Irrelevant data structure transformation
telemetry_summary = {f"entry_{i}": {k: v for k, v in item.items() if k != 'timestamp'} 
                        for i, item in enumerate(telemetry_log)}

# Decoy performance metric with misleading intermediate calculation
decoy_metrics = [0.91, 0.87, 0.94, 0.83]
adjusted_decoy = sum([x * 1.05 for x in decoy_metrics if x > 0.85]) / len(decoy_metrics)  # Distractor

# Real metrics and weights for evaluation
metrics = {
    'accuracy': 0.92,
    'latency': 0.045,  # in seconds
    'throughput': 240,  # requests per second
    'consistency': 0.88
}

weights = {
    'accuracy': 0.4,
    'latency': 0.3,
    'throughput': 0.2,
    'consistency': 0.1
}

# Auxiliary function using lambda for normalization
normalize = lambda x, low, high: (x - low) / (high - low) if high > low else 0

# Secondary scoring with red herring logic
def calculate_secondary_score(m):
    if m.get('accuracy', 0) < 0.8:
        return 0.5
    score = 0.0
    # This block looks relevant but doesn't affect final answer
    temp_scores = []
    for k, v in m.items():
        if k == 'latency':
            temp_scores.append(normalize(1/v, 0.01, 50) if v > 0 else 0)
        else:
            temp_scores.append(normalize(v, 0.7, 1.0))
    return sum(temp_scores) / len(temp_scores)

secondary_score = calculate_secondary_score(metrics)  # Intermediate distraction

# Complex conditional path that evaluates to False (dead branch)
if metrics['accuracy'] > 0.95 and weights['accuracy'] == 0.5:
    scaling_factor = 1.2
    final_latency = metrics['latency'] * 0.8
    boosted_accuracy = min(metrics['accuracy'] * scaling_factor, 1.0)
elif any([v < 0.8 for v in metrics.values()]):
    scaling_factor = 0.9
    final_score = 0.75
else:
    scaling_factor = 1.0  # Actually used implicitly

# Core evaluation logic buried among distractions
def evaluate_performance(m, w):
    # Normalize latency inversely
    normalized_latency = (1 / m['latency']) / 50  # Normalize to approx 0-1 scale
    
    # Apply weights to scaled metrics
    weighted_accuracy = m['accuracy'] * w['accuracy']
    weighted_latency = normalized_latency * w['latency']
    weighted_throughput = (m['throughput'] / 1000) * w['throughput']  # Scale throughput
    weighted_consistency = m['consistency'] * w['consistency']
    
    # Aggregate score
    total = weighted_accuracy + weighted_latency + weighted_throughput + weighted_consistency
    
    # Additional adjustment based on threshold (always applies)
    if m['accuracy'] >= 0.9:
        total *= 1.05  # Bonus for high accuracy
    
    return total

# Misleading list comprehension that computes something irrelevant
temp_result = [evaluate_performance(metrics, dict(zip(weights.keys(), perm))) 
               for perm in [(0.3,0.4,0.2,0.1), (0.4,0.3,0.1,0.2)] if perm[0] > 0.2]

# Critical execution point
final_score = evaluate_performance(metrics, weights)

# Print result as required
print(f"Target result: {final_score}")