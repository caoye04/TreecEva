from collections import defaultdict, Counter
import math

# Simulated system telemetry data
telemetry_logs = [
    'ERROR: disk_full', 'WARNING: cpu_high', 'INFO: service_restart',
    'ERROR: network_drop', 'ERROR: disk_full', 'WARNING: memory_leak',
    'INFO: heartbeat', 'WARNING: cpu_high', 'ERROR: network_drop'
]

# Irrelevant aggregation (distractor)
distinct_events = set(log.split(':')[1].strip() for log in telemetry_logs)
event_counter = Counter(telemetry_logs)

# Fake diagnostic function (dead code path)
def analyze_health_legacy(logs):
    stats = defaultdict(int)
    for log in logs:
        level = log.split(':')[0]
        stats[level] += 1
    return {k: v / len(logs) for k, v in stats.items()}

# Unused transformation (misleading intermediate)
log_frequencies = {event: telemetry_logs.count(f'ERROR: {event}') for event in distinct_events if 'disk' in event}

# Core evaluation logic
baseline_thresholds = {'latency': 200, 'retries': 5, 'timeout_rate': 0.05}
metrics = {
    'latency': 180,
    'retries': 3,
    'timeout_rate': 0.03,
    'availability': 0.997,
    'jitter': 12.4
}

weights = defaultdict(float, {
    'latency': 0.3,
    'retries': 0.25,
    'timeout_rate': 0.25,
    'availability': 0.2
})

# Secondary irrelevant calculation (red herring)
adjusted_metrics = {}
for k, v in metrics.items():
    if k == 'jitter':
        adjusted_metrics[k] = v * 1.15
    elif k == 'availability':
        adjusted_metrics[k] = round(v * 100, 2)
    else:
        adjusted_metrics[k] = max(v, 0)

# Decoy scoring function (never called)
def compute_legacy_score(data):
    score = 0
    for key, val in data.items():
        if val > baseline_thresholds.get(key, 1000):
            score -= 10
        else:
            score += 5
    return score + 50

# Real evaluation with nested logic and distractors
def evaluate_performance(metrs, wts):
    raw_scores = {}
    penalty_adjustment = 0
    
    # Complex conditional scoring
    for name, value in metrs.items():
        if name not in wts:
            continue
        
        threshold = baseline_thresholds.get(name, None)
        weight = wts[name]
        
        if threshold is None:
            raw_scores[name] = 100 * weight
            continue
        
        # Multi-step normalization
        if name == 'timeout_rate':
            normalized = max(0, 1 - (value / threshold))
            score = 80 + int(normalized * 20)
        elif name == 'availability':
            score = int(value * 100)
        else:
            if value <= threshold * 0.8:
                score = 100
            elif value <= threshold:
                score = 80 + int((threshold - value) / (threshold * 0.2) * 20)
            else:
                underperformance = (value - threshold) / threshold
                score = max(50, 80 - int(underperformance * 100))
                if name == 'latency':
                    penalty_adjustment -= 5  # Specific penalty
        
        raw_scores[name] = score * weight
    
    # Final aggregation with distraction
    base_total = sum(raw_scores.values())
    adjustment_factor = math.cos(math.pi / 6)  # Constant: ~0.866
    
    # Additional fake bonus (never applies due to logic)
    bonus = 0
    if all(metrs[k] < baseline_thresholds[k] * 0.7 for k in ['latency', 'retries'] if k in metrs):
        bonus = 10
    
    # Actual result computation
    final_raw = base_total + penalty_adjustment
    scaled_result = final_raw * adjustment_factor
    
    # Key execution point
    final_score = int(round(scaled_result))
    
    # Dead code branch (misleads flow understanding)
    if final_score > 95:
        status = 'OPTIMAL'
    elif final_score > 80:
        status = 'STABLE'
    else:
        status = 'DEGRADED'
        if metrs['latency'] > 250:
            status += '_CRITICAL'
    
    return final_score

# Execution with red herrings
snapshot_weights = [weights[k] for k in sorted(weights.keys())]
synthetic_metric = sum(len(log.split(':')[0]) for log in telemetry_logs) % 7

# Critical assignment
final_score = evaluate_performance(metrics, weights)

# Output requirement
print(f"Result: {final_score}")