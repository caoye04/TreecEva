def analyze_efficiency(metrics):
    adjusted_metrics = {}
    for k, v in metrics.items():
        if 'time' in k:
            adjusted_metrics[k] = v * 1.1
        elif 'error' in k:
            adjusted_metrics[k] = max(v - 5, 0)
        else:
            adjusted_metrics[k] = v
    return adjusted_metrics

metrics_data = {
    'processing_time': 85,
    'error_rate': 12,
    'throughput': 200,
    'latency_ms': 45
}

# Distractor: Unused alternative calculation path
baseline_adjustment = sum([v for v in metrics_data.values() if v > 50]) // 3

adjusted_data = analyze_efficiency(metrics_data)

productivity = 0
if adjusted_data['processing_time'] < 90:
    productivity += 30
if adjusted_data['error_rate'] < 10:
    productivity += 25
if 'throughput' in adjusted_data and adjusted_data['throughput'] > 180:
    productivity += 45

# Simulate risk factor with bitwise interference (modular behavior)
def compute_risk_factor(x, y):
    temp_a = (x ^ y) & 15
    temp_b = (x + y) % 7
    debug_flag = False  # unused but plausible
    return (temp_a * 2) - temp_b

risk_factor = compute_risk_factor(adjusted_data['latency_ms'], len(adjusted_data))

# Secondary distractor: complex string-based validation that doesn't affect outcome
critical_codes = ['ERR_01', 'TIMEOUT_X', 'CRC_FAIL']
flagged_issues = [c.lower() for c in critical_codes if 'ERR' in c]
diagnostic_log = "System check: " + ", ".join(flagged_issues)

# Core evaluation logic
status_weights = {'high': 1.5, 'medium': 1.0, 'low': 0.7}
raw_status = productivity / 100.0
status_key = 'low'
if raw_status >= 0.9:
    status_key = 'high'
elif raw_status >= 0.6:
    status_key = 'medium'

weighted_productivity = productivity * status_weights[status_key]

# Final computation with conditional adjustment
def evaluate_performance(p, r):
    base = p - r * 2
    if r < 10:
        bonus = 10
        extra_buffer = (p // 10) % 4  # computed but not used
        return base + bonus
    return base

final_score = evaluate_performance(productivity, risk_factor)

print(f"Result: {final_score}")