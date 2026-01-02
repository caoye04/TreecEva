from collections import defaultdict, Counter
import math

# Simulated system performance metrics (real data)
system_data = [
    {'cpu': 70, 'mem': 65, 'disk': 40, 'net': 30},
    {'cpu': 85, 'mem': 70, 'disk': 55, 'net': 45},
    {'cpu': 90, 'mem': 80, 'disk': 60, 'net': 50},
    {'cpu': 60, 'mem': 50, 'disk': 30, 'net': 20}
]

# Irrelevant telemetry logs (distractor data)
telemetry_logs = [
    {'ts': 1001, 'event': 'ping', 'node': 'A'},
    {'ts': 1002, 'event': 'ack', 'node': 'B'},
    {'ts': 1003, 'event': 'ping', 'node': 'C'}
]

# Dead function – never called (red herring)
def analyze_network_flow(logs):
    flow_count = defaultdict(int)
    for log in logs:
        flow_count[log['event']] += 1
    return flow_count

# Misleading intermediate calculation (irrelevant)
baseline_avg = 0
for record in system_data:
    baseline_avg += sum(record.values()) / len(record)
baseline_avg /= len(system_data)
baseline_avg = round(baseline_avg, 2)  # Looks important, isn't used

# Weight configuration for actual evaluation (critical)
weights = {
    'cpu': 0.4,
    'mem': 0.3,
    'disk': 0.2,
    'net': 0.1
}

# Historical thresholds (distractor)
historical_thresholds = [65, 70, 72, 75, 78]
median_threshold = sorted(historical_thresholds)[len(historical_thresholds)//2]

# Helper: Normalize metric using sigmoid (used in evaluation)
def normalize(value):
    return 1 / (1 + math.exp(-0.1 * (value - 50)))

# Aggregation function with distraction logic
def aggregate_metrics(data_list):
    raw_totals = defaultdict(float)
    counts = defaultdict(int)
    
    # Accumulate raw sums (partially relevant)
    for entry in data_list:
        for k, v in entry.items():
            raw_totals[k] += v
            counts[k] += 1
    
    # Compute averages (only some are used later)
    averages = {k: raw_totals[k] / counts[k] for k in raw_totals}
    
    # Decoy transformation: entropy-like measure (never used)
    entropy = 0
    total_sum = sum(averages.values())
    for v in averages.values():
        p = v / total_sum
        if p > 0:
            entropy -= p * math.log(p)
    
    return averages  # Only this is returned and used

# Another unused helper (dead code path)
def detect_anomalies(values, threshold=75):
    anomalies = []
    for i, val in enumerate(values):
        if val > threshold:
            anomalies.append(i)
    return anomalies

# Core evaluation logic (key)
def evaluate_performance(metrics_dict, weight_map):
    # Step 1: Aggregate input metrics
    avg_metrics = aggregate_metrics(metrics_dict)
    
    # Step 2: Normalize each metric score
    normalized_scores = {}
    for k, v in avg_metrics.items():
        normalized_scores[k] = normalize(v)
    
    # Step 3: Apply weights
    weighted_sum = 0.0
    for k in weight_map:
        if k in normalized_scores:
            weighted_sum += normalized_scores[k] * weight_map[k]
    
    # Step 4: Scale to 0-100 range
    final_score = weighted_sum * 100
    
    # Red herring: adjust based on phantom condition (never triggers)
    adjustment_factor = 0
    if 'gpu' in avg_metrics and avg_metrics['gpu'] > 90:
        adjustment_factor = -5
    final_score += adjustment_factor  # No effect
    
    # Final rounding
    final_score = round(final_score, 4)
    
    return final_score

# Unused counter (distractor)
metric_counter = Counter()
for d in system_data:
    for k in d:
        metric_counter[k] += 1

# Key execution point
metrics = system_data
final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")