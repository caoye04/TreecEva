from collections import defaultdict, Counter
import math

# Simulated system performance metrics (some are red herrings)
def get_system_metrics():
    data = defaultdict(float)
    data['latency'] = 120.5
    data['throughput'] = 850.2
    data['error_rate'] = 0.0034
    data['memory_usage'] = 78.9
    data['cpu_temp'] = 67.2  # irrelevant
    data['disk_reads'] = 4300  # misleading
    data['network_latency'] = 120.5  # duplicate
    data['packet_loss'] = 0.001
    data['jitter'] = 4.3
    return data

def apply_normalization(val, min_val=0, max_val=1000):
    # Only used for specific metrics, others bypass
    if val <= min_val:
        return 0.0
    if val >= max_val:
        return 1.0
    return val / max_val

def calculate_efficiency_ratio(tput, lat):
    # Useful function: efficiency = throughput / latency
    if lat == 0:
        return 0.0
    return tput / lat

def analyze_packet_integrity(pl, jitter):
    # Distractor function - not actually used in final score
    score = 1 - pl - (jitter * 0.01)
    return max(0.0, score)

def filter_outliers(values, threshold=2.0):
    # Dead code path - never called
    mean = sum(values) / len(values)
    std = (sum((x - mean)**2 for x in values) / len(values))**0.5
    return [v for v in values if abs(v - mean) < threshold * std]

def compute_health_factor(temp, usage):
    # Decoy logic - looks important but unused
    if temp > 80:
        return 0.3
    elif usage > 90:
        return 0.4
    else:
        return 1.0

# Weight configuration (only some weights matter)
weights = {
    'normalized_latency': 0.3,
    'efficiency_ratio': 0.5,
    'stability_index': 0.15,
    'security_score': 0.05,  # unused
    'redundancy_factor': 0.0  # explicit zero weight
}

# Irrelevant transformation chain
temp_log_entries = ['ERR', 'INFO', 'WARN', 'INFO', 'INFO']
log_counter = Counter(temp_log_entries)
log_entropy = sum(-v/len(temp_log_entries) * math.log(v/len(temp_log_entries)) for v in log_counter.values())

# Another decoy structure
historical_trends = []
for i in range(5):
    trend_point = {'epoch': i, 'val': 100 * math.sin(i * 0.5)}
    if trend_point['val'] > 80:
        trend_point['flag'] = True
    historical_trends.append(trend_point)

# Core evaluation logic
def evaluate_performance(metrics, w):
    score = 0.0

    # Step 1: Normalize latency (used)
    norm_lat = apply_normalization(metrics['latency'], min_val=1, max_val=200)
    score += w['normalized_latency'] * (1 - norm_lat)  # lower latency = higher score

    # Step 2: Compute efficiency ratio (used)
    eff_ratio = calculate_efficiency_ratio(metrics['throughput'], metrics['latency'])
    scaled_eff = min(eff_ratio / 10.0, 1.0)
    score += w['efficiency_ratio'] * scaled_eff

    # Step 3: Stability index from error rate and jitter (used)
    base_stability = (1 - metrics['error_rate']) * (1 - metrics['jitter'] * 0.01)
    stability_index = max(0.0, min(1.0, base_stability))
    score += w['stability_index'] * stability_index

    # Step 4: Fake security score (weight present but zero)
    sec_score = 0.95 if metrics['packet_loss'] < 0.01 else 0.6
    score += w['security_score'] * sec_score  # adds 0

    # Unused intermediate variables (distractors)
    memory_normalized = apply_normalization(metrics['memory_usage'], 0, 100)
    cpu_health = compute_health_factor(metrics['cpu_temp'], metrics['memory_usage'])
    packet_integrity = analyze_packet_integrity(metrics['packet_loss'], metrics['jitter'])

    # Red herring list comprehension with side effects (but no real impact)
    _ = [x * 0.9 for x in [metrics['disk_reads']] if metrics['disk_reads'] > 1000]

    # Final adjustment based on hidden rule: if latency equals network_latency, bonus
    if metrics['latency'] == metrics['network_latency']:
        score *= 1.05  # small boost

    return round(score * 1000)  # scale to integer

# Main execution flow
raw_metrics = get_system_metrics()

# Simulate data processing pipeline (some steps are dead ends)
processed_metrics = {}
for k, v in raw_metrics.items():
    if k in ['latency', 'throughput', 'error_rate', 'memory_usage', 'packet_loss', 'jitter']:
        processed_metrics[k] = v

# Add a fake derived metric (unused)
processed_metrics['bandwidth_utilization'] = raw_metrics['throughput'] * 0.01

# Critical statement
final_score = evaluate_performance(processed_metrics, weights)

print(f"Result: {final_score}")