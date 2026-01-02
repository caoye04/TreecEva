import math

# Simulated system health monitoring and performance evaluation

def monitor_system_load(timestamp):
    return (timestamp * 0.73) % 100 + 5

def calculate_latency(base, multiplier=1.2):
    return base * multiplier + 3.7

def analyze_trend(data_points):
    trend = 0
    for i in range(1, len(data_points)):
        trend += data_points[i] - data_points[i-1]
    return trend / len(data_points)

def dummy_analysis(payload):
    # Dead function - never used in actual computation
    result = 0
    for k in payload:
        result += len(k) * payload[k]
    return result ** 0.5

def generate_placeholder_data(keys):
    # Irrelevant data generation
    return {k: len(k) * 17 for k in keys}

def adjust_for_noise(value, level=0.94):
    return value * level + (level * 5)

def compute_entropy(sequence):
    # Unused complex calculation
    freq = {}
    for item in sequence:
        freq[item] = freq.get(item, 0) + 1
    entropy = 0
    for f in freq.values():
        p = f / len(sequence)
        entropy -= p * math.log(p)
    return entropy

def validate_thresholds(config, readings):
    # Misleading function that looks important but doesn't affect final result
    alerts = []
    for key in config:
        if key in readings:
            if readings[key] > config[key].get('max', 100):
                alerts.append(f"{key}_high")
            elif readings[key] < config[key].get('min', 0):
                alerts.append(f"{key}_low")
    return len(alerts) == 0

def normalize_metrics(raw):
    normalized = {}
    total = sum(raw.values())
    for k, v in raw.items():
        normalized[k] = v / total * 100
    return normalized

def filter_outliers(data, factor=1.5):
    # Not actually used in final path
    median = sorted(data.values())[len(data)//2]
    filtered = {}
    for k, v in data.items():
        if abs(v - median) <= factor * median:
            filtered[k] = v
    return filtered

def derive_stability_index(values):
    variance = sum([(v - sum(values)/len(values))**2 for v in values]) / len(values)
    return 100 / (1 + variance)

def evaluate_performance(log, config):
    # Core logic embedded within distractions
    base_score = 0
    
    # Extract relevant metrics
    cpu_usage = log.get('cpu_util', 0)
    mem_pressure = log.get('mem_load', 0)
    io_efficiency = log.get('disk_io', 50)
    network_jitter = log.get('net_jitter', 0)
    
    # Real computation begins
    adjusted_cpu = max(0, 100 - cpu_usage)  # Invert usage
    penalty = 0
    
    if mem_pressure > 80:
        penalty += 15
    elif mem_pressure > 60:
        penalty += 8
    
    if network_jitter > 25:
        penalty += 12 * (network_jitter / 100)
    
    throughput_score = io_efficiency * 1.8
    
    # Combine scores before penalty
    base_score = adjusted_cpu + throughput_score
    
    # Apply non-linear transformation
    if base_score > 120:
        base_score = 120 + (base_score - 120) * 0.4
    
    # Final score with penalty
    final_raw = base_score - penalty
    
    # Additional adjustment based on config policy
    scaling_factor = config.get('policy', {}).get('scaling', 1.0)
    drift_correction = config.get('calibration', 0)
    
    # Only scaling_factor is actually applied; drift_correction is a red herring
    final_adjusted = final_raw * scaling_factor
    
    # Distractor: unused derived metrics
    auxiliary_metrics = {
        'entropy': compute_entropy([int(cpu_usage), int(mem_pressure)]),
        'trend': analyze_trend([cpu_usage, mem_pressure, io_efficiency]),
        'stability': derive_stability_index([adjusted_cpu, throughput_score])
    }
    
    # Final clamping
    return max(10, min(200, final_adjusted))

# Main execution flow
if __name__ == "__main__":
    # Timestamp simulation
    ts = 12345
    load = monitor_system_load(ts)
    latency = calculate_latency(load, 1.1)

    # Real input data
    metrics_log = {
        'cpu_util': 68,
        'mem_load': 72,
        'disk_io': 64,
        'net_jitter': 32,
        'temp_sensor': 45,  # Irrelevant field
        'power_draw': 89   # Irrelevant field
    }

    # Benchmark configuration with decoy entries
    benchmark_config = {
        'policy': {
            'scaling': 1.25  # This affects result
        },
        'thresholds': {
            'cpu_util': {'max': 90},
            'mem_load': {'max': 75}  # Triggers no action
        },
        'calibration': 4.3,  # Red herring - not used
        'version': '2.1'  # Unused metadata
    }

    # Generate irrelevant auxiliary data
    placeholders = generate_placeholder_data(['A', 'B', 'C'])
    dummy_payload = {'test': 100, 'data': 200}
    dummy_result = dummy_analysis(dummy_payload)

    # Normalize real metrics (used)
    normalized_metrics = normalize_metrics(metrics_log)

    # Validate thresholds (called but doesn't affect final_score)
    health_status = validate_thresholds(benchmark_config['thresholds'], metrics_log)

    # Noise adjustment on latency (irrelevant)
    noisy_latency = adjust_for_noise(latency)

    # Critical statement
    final_score = evaluate_performance(metrics_log, benchmark_config)
    
    # Output result
    print(f"Result: {final_score}")