import math

# Simulated system health metrics (some relevant, some not)
metrics = {
    'response_time_ms': 142,
    'cpu_load': 0.78,
    'memory_usage_mb': 3840,
    'request_throughput': 235,
    'error_rate': 0.012,
    'retry_count': 5,
    'timeout_count': 3,
    'cache_hit_ratio': 0.88,
    'disk_io_ops': 1200,
    'network_latency_ms': 21
}

# Irrelevant baseline thresholds (distractor data)
baseline_thresholds = {
    'temperature_c': 45,
    'fan_rpm': 3200,
    'power_draw_w': 180,
    'uptime_hours': 732
}

# Decoy function – looks important but unused in final calculation
def analyze_stability(data):
    score = 0
    if data['cpu_load'] < 0.8:
        score += 20
    if data['memory_usage_mb'] < 4096:
        score += 15
    if data['disk_io_ops'] > 1000:
        score += 10
    return score + len(data)  # red herring computation

# Another decoy: complex transformation with no impact
def transform_metrics(raw):
    transformed = {}
    for k, v in raw.items():
        if 'ms' in k:
            transformed[k] = max(1, int(math.log(v) * 10))
        elif 'rate' in k:
            transformed[k] = round(100 * (1 - v), 2)
        else:
            transformed[k] = v // 10 if isinstance(v, (int, float)) else v
    return {key.upper(): val for key, val in transformed.items()}

# Real evaluation logic buried among distractions
def evaluate_performance(data, standard):
    # Extract relevant KPIs
    rt = data['response_time_ms']
    tp = data['request_throughput']
    er = data['error_rate']
    ch = data['cache_hit_ratio']

    # Hidden formula: weighted combination with nonlinear components
    time_penalty = 100 * (math.log(rt / 100) if rt > 100 else 0)
    throughput_bonus = 0.25 * (tp - 200) if tp > 200 else -10
    error_penalty = 50 * math.pow(er, 0.5)
    cache_efficiency = 20 * (ch - 0.8) if ch > 0.8 else -15

    # Distractor variables - look like they're used but aren't
    load_factor = data['cpu_load'] * 100
    memory_pressure = 4096 - data['memory_usage_mb']
    retry_ratio = data['retry_count'] / (data['request_throughput'] or 1)

    # Core scoring logic
    raw_score = 50 + time_penalty + throughput_bonus + error_penalty + cache_efficiency

    # Additional smokescreen: conditional that never triggers due to data
    if data.get('missing_safety_check', False):
        raw_score -= 100  # dead code path

    # Normalize score using modular arithmetic twist
    normalized = (raw_score * 7) % 89

    # Final adjustment based on bitwise inspection of throughput
    if tp & 1:  # odd throughput?
        normalized += 3

    return int(normalized)

# Unused lambda - misleading functional style hint
data_enhancer = lambda x: {k: v * 1.1 for k, v in x.items() if isinstance(v, (int, float))}

# Benchmark configuration (looks configurable but fixed)
benchmark = {
    'target_throughput': 250,
    'max_latency': 150,
    'min_cache_hit': 0.9
}

# Dead code block - linear search for irrelevant condition
outliers = []
for key, value in metrics.items():
    if isinstance(value, (int, float)) and value > 1000 and 'ms' not in key:
        outliers.append(key)  # computed but never used

# Key execution point
final_score = evaluate_performance(metrics, benchmark)

# Print result as required
print(f"Target result: {final_score}")