from collections import defaultdict, Counter
import math

# Simulated system telemetry data
telemetry_logs = [
    {'cpu': 75, 'mem': 80, 'disk': 40, 'latency': 23},
    {'cpu': 60, 'mem': 65, 'disk': 50, 'latency': 18},
    {'cpu': 90, 'mem': 88, 'disk': 30, 'latency': 45},
    {'cpu': 55, 'mem': 50, 'disk': 60, 'latency': 15}
]

# Irrelevant helper (distractor)
def analyze_pattern(seq):
    freq = defaultdict(int)
    for s in seq:
        freq[s] += 1
    return dict(freq)

# Unused transformation function (dead code path)
def transform_data(raw):
    result = []
    for item in raw:
        transformed = {k: v * 1.1 for k, v in item.items()}
        result.append(transformed)
    return result

# Decoy metric calculator with misleading intermediate output
def calculate_health_index(logs):
    scores = []
    for entry in logs:
        # Complex but irrelevant formula
        h = (entry['cpu'] * 0.3 + entry['mem'] * 0.3 + entry['disk'] * 0.2) / (entry['latency'] + 1)
        scores.append(round(h, 2))
    print(f"DEBUG: Health indices (not used): {scores}")
    return sum(scores) / len(scores)

calculate_health_index(telemetry_logs)  # Executed but result ignored

# Real processing begins here
base_metrics = ['response_time', 'throughput', 'error_rate', 'availability']
raw_values = [120, 850, 0.023, 0.997]

# Mapping of metric names to values using zip (required feature)
metric_dict = dict(zip(base_metrics, raw_values))

# Additional derived metrics with distractors
extended_metrics = metric_dict.copy()
extended_metrics['p95_latency'] = 145
extended_metrics['cache_hit_ratio'] = 0.88
extended_metrics['retry_count'] = 3

# Weight configuration (only some are actually used)
weights = defaultdict(float)
weights.update({
    'response_time': 0.35,
    'throughput': 0.25,
    'error_rate': -0.2,      # negative weight: lower is better
    'availability': 0.2,
    'p95_latency': 0.1,      # defined but not used (red herring)
    'cache_hit_ratio': 0.05  # defined but not used
})

# Spurious enumeration with side effects (distractor)
deviation_log = []
for i, (metric, val) in enumerate(zip(base_metrics, raw_values)):
    expected = [100, 1000, 0.01, 1.0]
    dev = abs(val - expected[i]) / expected[i]
    deviation_log.append((i, metric, round(dev, 3)))

print(f"Deviation trace (not part of final score): {deviation_log}")

# Core evaluation logic (key path)
def normalize_response_time(rt):
    return max(0, min(1, (200 - rt) / 100))  # higher rt → lower score

def normalize_throughput(tp):
    return min(1, tp / 1000)

def normalize_error_rate(er):
    return max(0, 1 - er / 0.05)  # assumes 5% threshold

def normalize_availability(av):
    return av  # already in [0,1]

# Main scoring function
metrics_used = ['response_time', 'throughput', 'error_rate', 'availability']
def evaluate_performance(metrics, weight_map):
    normalized = {}
    
    # Use enumerate to track processing step (legitimate use)
    for idx, m in enumerate(metrics_used):
        if m == 'response_time':
            normalized[m] = normalize_response_time(metrics[m])
        elif m == 'throughput':
            normalized[m] = normalize_throughput(metrics[m])
        elif m == 'error_rate':
            normalized[m] = normalize_error_rate(metrics[m])
        elif m == 'availability':
            normalized[m] = normalize_availability(metrics[m])
    
    # Compute weighted sum — only using the first four weights
    total_weight = sum(weight_map[m] for m in metrics_used)
    weighted_sum = 0
    for m in metrics_used:
        weighted_sum += normalized[m] * weight_map[m]
    
    # Final adjustment based on consistency (extra logic)
    consistency_bonus = 1.0
    values_tuple = tuple(normalized.values())
    if all(score > 0.7 for score in values_tuple):
        consistency_bonus = 1.1
    
    raw_score = weighted_sum / total_weight
    final = raw_score * consistency_bonus * 100
    
    # Dead branch (misleading)
    if final > 120:  # impossible due to normalization
        final = 120
        
    return round(final, 4)

# Execute main logic
final_score = evaluate_performance(metric_dict, weights)

# Print required output
print(f"Result: {final_score}")