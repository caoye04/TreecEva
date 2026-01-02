from collections import defaultdict, Counter
import math

# Simulated system telemetry data
timing_log = [
    (100, 'cpu_load', 0.75),
    (200, 'mem_usage', 0.88),
    (300, 'cpu_load', 0.62),
    (400, 'disk_io', 0.45),
    (500, 'cpu_load', 0.91),
    (600, 'network', 0.33),
    (700, 'mem_usage', 0.79)
]

system_flags = {
    'overheat': False,
    'throttling': True,
    'legacy_mode': False,
    'secure_boot': True,
    'power_saving': False
}

# Irrelevant helper: counts event types (used nowhere critical)
def count_event_types(log):
    counter = defaultdict(int)
    for timestamp, event_type, value in log:
        counter[event_type] += 1
    return counter

# Dead function: calculates average but with wrong weighting
def faulty_average(log):
    total, count = 0, 0
    for t, et, v in log:
        if et == 'cpu_load':
            total += v * 0.5  # Incorrect weight
        else:
            total += v * 0.1
        count += 1
    return total / count if count else 0

# Misleading intermediate: looks important but unused later
cached_stats = {
    'peak': max([v for _, _, v in timing_log]),
    'valley': min([v for _, _, v in timing_log]),
    'range': None
}
cached_stats['range'] = cached_stats['peak'] - cached_stats['valley']

# Decoy transformation: operates on flags but returns dummy value
def analyze_flag_interactions(flags):
    score = 0
    if flags['overheat'] and not flags['throttling']:
        score += 10
    if not flags['secure_boot']:
        score += 25
    if flags['legacy_mode'] and flags['power_saving']:
        score -= 15
    return score * 0.1  # Not actually used

# Unused recursive countdown (red herring)
def countdown(n):
    return 1 if n <= 0 else n * countdown(n - 1)

# Real logic begins here — weighted aggregation based on event type and flag state
def extract_cpu_samples(log):
    return [v for t, et, v in log if et == 'cpu_load']

def calculate_stability_index(values):
    mean = sum(values) / len(values)
    variance = sum((v - mean) ** 2 for v in values) / len(values)
    return math.exp(-variance)  # Higher stability = lower variance

def compute_priority_weight(flags):
    weight = 1.0
    if flags['throttling']:
        weight *= 0.7
    if not flags['secure_boot']:
        weight *= 1.3
    if flags['overheat']:
        weight *= 1.5
    return weight

def detect_anomalies(log):
    anomalies = []
    for t, et, v in log:
        if et == 'cpu_load' and v > 0.85:
            anomalies.append(t)
    return anomalies

def aggregate_metrics(log, flags):
    # Step 1: Extract CPU load samples
    cpu_values = extract_cpu_samples(log)
    
    # Step 2: Calculate stability index from CPU samples
    stability = calculate_stability_index(cpu_values)
    
    # Step 3: Detect anomaly timestamps
    anomalies = detect_anomalies(log)
    anomaly_penalty = len(anomalies) * 0.05
    
    # Step 4: Compute priority weight from system flags
    priority_weight = compute_priority_weight(flags)
    
    # Step 5: Base metric from average CPU load
    base_metric = sum(cpu_values) / len(cpu_values)
    
    # Step 6: Apply stability adjustment
    adjusted_metric = base_metric * stability
    
    # Step 7: Apply anomaly penalty
    penalized_metric = adjusted_metric - anomaly_penalty
    
    # Step 8: Scale by priority weight
    final_score = penalized_metric * priority_weight
    
    # Step 9: Normalize using logarithmic scale
    final_diagnostic = math.log(1 + abs(final_score)) * 100
    
    # Return final diagnostic value
    return final_diagnostic

# Key execution point
final_diagnostic = aggregate_metrics(timing_log, system_flags)

# Print result as required
print(f"Result: {final_diagnostic}")