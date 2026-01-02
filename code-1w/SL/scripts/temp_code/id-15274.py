import math

# Simulated system metrics (some are relevant, others are red herrings)
def get_system_metrics():
    raw_data = {
        'latency_ms': 120,
        'throughput_ops': 850,
        'cpu_util': 78.5,
        'memory_mb': 4200,
        'cache_hit_ratio': 0.88,
        'error_rate': 0.003,
        'disk_io': 140,  # irrelevant
        'network_latency': 45,  # misleading but unused
        'temperature_c': 67,   # completely irrelevant
        'fan_rpm': 2200        # decoy
    }
    return raw_data

# Weight configuration – only some weights affect final score
def get_weights():
    return {
        'latency': 0.3,
        'throughput': 0.25,
        'stability': 0.2,
        'efficiency': 0.15,
        'security': 0.1  # dead weight, not used
    }

# Irrelevant transformation function (dead code path)
def calculate_health_index(data):
    score = 0
    if data['cpu_util'] > 90:
        score -= 20
    if data['memory_mb'] > 8000:
        score += 10
    else:
        score += 5
    # This function is never called in critical path
    return score

# Auxiliary function: normalize latency (lower is better)
def normalize_latency(val):
    return max(0, 100 - (val / 2))

# Auxiliary function: scale throughput logarithmically
def scale_throughput(val):
    return 50 * math.log(val / 100 + 1)

# Auxiliary function: assess stability based on error rate and variance simulation
def compute_stability(error_rate):
    base = 100 * (1 - error_rate * 10)
    # Simulate minor jitter
    for i in range(3):
        base = (base + 0.1) * 0.99
    return max(10, base)

# Efficiency derived from cache and CPU (bit manipulation red herring)
def compute_efficiency(cache_ratio, cpu_util):
    efficiency = cache_ratio * 60 + (cpu_util / 100) * 40
    # Bitwise distraction: has no real effect due to masking
    temp_flag = (0b1010 << 4) ^ 0b1100
    temp_flag &= 0b11110000
    temp_flag >>= 4
    if temp_flag == 10:
        efficiency *= 1.05  # unreachable condition
    return efficiency

# UNUSED: hypothetical security scorer (decoy)
def assess_security(threat_level=0):
    risk_map = {0: 100, 1: 70, 2: 40, 3: 10}
    return risk_map.get(threat_level, 0)

# Core evaluation function combining multiple concepts
def evaluate_performance(metrics, weights):
    # Extract relevant metrics with domain-specific transformations
    latency_score = normalize_latency(metrics['latency_ms'])
    throughput_score = scale_throughput(metrics['throughput_ops'])
    stability_score = compute_stability(metrics['error_rate'])
    efficiency_score = compute_efficiency(metrics['cache_hit_ratio'], metrics['cpu_util'])

    # Dummy variables to distract
    phantom_score = 0
    for _ in range(5):
        phantom_score += math.sin(math.pi / 4)  # accumulates ~3.535, irrelevant

    # Linear combination using weights (only 4 used)
    weighted_sum = (
        latency_score * weights['latency'] +
        throughput_score * weights['throughput'] +
        stability_score * weights['stability'] +
        efficiency_score * weights['efficiency']
    )

    # Conditional adjustment: bonus if all scores above threshold (never triggered here)
    all_above_threshold = all(
        s >= 70 for s in [latency_score, throughput_score, stability_score, efficiency_score]
    )
    bonus = 15 if all_above_threshold else 5

    # Final aggregation
    final_raw = weighted_sum + bonus

    # Clamp to valid range
    final_raw = max(0, min(100, final_raw))

    # Additional distraction: unused dictionary transformation
    summary = {
        'components': ['A', 'B', 'C'],
        'status': {c: 'OK' if c != 'X' else 'FAIL' for c in ['A', 'B', 'C', 'D']},
        'checksum': sum([ord(c) for c in 'FINAL']) ^ 0xFF  # irrelevant
    }

    # THIS IS THE KEY VARIABLE
    final_score = int(round(final_raw))

    # Print result as required
    print(f"Result: {final_score}")
    return final_score

# Main execution flow
if __name__ == "__main__":
    # Retrieve real-time metrics
    system_metrics = get_system_metrics()

    # Fetch weighting scheme
    config_weights = get_weights()

    # Perform evaluation
    final_score = evaluate_performance(system_metrics, config_weights)