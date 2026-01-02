from collections import defaultdict, Counter
import math

# Simulated system metrics from a distributed logging framework
timestamps = [1623456780, 1623456789, 1623456795, 1623456801, 1623456810]
raw_logs = [
    'INFO: Server started on port 8080',
    'ERROR: Database connection timeout',
    'WARNING: High memory usage detected',
    'INFO: User login successful',
    'CRITICAL: Disk space below 5%'
]

# Irrelevant processing: parsing logs for no real purpose (red herring)
log_levels = []
for log in raw_logs:
    if 'CRITICAL' in log:
        log_levels.append('CRITICAL')
    elif 'ERROR' in log:
        log_levels.append('ERROR')
    elif 'WARNING' in log:
        log_levels.append('WARNING')
    else:
        log_levels.append('INFO')

distinct_levels = set(log_levels)
level_count = dict(Counter(log_levels))

# Decoy function: never actually used but looks important
def analyze_failure_rate(logs):
    errors = 0
    for entry in logs:
        if 'ERROR' in entry or 'CRITICAL' in entry:
            errors += 1
    return errors / len(logs) if logs else 0

# Another decoy: complex timestamp diff analysis (unused)
time_diffs = []
for i in range(1, len(timestamps)):
    time_diffs.append(timestamps[i] - timestamps[i-1])

avg_interval = sum(time_diffs) / len(time_diffs) if time_diffs else 0
spike_count = sum(1 for diff in time_diffs if diff > 5)

# Real data structure: performance metrics (core of actual logic)
metrics = {
    'latency_ms': 125,
    'throughput_ops': 480,
    'error_rate': 0.035,
    'memory_util': 0.78,
    'cpu_load': 0.65
}

# Weight configuration map (used in final calculation)
weights = defaultdict(float)
weights['latency_ms'] = -0.4
weights['throughput_ops'] = 0.35
weights['error_rate'] = -0.5
weights['memory_util'] = -0.2
weights['cpu_load'] = -0.15

# Bit manipulation red herring: simulates 'encoding' but irrelevant
encoded_flags = 0
for key in metrics:
    if 'ops' in key:
        encoded_flags |= (1 << 3)
    if 'error' in key:
        encoded_flags ^= (1 << 5)
    if 'latency' in key:
        encoded_flags &= ~((1 << 2) | (1 << 1))

# Fake normalization chain (looks useful, not used)
normalized = {}
for k, v in metrics.items():
    if k == 'latency_ms':
        normalized[k] = round(1 / (1 + math.exp(-v/100)), 3)
    elif 'ops' in k:
        normalized[k] = min(v / 1000, 1.0)
    else:
        normalized[k] = 1 - v

# Unused conditional block with misleading print (dead path)
current_status = 'OPTIMAL'
if metrics['error_rate'] > 0.05:
    current_status = 'DEGRADED'
elif metrics['memory_util'] > 0.9:
    current_status = 'CRITICAL'
else:
    temp_flag = (encoded_flags >> 4) & 1
    if temp_flag:
        current_status = 'MONITORING'
    # This branch does nothing relevant

# Core evaluation function (only this matters)
def evaluate_performance(met, wgt):
    score = 0.0
    contributions = defaultdict(float)
    
    # Real scoring logic buried in distractions
    for metric_name, value in met.items():
        weight = wgt[metric_name]
        
        # Apply non-linear penalty for latency beyond threshold
        if metric_name == 'latency_ms':
            base = value
            if base > 100:
                base = 100 + (base - 100) ** 0.5 * 10  # sqrt penalty
            contributions[metric_name] = base * weight
        
        # Throughput bonus with diminishing returns
        elif metric_name == 'throughput_ops':
            capped_throughput = min(value, 600)
            efficiency = capped_throughput / 600
            contributions[metric_name] = (efficiency ** 0.5) * value * weight
        
        # Error rate: exponential penalty
        elif metric_name == 'error_rate':
            penalty_factor = math.exp(value * 10)
            contributions[metric_name] = value * penalty_factor * weight
        
        # Resource utilization: linear weighted deduction
        else:
            contributions[metric_name] = value * weight
    
    # Aggregate final score
    total_contribution = sum(contributions.values())
    adjusted_score = 100 + total_contribution  # Base score 100
    
    # Final adjustment using bitwise artifact (distraction but harmless)
    flag_adjust = (encoded_flags ^ 0xAA) & 0x0F
    if flag_adjust > 0:
        adjusted_score -= flag_adjust * 0.25  # minor numeric noise
    
    return round(adjusted_score, 6)

# Execute main logic
final_score = evaluate_performance(metrics, weights)

# Print result as required
print(f"Target result: {final_score}")