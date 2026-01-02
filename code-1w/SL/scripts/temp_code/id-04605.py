import math

# Simulated system telemetry data
technical_metrics = {
    'throughput': 847.5,
    'latency_ms': 12.3,
    'error_rate': 0.0014,
    'retry_count': 3,
    'packet_loss': 0.002
}

# Irrelevant diagnostic thresholds (distractor)
diagnostic_rules = {
    'cpu_temp_limit': 85,
    'fan_speed_rpm': 3200,
    'voltage_stability': 3.3,
    'clock_drift_threshold': 0.05
}

# Benchmark configuration with meaningful parameters
benchmark_config = {
    'weight_latency': 0.4,
    'weight_throughput': 0.35,
    'weight_errors': 0.25,
    'normalization_factor': 1000,
    'enable_jitter_correction': True,
    'jitter_penalty_factor': 1.15
}

# Historical reference data (mostly irrelevant)
historical_benchmarks = [
    {'version': '1.0', 'score': 72.3},
    {'version': '1.1', 'score': 74.1},
    {'version': '1.2', 'score': 78.9},
    {'version': '1.3', 'score': 81.2}
]

# Auxiliary function that looks important but is unused (dead code path)
def compute_thermal_throttle(latency, temperature):
    if temperature > diagnostic_rules['cpu_temp_limit']:
        return latency * 1.5
    return latency

# Another decoy function with bit manipulation red herring
def apply_bitmask_correction(value, mask_bits=0b1111):
    masked = int(value * 100) & mask_bits
    return masked / 100.0

# Core processing function with nested logic
def normalize_value(raw, max_val, min_val=0):
    if raw > max_val:
        raw = max_val
    elif raw < min_val:
        raw = min_val
    return (raw - min_val) / (max_val - min_val)

# Jitter detection using modular arithmetic (relevant only if enabled)
def calculate_jitter_penalty(base_latency, history_window):
    jitter_sum = 0
    for i in range(len(history_window)):
        sample = history_window[i]
        deviation = abs(sample - base_latency)
        # Apply modulo pattern to simulate periodic interference
        if i % 3 == 0:
            deviation = (deviation * 1.1) % 5.0
        jitter_sum += deviation
    return jitter_sum / len(history_window) if history_window else 0

# Simulated recent latency samples (some used, some not)
recent_latency_samples = [12.1, 12.5, 11.9, 13.2, 12.0, 11.8, 12.4]

# Unused transformation chain (distractor)
transformed_samples = []
for sample in recent_latency_samples:
    adjusted = sample * 0.98
n    if adjusted < 12.0:
        adjusted += 0.15
    transformed_samples.append(round(adjusted, 2))

# Main evaluation logic
def evaluate_performance(metrics, config):
    # Extract relevant metrics
    raw_latency = metrics['latency_ms']
    raw_throughput = metrics['throughput']
    raw_errors = metrics['error_rate']
    
    # Normalize metrics to 0-1 scale
    norm_latency = 1 - normalize_value(raw_latency, 50.0)  # Lower latency = better
    norm_throughput = normalize_value(raw_throughput, 1000.0)
    norm_errors = 1 - normalize_value(raw_errors, 0.01)
    
    # Weighted combination
    base_score = (
        norm_latency * config['weight_latency'] +
        norm_throughput * config['weight_throughput'] +
        norm_errors * config['weight_errors']
    ) * config['normalization_factor']
    
    # Conditional jitter penalty (active branch)
    if config['enable_jitter_correction']:
        avg_jitter = calculate_jitter_penalty(raw_latency, recent_latency_samples[::2])  # Use every other sample
        jitter_penalty = avg_jitter * config['jitter_penalty_factor']
        base_score -= jitter_penalty * 2  # Penalty scaled by factor
    
    # Spurious bitwise check (looks significant but has no effect due to constant condition)
    status_flag = 0b1010
    if status_flag & 0b0001:  # Never true
        base_score *= 0.9
    
    # Additional meaningless adjustment with tuple unpacking distraction
    factors = (0.99, 1.01, 1.005)
    scaling_factor, _, _ = factors  # Only use first element
    base_score *= scaling_factor
    
    return round(base_score, 4)

# Misleading intermediate calculation (red herring)
projected_improvement = 0
for entry in historical_benchmarks:
    improvement = entry['score'] * 1.08
    if improvement > 80:
        projected_improvement += 2.5

# Critical execution point
metrics_log = {
    'latency_ms': technical_metrics['latency_ms'],
    'throughput': technical_metrics['throughput'],
    'error_rate': technical_metrics['error_rate']
}

final_score = evaluate_performance(metrics_log, benchmark_config)

# Output result as required
print(f"Result: {final_score}")