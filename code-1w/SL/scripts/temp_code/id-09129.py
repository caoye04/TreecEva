import math

# Simulated system telemetry data
telemetry_stream = [
    {'cpu': 78, 'mem': 82, 'io': 45, 'latency': 120, 'timestamp': 1001},
    {'cpu': 65, 'mem': 70, 'io': 52, 'latency': 98, 'timestamp': 1002},
    {'cpu': 90, 'mem': 95, 'io': 30, 'latency': 210, 'timestamp': 1003},
    {'cpu': 45, 'mem': 60, 'io': 60, 'latency': 75, 'timestamp': 1004}
]

# Irrelevant baseline thresholds (distractor)
baseline_thresholds = {
    'temperature': 75,
    'fan_speed': 2000,
    'power_draw': 150,
    'voltage': 1.2
}

# Benchmark configuration with red herring entries
benchmark_config = {
    'weights': {'response_time': 0.4, 'throughput': 0.3, 'stability': 0.2, 'efficiency': 0.1},
    'scaling_factor': 1.5,
    'decay_rate': 0.9,
    'max_latency_cap': 200,
    'irrelevant_flags': ['LOGGING_DISABLED', 'DEBUG_MODE_OFF', 'ENCRYPTION_ACTIVE']
}

# Historical anomaly records (unused - dead data path)
anomaly_registry = {
    'severe': [],
    'moderate': [{'ts': 998, 'type': 'spike'}, {'ts': 980, 'type': 'drop'}],
    'resolved': 12
}

# Auxiliary function that is never called (decoy)
def calculate_thermal_pressure(temp, duration):
    if duration < 60:
        return temp * 0.8
    else:
        return temp * math.log(duration)

# Data transformation pipeline with intermediate distractors
def preprocess_telemetry(raw_data):
    processed = []
    total_load = 0  # misleading accumulator
    peak_memory = 0
    for entry in raw_data:
        load = entry['cpu'] * 0.6 + entry['mem'] * 0.4
        total_load += load
        if entry['mem'] > peak_memory:
            peak_memory = entry['mem']
        # Compute derived metrics
        efficiency_score = (entry['cpu'] + entry['io']) / 2 if entry['latency'] < 150 else 0
        response_penalty = max(0, entry['latency'] - 50) * 0.1
        processed.append({
            'load': load,
            'efficiency': efficiency_score,
            'penalty': response_penalty,
            'timestamp': entry['timestamp']
        })
    avg_load = total_load / len(raw_data) if raw_data else 0
    # Fake normalization (not used later)
    normalized = [{'norm_val': p['load'] / (avg_load + 1e-5)} for p in processed]
    return processed

# Core evaluation logic with key computation buried in noise
def evaluate_performance(metrics_log, config):
    weights = config['weights']
    scaling = config['scaling_factor']
    decay = config['decay_rate']
    
    cumulative = {'response_time': 0, 'throughput': 0, 'stability': 0, 'efficiency': 0}
    count = 0
    temporal_weight = 1.0
    
    # Reverse iteration to simulate time decay (key logic)
    for record in reversed(metrics_log):
        cumulative['response_time'] += (1 / (record['penalty'] + 1)) * temporal_weight
        cumulative['throughput'] += record['efficiency'] * temporal_weight
        cumulative['efficiency'] += (100 - record['penalty']) * temporal_weight
        cumulative['stability'] += (100 - abs(record['load'] - 70)) * temporal_weight
        
        temporal_weight *= decay  # decaying influence over time
        count += 1
    
    # Normalize by weighted count
    total_weight = sum(decay**i for i in range(count))
    for k in cumulative:
        cumulative[k] /= total_weight
    
    # Apply weighting schema (critical step)
    final_value = 0
    for metric, weight in weights.items():
        final_value += cumulative[metric] * weight
    
    # Scaling applied once
    final_value *= scaling
    
    # Spurious adjustment based on unused config field (red herring)
    if 'max_latency_cap' in config and config['max_latency_cap'] > 150:
        final_value += 5.0  # minor boost
    
    # Dead branch: this condition is never true in current data
    if any('CRITICAL' in flag for flag in config.get('irrelevant_flags', [])):
        final_value -= 20
    
    # Final non-linear transformation
    final_value = math.tanh(final_value / 50) * 50 + final_value
    
    return int(round(final_value))

# Secondary processing chain (never invoked - distraction)
def generate_diagnostic_report(data):
    report = {"issues": []}
    for d in data:
        if d['cpu'] > 85 and d['mem'] > 90:
            report['issues'].append(f"High stress at {d['timestamp']}")
    return report

# Unused utility for bit manipulation (irrelevant)
def pack_status_code(cpu, mem):
    return ((cpu & 0xFF) << 8) | (mem & 0xFF)

# Main execution flow
processed_metrics = preprocess_telemetry(telemetry_stream)

# Dummy dictionary update (side effect with no impact)
stats_summary = {}
for m in processed_metrics:
    ts = m['timestamp']
    stats_summary[ts] = {'adjusted_load': m['load'] * 1.05}

# Critical statement
final_score = evaluate_performance(processed_metrics, benchmark_config)

# Superfluous sorting (no effect on result)
sorted_summary = sorted(stats_summary.items(), key=lambda x: x[0])

# Output result as required
print(f"Result: {final_score}")