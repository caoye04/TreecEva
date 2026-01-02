def analyze_component_health(sensor_data, threshold=0.75):
    # Irrelevant health scoring with red herring logic
    baseline = sum([x * 0.1 for x in sensor_data if x > 0.5])
    anomalies = [i for i, x in enumerate(sensor_data) if x < 0.3]
    penalty = len(anomalies) * 0.2 if baseline < 1.0 else 0.0
    return (baseline - penalty) * 1.5


def compute_bandwidth_efficiency(payloads):
    # Distractor: network efficiency calculation (unused later)
    total_chars = sum(len(p) for p in payloads)
    compressed = ''.join([p.lower().replace(' ', '') for p in payloads])
    unique = len(set(compressed))
    efficiency = unique / total_chars if total_chars > 0 else 0
    return efficiency * 100

# Simulated system telemetry
telemetry_stream = [
    'ERROR:HALT', 'INFO:OK', 'WARN:FLUX', 'INFO:OK', 'DEBUG:SPIN',
    'INFO:OK', 'INFO:OK', 'WARN:FLUX', 'INFO:OK'
]

# Parse status counts - relevant only in part
status_count = {}
for entry in telemetry_stream:
    level = entry.split(':')[0]
    status_count[level] = status_count.get(level, 0) + 1

info_count = status_count.get('INFO', 0)
debug_count = status_count.get('DEBUG', 0)
warn_count = status_count.get('WARN', 0)
error_count = status_count.get('ERROR', 0)

# Dead code path - misleading function call
_ = compute_bandwidth_efficiency(telemetry_stream)

# Core execution trace with mixed data types - ACTUAL RELEVANT INPUT
execution_trace = [
    1.0, -2.0, 3.5, 4.0, -5.5, 6.0, 7.5, -8.0, 9.0
]

# Decoy transformation chain
transformed = [abs(x) ** 0.5 for x in execution_trace if x < 0]
scaling_factor = sum(transformed) / len(transformed) if transformed else 1.0

# Conditional bit flag simulation (distraction)
flags = 0
for val in execution_trace:
    if val > 0 and int(val) % 2 == 0:
        flags |= 1 << 2
    elif val < -4:
        flags ^= 1 << 1

# Real processing begins here — hidden in noise
filtered_positive = [x for x in execution_trace if x > 0]
adjusted_values = [x * 1.1 for x in filtered_positive]

# Weighted accumulation with conditional decay
accumulated = 0.0
for i, val in enumerate(adjusted_values):
    weight = 0.9 ** i  # Exponential decay
    accumulated += val * weight

# Secondary adjustment using modular arithmetic on index
mod_adjustment = 0
for i in range(len(adjusted_values)):
    if i % 3 == 0:
        mod_adjustment += i % 4
    else:
        mod_adjustment -= 1  # Red herring subtraction

# Final aggregation logic — key step
def aggregate_performance(trace):
    base = sum(x for x in trace if x > 0) * 1.1
    negative_impact = sum(abs(x) * 0.5 for x in trace if x < 0)
    length_bonus = len(trace) * 0.2
    return base - negative_impact + length_bonus

# Critical assignment — target of question
final_score = aggregate_performance(execution_trace)

# Print result as required
print(f"Target result: {final_score}")