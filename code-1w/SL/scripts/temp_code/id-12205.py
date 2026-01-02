from collections import defaultdict, Counter
import math

# Simulated system telemetry data
telemetry_log = [
    'ERROR:disk_full', 'WARNING:cpu_spike', 'INFO:service_restart',
    'ERROR:network_loss', 'ERROR:disk_full', 'WARNING:mem_leak',
    'INFO:service_restart', 'ERROR:network_loss', 'WARNING:cpu_spike'
]

# Parse logs into structured format
event_counts = defaultdict(int)
event_types = []
for entry in telemetry_log:
    if ':' in entry:
        level, event = entry.split(':', 1)
        event_counts[(level, event)] += 1
        event_types.append(event)

# Irrelevant aggregation: counts per severity
count_by_severity = Counter([e.split(':')[0] for e in telemetry_log])

# Critical metrics (only disk and network errors affect score)
disk_error_count = event_counts[('ERROR', 'disk_full')]
network_error_count = event_counts[('ERROR', 'network_loss')]

# Misleading intermediate: uptime-derived weight (not actually used)
uptime_hours = 97.5
theoretical_weight = math.log(uptime_hours + 1) if uptime_hours > 0 else 0

# Weight assignment logic with red herring branches
base_weights = {'disk': 1.0, 'network': 1.0, 'memory': 0.5}

if disk_error_count > 1:
    base_weights['disk'] *= 1.5

if network_error_count >= 2:
    base_weights['network'] *= 2.0

# Dead code path: hypothetical memory escalation (never triggered in this input)
if 'mem_usage_critical' in event_types:
    base_weights['memory'] *= 3.0  # Unused in final calculation

# Spurious transformation: reverse event type frequencies
event_freq = Counter(event_types)
transformed_freqs = {k: v ** 0.5 for k, v in event_freq.items() if v > 1}

# Real metric computation begins here
raw_metrics = {
    'disk_health': max(0, 100 - (disk_error_count * 15)),
    'network_stability': max(0, 100 - (network_error_count * 12))
}

# Hidden normalization using character count from static string
normalization_key = len('system_integrity_verify')  # = 21

normalized_disk = raw_metrics['disk_health'] / normalization_key
normalized_network = raw_metrics['network_stability'] / normalization_key

# Correct weights based on actual error thresholds
weights = {
    'disk': base_weights['disk'] if disk_error_count > 0 else 1.0,
    'network': base_weights['network'] * 1.1 if network_error_count > 0 else 1.0
}

# Composite scoring with conditional boosts
performance_boost = 1.0
if raw_metrics['disk_health'] > 70 and raw_metrics['network_stability'] > 70:
    performance_boost = 1.2

# Main evaluation function
def evaluate_performance(metrics, w):
    score = 0.0
    components = ['disk_health', 'network_stability']
    
    # Map metrics to weights via name substring matching (advanced logic)
    for comp in components:
        if 'disk' in comp:
            score += metrics[comp] * w['disk']
        elif 'network' in comp:
            score += metrics[comp] * w['network']
    
    # Apply boost only if both normalized values exceed threshold
    if normalized_disk > 3.0 and normalized_network > 3.0:
        score *= performance_boost
    
    # Final adjustment: subtract sum of unused memory weight and theoretical weight
    global base_weights, theoretical_weight
    unused_penalty = base_weights.get('memory', 0) + theoretical_weight * 0.1
    return score - unused_penalty

# Execute main logic
diagnostic_report = {"status": "processed", "entries": len(telemetry_log)}
summary_stats = {"unique_events": len(set(event_types)), "total_errors": sum(count_by_severity[e] for e in ['ERROR'])}

# Key execution point
final_score = evaluate_performance(raw_metrics, weights)

# Output result
print(f"Result: {final_score}")