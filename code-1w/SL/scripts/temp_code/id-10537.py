from collections import Counter, defaultdict
import math

# Simulated system telemetry data
timestamps = [1623456780, 1623456789, 1623456795, 1623456801, 1623456810]
raw_logs = [
    'INFO: CPU=75%, MEM=82%',
    'WARN: CPU=88%, DISK=91%',
    'ERROR: NETWORK timeout',
    'INFO: CPU=60%, MEM=75%',
    'CRITICAL: CPU=95%, TEMP=high'
]

# Irrelevant preprocessing - red herring
hash_sum = sum(hash(entry) % 100 for entry in raw_logs)
offset_map = {i: hash_sum * (i + 1) // 2 for i in range(5)}

# Distractor: unused function
def analyze_bandwidth(data):
    return sum(len(d) for d in data) / len(data)

# Misleading intermediate aggregation
temp_aggregate = defaultdict(int)
for i, log in enumerate(raw_logs):
    temp_aggregate['entries'] += 1
    temp_aggregate['chars'] += len(log)
    if 'ERROR' in log:
        temp_aggregate['errors'] += 1

# Real processing begins here
log_entries = []
for log in raw_logs:
    metrics = {}
    if 'CPU=' in log:
        start = log.find('CPU=') + 4
        end = log.find('%', start)
        try:
            metrics['cpu'] = int(log[start:end])
        except ValueError:
            metrics['cpu'] = 0
    if 'MEM=' in log:
        start = log.find('MEM=') + 4
        end = log.find('%', start)
        try:
            metrics['mem'] = int(log[start:end])
        except ValueError:
            metrics['mem'] = 0
    log_entries.append(metrics)

# System state with decoy values
system_state = {
    'uptime': 12780,
    'cores': 8,
    'thresholds': {
        'cpu_high': 90,
        'mem_high': 80,
        'temp_warn': 75
    },
    'weights': [0.3, 0.5, 0.7],  # unused distraction
    'mode': 'performance'
}

# Distractor: complex but unused calculation
correlation_score = 0
for i in range(len(timestamps) - 1):
    delta_t = timestamps[i+1] - timestamps[i]
    jitter = abs(delta_t - 9)
    correlation_score += math.sin(jitter) * hash_sum

# Another dead-end analysis
snapshot_frequencies = Counter()
for ts in timestamps:
    second = ts % 60
    snapshot_frequencies[second // 10] += 1

# Core logic hidden among distractions
def evaluate_stability(metrics_list, state):
    score = 100.0
    penalty_per_event = 5.0
    
    # Track occurrences using Counter (required feature)
    event_counter = Counter()
    
    for metrics in metrics_list:
        if 'cpu' in metrics:
            if metrics['cpu'] > state['thresholds']['cpu_high']:
                event_counter['cpu_over'] += 1
            elif metrics['cpu'] > 80:
                event_counter['cpu_elevated'] += 1

        if 'mem' in metrics:
            if metrics['mem'] > state['thresholds']['mem_high']:
                event_counter['mem_high'] += 1

    # Apply penalties
    score -= event_counter['cpu_over'] * 12.5
    score -= event_counter['cpu_elevated'] * 4.0
    score -= event_counter['mem_high'] * 6.0
    
    # Conditional expression distraction (not affecting final result)
    fallback_mode = 'recovery' if score < 60 else 'normal'
    adjustment = 10 if fallback_mode == 'normal' else 0  # not applied
    
    # Hidden normalization step
    if len(metrics_list) > 0:
        avg_cpu = sum(m.get('cpu', 0) for m in metrics_list) / len(metrics_list)
        if avg_cpu > 85:
            score -= 8.5  # additional penalty
    
    return score

# Secondary processing path - looks important but unused
historical_trend = []
for entry in log_entries:
    if 'cpu' in entry:
        normalized = entry['cpu'] / 100.0
        smoothed = math.log(1 + normalized * 10)  # irrelevant transform
        historical_trend.append(smoothed)

# Actual key function with multiple concepts
state_flags = set()
flag_weights = {'critical': 10, 'warning': 5, 'info': 1}  # unused tuple-like distractor

# Main diagnostic processor
def process_metrics(entries, sys_state):
    # Use of defaultdict as required
    severity_count = defaultdict(int)
    total_cpu_load = 0
    valid_cpu_count = 0
    
    for entry in entries:
        if 'cpu' in entry:
            total_cpu_load += entry['cpu']
            valid_cpu_count += 1
            
            if entry['cpu'] > 90:
                severity_count['critical'] += 1
            elif entry['cpu'] > 75:
                severity_count['elevated'] += 1

    # Compute average only if data exists
    avg_cpu = total_cpu_load / valid_cpu_count if valid_cpu_count > 0 else 0
    
    # Determine base health from CPU distribution
    health_modifier = 0
    health_modifier += severity_count['critical'] * -15
    health_modifier += severity_count['elevated'] * -5
    
    # Additional factor: memory presence heuristic
    mem_present_count = sum(1 for e in entries if 'mem' in e)
    if mem_present_count >= 3:
        health_modifier -= 3  # slight penalty for sustained high monitoring
    
    # Final diagnostic computed through layered logic
    base_score = 100 + health_modifier
    
    # Conditional expression that actually matters
    final_adjustment = -10 if avg_cpu > 88 else (-5 if avg_cpu > 80 else 0)
    
    result = base_score + final_adjustment
    
    # Dead code branch - never reached due to prior logic
    if result > 150:
        result = 150  # clamping - unreachable
    elif result < 0:
        result = 0   # clamping - unreachable
    
    return round(result, 4)

# Key statement execution point
final_diagnostic = process_metrics(log_entries, system_state)

# Print result as required
print(f"Target result: {final_diagnostic}")