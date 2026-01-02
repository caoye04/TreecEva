from collections import defaultdict, Counter
import math

# Simulate system telemetry data
telemetry_logs = [
    'cpu:high mem:low disk:medium',
    'cpu:medium mem:high disk:low',
    'cpu:low mem:medium disk:high',
    'cpu:high mem:high disk:high'
]

# Irrelevant helper function (decoy)
def analyze_network_traffic(logs):
    traffic_pattern = defaultdict(int)
    for log in logs:
        if 'net' in log:
            parts = log.split(' ')
            for part in parts:
                if 'net' in part:
                    k, v = part.split(':')
                    traffic_pattern[v] += 1
    return dict(traffic_pattern)

# Unused but plausible transformation
def legacy_normalize(values):
    max_val = max(values) if values else 1
    return [v / max_val for v in values]

# Core metric processing
def parse_telemetry(logs):
    parsed = []
    resource_map = {'low': 1, 'medium': 2, 'high': 3}
    for log in logs:
        entries = log.split(' ')
        record = {}
        for entry in entries:
            resource, level = entry.split(':')
            record[resource] = resource_map.get(level, 0)
        parsed.append(record)
    return parsed

# Secondary computation - frequency analysis (partially relevant)
def compute_frequency_bias(data):
    freq_counter = Counter()
    for record in data:
        freq_counter.update(record.keys())
    total = sum(freq_counter.values())
    return {k: freq_counter[k] / total for k in freq_counter}

# Weight adjustment based on bias
def adjust_weights(base_weights, bias):
    adjusted = {}
    for k in base_weights:
        # Only cpu and mem are actually used
        if k in ['cpu', 'mem']:
            adjusted[k] = base_weights[k] * (1 + bias.get(k, 0))
    return adjusted

# Main evaluation logic
def calculate_stability_index(records):
    stability = []
    for r in records:
        # Stability is only defined on cpu and mem
        s = (r.get('cpu', 0) + r.get('mem', 0)) / 2
        stability.append(s ** 1.5)
    return sum(stability)

# Final scoring with conditional weighting
def evaluate_performance(metrics, weights):
    raw_scores = []    
    for m in metrics:
        score = 0
        # Only cpu and mem contribute to final score
        if m['cpu'] >= 2:
            score += m['cpu'] * weights['cpu']
        if m['mem'] >= 2:
            score += m['mem'] * weights['mem']
        # disk is mentioned but does NOT contribute
        raw_scores.append(score)
    
    avg_raw = sum(raw_scores) / len(raw_scores) if raw_scores else 0
    
    # Apply stability bonus only if avg > 3.0
    stability_metrics = [{'cpu': m['cpu'], 'mem': m['mem']} for m in metrics]
    stability_index = calculate_stability_index(stability_metrics)
    
    # Bonus logic
    bonus = 0
    if avg_raw > 3.0:
        bonus = stability_index * 0.7
    elif avg_raw > 2.0:
        bonus = stability_index * 0.3
        
    final = avg_raw * 1.2 + bonus
    
    # Red herring: normalize to 100 scale (not actually used)
    normalized = min(final * 10, 100) if final > 0 else 0
    
    return int(round(final))  # Deterministic integer result

# Initialization
base_weights = {'cpu': 1.8, 'mem': 1.6, 'disk': 1.4}  # disk weight is irrelevant

# Parse logs into structured metrics
metrics_data = parse_telemetry(telemetry_logs)

# Compute frequency bias (only cpu and mem matter)
frequency_bias = compute_frequency_bias(metrics_data)

# Adjust weights using bias
adjusted_weights = adjust_weights(base_weights, frequency_bias)

# DEAD CODE PATH - never called
# def debug_print_all():
#     print(f"Raw: {telemetry_logs}")
#     print(f"Parsed: {metrics_data}")

# Critical execution point
final_score = evaluate_performance(metrics_data, adjusted_weights)

# Output result
print(f"Target result: {final_score}")