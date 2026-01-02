def analyze_efficiency(ratio):
    if ratio > 1.5:
        return "optimal"
    elif ratio > 0.8:
        return "acceptable"
    else:
        return "poor"

status_map = {"optimal": 3, "acceptable": 2, "poor": 1}

def compute_base_value(x, y):
    temp_result = (x ** 2 + y ** 2) ** 0.5
    normalized = int(temp_result // 1)  # Floor to nearest integer
    return normalized if normalized > 0 else 1

# Simulate system performance metrics
metrics = {
    'throughput': 480,
    'latency': 120,
    'cores_used': 6,
    'peak_utilization': 94.5,
    'downtime_events': 3
}

bonus_multiplier = 1.0
core_efficiency = metrics['throughput'] / (metrics['cores_used'] * 20)

# Distractor: irrelevant string processing
system_tag = f"SYS-{metrics['downtime_events'] * 10}"
diagnostic_code = system_tag.lower().replace('-', '_').upper()  # No effect

# Conditional bonus logic with red herring variables
if core_efficiency > 1.5:
    bonus_multiplier += 0.3
elif core_efficiency > 1.0:
    bonus_multiplier += 0.15
else:
    adjustment = 0.05  # Dead code path, never used

# String-based switch emulation (semi-relevant)
latency_status = "optimal" if metrics['latency'] < 100 else "acceptable" if metrics['latency'] < 150 else "poor"
efficiency_class = analyze_efficiency(core_efficiency)

# Irrelevant list construction
historical_bonuses = [1.0, 1.15, 1.0, 1.3, 1.15]
cumulative_avg = sum(historical_bonuses) / len(historical_bonuses)  # Computed but unused

base_score = compute_base_value(metrics['throughput'], metrics['latency'])

# Multi-factor score computation with distractors
status_value = status_map[efficiency_class]
latency_penalty = 0
if metrics['downtime_events'] > 0:
    latency_penalty = metrics['downtime_events'] * 2

# Key logic chain
raw_performance = base_score * status_value - latency_penalty

# Another distractor: complex string formatting with no impact
report_summary = f"Performance: {raw_performance:.1f}, Status: {efficiency_class.upper()}"
summary_length = len(report_summary)  # Used only here
size_flag = "long" if summary_length > 50 else "short"

# Final adjustment based on conditional expression
final_score = raw_performance * bonus_multiplier
final_score = final_score + 10 if 'optimal' in [efficiency_class, latency_status] else final_score - 5

Result: {final_score}