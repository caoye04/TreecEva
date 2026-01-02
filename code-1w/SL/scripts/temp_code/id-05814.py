from collections import defaultdict, Counter
import math

# Simulated system metrics from a distributed network node
node_metrics = [
    {'latency': 120, 'throughput': 850, 'errors': 3, 'retries': 2},
    {'latency': 95, 'throughput': 900, 'errors': 1, 'retries': 1},
    {'latency': 110, 'throughput': 870, 'errors': 4, 'retries': 3},
    {'latency': 100, 'throughput': 920, 'errors': 0, 'retries': 0},
    {'latency': 105, 'throughput': 880, 'errors': 2, 'retries': 1}
]

# Irrelevant baseline thresholds (distractor)
thresholds = defaultdict(lambda: 0)
thresholds['latency'] = 150
thresholds['throughput'] = 800
thresholds['errors'] = 5

# Weight configuration for performance evaluation
weights = {
    'latency_weight': 0.3,
    'throughput_weight': 0.4,
    'error_penalty': 0.2,
    'reliability_bonus': 0.1
}

# Auxiliary function – not directly used in final calculation (red herring)
def normalize_value(val, min_val, max_val):
    return (val - min_val) / (max_val - min_val) if max_val > min_val else 0

# Secondary metric tracker (unused path)
metric_stats = Counter()
for entry in node_metrics:
    for k, v in entry.items():
        metric_stats[k] += v

# Extract raw values for processing
latencies = [m['latency'] for m in node_metrics]
throughputs = [m['throughput'] for m in node_metrics]
error_counts = [m['errors'] for m in node_metrics]
retry_counts = [m['retries'] for m in node_metrics]

# Compute aggregate indicators (some are distractions)
avg_latency = sum(latencies) / len(latencies)
median_throughput = sorted(throughputs)[len(throughputs)//2]
min_error = min(error_counts)
total_retries = sum(retry_counts)

# Distractor: hypothetical improvement projections
projected_improvement = []
for i, tp in enumerate(throughputs):
    proj = tp * (1 + 0.05 * math.exp(-retry_counts[i]))
    projected_improvement.append(proj)

# Core normalization using inverted scales
normalized_latency = 100 - (avg_latency - 90)  # Lower latency → higher score
normalized_throughput = (median_throughput - 800) * 0.1  # Scale throughput above baseline

# Penalty based on total error incidents
error_rate = sum(error_counts) / len(node_metrics)
penalty = error_rate * 10

# Bonus logic based on retry patterns (conditional activation)
bonus = 0
if total_retries < 5:
    bonus = 5
elif total_retries < 8:
    bonus = 2
else:
    bonus = 0

# Misleading intermediate scoring (dead computation path)
synthetic_score = 0
for i, lat in enumerate(latencies):
    if lat < 110:
        synthetic_score += 10
    elif throughputs[i] > 900:
        synthetic_score += 5

# Actual performance evaluation function
def evaluate_performance(metrics, w):
    # Local weight unpacking
    lw = w['latency_weight']
    tw = w['throughput_weight']
    ep = w['error_penalty']
    rb = w['reliability_bonus']
    
    # Aggregate relevant metrics
    raw_latency = sum(m['latency'] for m in metrics) / len(metrics)
    raw_throughput = sum(m['throughput'] for m in metrics) / len(metrics)
    total_errors = sum(m['errors'] for m in metrics)
    total_retries = sum(m['retries'] for m in metrics)
    
    # Base score components
    latency_score = 120 - raw_latency  # Max 30 when latency=90
    throughput_score = (raw_throughput - 800) * 0.5  # Up to 60 points
    
    # Error penalty scaled by frequency
    error_score = max(0, 20 - (total_errors * 4))
    
    # Reliability bonus only if retries are low
    reliability_score = 10 if total_retries <= 4 else 0
    
    # Final weighted combination
    composite = (
        latency_score * lw +
        throughput_score * tw +
        error_score * ep +
        reliability_score * rb
    )
    
    # Apply nonlinear adjustment for stability
    adjusted = composite * (0.95 + 0.05 * math.cos(math.pi * total_retries / 20))
    
    return round(adjusted, 4)

# Trigger the key evaluation
final_score = evaluate_performance(node_metrics, weights)

# Print result as required
print(f"Target result: {final_score}")