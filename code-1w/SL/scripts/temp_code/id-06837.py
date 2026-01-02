from collections import defaultdict
import math

# Simulated system performance metrics with irrelevant and relevant data
def generate_metrics():
    data = {}
    data['latency_ms'] = 120
    data['throughput_ops'] = 450
    data['error_rate'] = 0.03
    data['memory_usage_mb'] = 750
    data['cpu_temp_c'] = 68  # Irrelevant
    data['disk_reads'] = 2000  # Irrelevant
    data['network_packets'] = 15000  # Irrelevant
    data['cache_hit_ratio'] = 0.88
    data['retry_count'] = 4
    return data

# Weight configuration for scoring (only some weights affect final result)
def get_weights():
    w = defaultdict(float)
    w['latency_ms'] = -0.4
    w['throughput_ops'] = 0.3
    w['error_rate'] = -0.5
    w['cache_hit_ratio'] = 0.6
    w['retry_count'] = -0.2
    # Below are decoy weights with no corresponding metric impact
    w['cpu_temp_c'] = 0.1
    w['disk_latency'] = 0.05
    w['bandwidth_mbps'] = 0.08
    return w

# Auxiliary function – looks important but used minimally
def normalize(value, base=100):
    return value / base if base != 0 else 0

# Bit manipulation red herring – looks like it's doing optimization masking
def apply_mask(x, mask=0b1111):
    return x & mask  # Only affects low bits, misleading

# Decoy recursive function that calculates fibonacci-like sequence (unused)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

# Real scoring logic buried in distractions
def calculate_component(key, value, weight_map):
    contribution = 0.0
    if key == 'latency_ms':
        contribution = value * weight_map[key] / 10.0
    elif key == 'throughput_ops':
        contribution = (value / 100) * weight_map[key]
    elif key == 'error_rate':
        contribution = -math.log(1 + value) * 100 * weight_map[key]
    elif key == 'cache_hit_ratio':
        contribution = value * 100 * weight_map[key]
    elif key == 'retry_count':
        contribution = -(value ** 1.5) * 10 * weight_map[key]
    else:
        contribution = 0.0  # Ignore irrelevant metrics
    return contribution

# Main evaluation with conditional logic red herrings
def evaluate_performance(metrics, weights):
    score = 0.0
    bonus_applied = False
    penalty_flag = False

    # Fake complex control flow with dead branches
    temp_log = []
    for k in metrics:
        if k == 'cpu_temp_c' and metrics[k] > 70:
            penalty_flag = True
        elif k == 'disk_reads' and metrics[k] > 1000:
            temp_log.append('high_io')  # Dead code path
        elif k == 'network_packets' and metrics[k] > 10000:
            pass  # Meaningless check

    # Actual scoring loop
    for key, value in metrics.items():
        if key in weights:
            raw_contrib = calculate_component(key, value, weights)
            adjusted_contrib = raw_contrib * 1.1 if raw_contrib > 0 else raw_contrib * 0.9  # Slight asymmetry
            score += adjusted_contrib

    # Spurious bonus logic (never triggers due to conditions)
    if score > 50 and not bonus_applied:
        queue = [1, 2, 3]
        while queue:
            x = queue.pop()
            if x == 3:
                score += 5  # This block is unreachable in this input

    # Hidden threshold adjustment
    if 85 <= score < 86:
        score = round(score) + 2  # Would adjust, but not triggered

    # Final scaling based on hidden rule
    anomaly_factor = sum(1 for v in metrics.values() if isinstance(v, float) and v > 0.5)
    if anomaly_factor >= 3:
        score *= 1.05

    return score

# Misleading pre-computations
system_state = {"mode": "active", "version": 2, "debug": True}
dummy_list = [apply_mask(fib(6)) for _ in range(3)]  # Computationally wasteful

# Core execution chain
metrics = generate_metrics()
weights = get_weights()

# Critical statement
final_score = evaluate_performance(metrics, weights)

# Output result as required
print(f"Result: {final_score}")