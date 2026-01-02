def analyze_efficiency(logs):
    total_entries = len(logs)
    valid_count = sum(1 for entry in logs if 'ERROR' not in entry)
    error_rate = (total_entries - valid_count) / total_entries if total_entries > 0 else 0
    efficiency = (valid_count * 1.5) / total_entries if total_entries > 0 else 0
    return efficiency, error_rate

logs_data = [
    'INFO: system started',
    'DEBUG: memory allocated',
    'ERROR: disk failure',
    'INFO: retrying connection',
    'WARN: high latency',
    'INFO: operation complete'
]

# Simulate historical benchmark (irrelevant but plausible)
historical_avg = 0.82
weight_factor = 0.9
projected_gain = (historical_avg * weight_factor) + 0.05

productivity, risk_factor = analyze_efficiency(logs_data)

# Distractor: unused metrics
temp_diagnostic = [x.upper() for x in logs_data if 'D' in x]
placeholder_sum = sum(len(item) for item in temp_diagnostic)
shadow_metric = placeholder_sum * 0.1 if temp_diagnostic else 0

scaling_constant = 100
calibration_offset = 5

intermediate_result = productivity * scaling_constant
penalty_adjustment = 10 if risk_factor > 0.1 else 0

# Key computation with mild interference
adjustment_factor = 1 - risk_factor
raw_score = intermediate_result * adjustment_factor - penalty_adjustment

# Final evaluation using conditional expression
final_score = raw_score + calibration_offset if raw_score > 70 else raw_score - 20

# Additional red herring: complex string manipulation with no impact
delimited_trace = '|'.join([item.split(':')[0] for item in logs_data])
trace_checksum = sum(ord(c) % 5 for c in delimited_trace)

Result: {final_score}