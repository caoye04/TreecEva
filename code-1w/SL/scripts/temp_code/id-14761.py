import math

# Simulated system telemetry data
technical_metrics = {
    'latency_ms': 120,
    'throughput_rps': 850,
    'error_rate': 0.012,
    'cpu_utilization': 0.78,
    'memory_mb': 1920
}

# Business KPIs (irrelevant to final computation but plausible distractors)
business_kpis = {
    'customer_satisfaction': 0.87,
    'revenue_growth': 0.15,
    'churn_rate': 0.03,
    'support_tickets': 47
}

# Baseline thresholds for evaluation
baseline = {
    'latency_ms': 100,
    'throughput_rps': 1000,
    'error_rate': 0.01,
    'cpu_utilization': 0.80
}

# Irrelevant transformation: encode metrics into hex (dead code path)
def encode_metrics(metrics):
    return {k: hex(int(v * 100)) if isinstance(v, float) else hex(v) for k, v in metrics.items()}

coded_tech = encode_metrics(technical_metrics)  # Unused later

coded_business = encode_metrics(business_kpis)  # Completely irrelevant

# Decoy function that looks important but isn't used
def calculate_health_index(data):
    weight_map = {'latency_ms': 0.3, 'throughput_rps': 0.25, 'error_rate': 0.35, 'cpu_utilization': 0.1}
    total = 0
    for k, w in weight_map.items():
        total += (1 - data[k] / (data[k] + 1)) * w  # Nonsensical normalization
    return round(total * 100, 2)

# Another decoy: complex bit manipulation on unrelated values
def analyze_stability_flags(metrics):
    flag = 0
    flag |= (1 if metrics['latency_ms'] < 150 else 0) << 3
    flag |= (1 if metrics['error_rate'] < 0.02 else 0) << 2
    flag |= (1 if metrics['cpu_utilization'] < 0.85 else 0) << 1
    flag |= (1 if metrics['throughput_rps'] > 800 else 0)
    # Extract only middle bits
    extracted = (flag >> 1) & 0b11
    return extracted * 17  # Arbitrary scaling, not used

stability_code = analyze_stability_flags(technical_metrics)  # Computed but unused

# Real processing begins here — metric adjustment with modular arithmetic
def adjust_value(value, threshold, method='additive'):
    if method == 'additive':
        return abs(value - threshold) * 100
    elif method == 'multiplicative':
        return (max(value, threshold) / min(value, threshold)) * 50
    else:
        return 0

# Secondary helper — only some branches are relevant
def normalize_component(val, max_val):
    if val <= 0:
        return 0.0
    result = math.log(val) / math.log(max_val)  # Logarithmic normalization
    if result > 1:  # Clamp to [0,1]
        return 1.0
    return max(result, 0.0)

# Core evaluation logic (only this affects final_score)
def evaluate_performance(metrics, base):
    score = 100.0  # Initial perfect score

    # Deviation penalties using modular arithmetic and conditional branching
    latency_dev = adjust_value(metrics['latency_ms'], base['latency_ms'], 'additive')
    score -= latency_dev * 0.05

    throughput_dev = adjust_value(metrics['throughput_rps'], base['throughput_rps'], 'multiplicative')
    score -= throughput_dev * 0.03

    error_dev = adjust_value(metrics['error_rate'], base['error_rate'], 'additive')
    score -= error_dev * 0.8

    # Conditional cpu bonus/penalty
    if metrics['cpu_utilization'] < base['cpu_utilization']:
        score += 5  # Efficient resource use bonus
    else:
        score -= 3  # Overuse penalty

    # Final nonlinear adjustment based on composite deviation
    total_deviation = latency_dev + throughput_dev + error_dev
    if total_deviation < 50:
        score += 10
    elif total_deviation < 100:
        score += 5
    else:
        score -= normalize_component(total_deviation, 200) * 15

    return round(score, 6)

# Execution point of interest
metric_data = {
    k: technical_metrics[k]
    for k in ['latency_ms', 'throughput_rps', 'error_rate', 'cpu_utilization']
}

final_score = evaluate_performance(metric_data, baseline)
print(f"Target result: {final_score}")