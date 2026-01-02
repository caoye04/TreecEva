from collections import defaultdict, Counter
import math

# Simulated system metrics from a distributed network node
metrics = {
    'latency_ms': 127,
    'packet_loss_ratio': 0.037,
    'throughput_mbps': 89,
    'retries': 5,
    'jitter_ms': 4.2,
    'uptime_hours': 372,
    'error_count': 14
}

# Baseline thresholds for ideal performance
baseline = {
    'latency_ms': 100,
    'packet_loss_ratio': 0.02,
    'throughput_mbps': 100,
    'retries': 3,
    'jitter_ms': 5.0  # Note: higher jitter is worse, so this is a ceiling
}

# Irrelevant telemetry data (distractor)
telemetry_snapshot = [
    {'sensor': 'temp', 'value': 68, 'unit': 'F'},
    {'sensor': 'cpu', 'value': 72.3, 'unit': '%'},
    {'sensor': 'memory', 'value': 4128, 'unit': 'MB'}
]

telemetry_stats = defaultdict(int)
for entry in telemetry_snapshot:
    telemetry_stats[entry['sensor']] += entry['value']

# Dead function - never called (red herring)
def analyze_hardware_health(snapshot):
    warnings = 0
    for s in snapshot:
        if s['value'] > 80:
            warnings += 1
    return warnings

# Misleading intermediate calculation (distractor)
normalized_latency = round((metrics['latency_ms'] / baseline['latency_ms']) * 100)
effective_reliability = (1 - metrics['packet_loss_ratio']) ** metrics['retries']
adjusted_jitter = max(0, baseline['jitter_ms'] - metrics['jitter_ms'])  # inverted meaning

# Decoy scoring using irrelevant formula
decoy_score = 0
if metrics['throughput_mbps'] > baseline['throughput_mbps'] * 0.8:
    if metrics['error_count'] < 10:
        decoy_score += 20
    decoy_score += 10
if metrics['uptime_hours'] > 360:
    decoy_score += 15  # This path is taken but irrelevant

# Unused weight map (dead code path)
weight_map = Counter()
weight_map['latency'] = 0.3
weight_map['throughput'] = 0.25
weight_map['reliability'] = 0.35
weight_map['stability'] = 0.1

# Core evaluation logic (buried among distractors)
def calculate_latency_impact(latency, base):
    return max(0, 1 - (latency / base))

def calculate_packet_penalty(loss, base):
    return max(0, 1 - (loss / base))

def calculate_throughput_bonus(tp, base):
    return min(1.2, tp / base)

def calculate_retry_decay(retries, base):
    return 0.95 ** abs(retries - base)

# Main scoring function
def evaluate_performance(m, b):
    score_components = defaultdict(float)
    
    # Real scoring components
    score_components['latency'] = calculate_latency_impact(m['latency_ms'], b['latency_ms'])
    score_components['packet'] = calculate_packet_penalty(m['packet_loss_ratio'], b['packet_loss_ratio'])
    score_components['throughput'] = calculate_throughput_bonus(m['throughput_mbps'], b['throughput_mbps'])
    score_components['retry'] = calculate_retry_decay(m['retries'], b['retries'])
    
    # Composite score with weighted sum
    composite = (
        score_components['latency'] * 0.3 +
        score_components['packet'] * 0.3 +
        score_components['throughput'] * 0.25 +
        score_components['retry'] * 0.15
    )
    
    # Final nonlinear transformation
    final_raw = composite * 100
    penalty_factor = 0.1 * m['error_count']
    adjusted_score = final_raw * (1 - penalty_factor) if penalty_factor < 1 else final_raw * 0.1
    
    # Normalize to bounded output
    bounded_score = max(0, min(100, adjusted_score))
    
    # Key result variable
    final_score = int(round(bounded_score))
    
    # Distractor: unused conditional modification
    if m['jitter_ms'] < b['jitter_ms']:
        final_score += 5  # This would help, but jitter not used in main logic
    
    return final_score

# Execution point of interest
final_score = evaluate_performance(metrics, baseline)

# Print required result
print(f"Result: {final_score}")