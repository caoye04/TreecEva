import itertools

# Simulated system telemetry data
telemetry_stream = [15, 23, 42, 19, 8, 31, 44, 12]

# Irrelevant constants for signal interference
MAX_BUFFER_SIZE = 1024
DEFAULT_TIMEOUT = 30
DEBUG_MODE = False

# Benchmark thresholds (only some are actually used)
benchmarks = {
    'latency_ms': 25,
    'throughput_tps': 40,
    'error_rate': 0.05,
    'cache_hit_ratio': 0.85,
    'retry_count': 3
}

# Distractor: unused function that looks important
def analyze_network_health(data):
    total = sum(x ** 0.5 for x in data if x > 20)
    return round(total, 2)

# Another red herring: complex-looking but unused transformation
turbulence_factors = [x ^ (i % 7) for i, x in enumerate(telemetry_stream)]
smoothed_data = [sum(telemetry_stream[:i+1]) / (i+1) for i in range(len(telemetry_stream))]

# Decoy statistic computation
aggregate_metric = max(smoothed_data) * min(turbulence_factors) // 2 if turbulence_factors else 0

# Real processing begins here
metric_data = {
    'response_times': [x for x in telemetry_stream if x >= 20],
    'failures': [x for x in telemetry_stream if x < 15],
    'retries': len([x for x in telemetry_stream if x % 3 == 0])
}

# Misleading intermediate calculation
baseline_shift = sum(itertools.accumulate([2, 4, 6])) // 3  # equals 6

# Secondary decoy: circular logic with no impact
current_state = {'status': 1}
for _ in range(3):
    current_state['status'] ^= 1

# Actual core logic buried in distractions
def compute_efficiency(values, base):
    if not values:
        return 0
    avg = sum(values) / len(values)
    peak = max(values)
    score = (avg / base) * (1 + (peak - avg) / (avg + 1))
    return score

def adjust_for_retries(raw_score, retry_count, limit):
    if retry_count > limit:
        return raw_score * 0.85
    return raw_score

# Distractor dictionary with fake metrics
auxiliary_metrics = {
    'jitter': sum(x % 5 for x in telemetry_stream),
    'stability_index': len(list(itertools.groupby(smoothed_data)))
}

# Function that appears critical but contains both relevant and irrelevant parts
def evaluate_performance(metrics, config):
    # Extract relevant components
    times = metrics.get('response_times', [])
    failures = metrics.get('failures', [])
    retry_count = metrics.get('retries', 0)
    
    # Irrelevant pre-checks
    if len(failures) > config['retry_count']:
        pass  # dead logic branch
    
    # Real scoring path
    base_latency = config['latency_ms']
    efficiency = compute_efficiency(times, base_latency)
    
    # Adjustment based on retries
    adjusted_score = adjust_for_retries(efficiency, retry_count, config['retry_count'])
    
    # Final scaling - only this matters
    final_value = int(round(adjusted_score * 100))
    
    # Red herring: unused assignment
    diagnostic_trace = {k: v for k, v in config.items() if v > 10}
    
    return final_value

# Key execution point
final_score = evaluate_performance(metric_data, benchmarks)

# Output required format
print(f"Result: {final_score}")