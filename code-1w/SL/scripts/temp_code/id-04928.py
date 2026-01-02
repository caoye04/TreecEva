import math

# Simulated system telemetry and diagnostic processing
# with extensive red herrings and irrelevant transformations
timing_log = [1.2, 0.8, 1.5, 2.3, 0.7, 1.1, 0.9, 1.4]
system_flags = [True, False, True, True, False, True, False, True]

# Irrelevant statistical summaries (distractors)
mean_latency = sum(timing_log) / len(timing_log)
median_latency = sorted(timing_log)[len(timing_log)//2]
std_deviation = math.sqrt(sum((x - mean_latency)**2 for x in timing_log) / len(timing_log))

# Fake anomaly detection using unused heuristics
anomaly_threshold = 2.0
spike_count = sum(1 for t in timing_log if t > anomaly_threshold)
anomaly_score = spike_count * 0.7 + (sum(system_flags) * 0.3)

# Unused data transformation path (dead code)
def legacy_calibrate(data):
    return [round(x * 0.95, 2) for x in data if x > 1.0]

calibrated_log = legacy_calibrate(timing_log)  # Computed but not used

# Red herring: complex flag analysis with no impact
flag_patterns = []
for i, flag in enumerate(system_flags):
    if flag and i % 2 == 0:
        flag_patterns.append(i * 1.5)
    elif not flag and i % 3 == 0:
        flag_patterns.append(-i)

# Decoy function that looks important but isn't called
def compute_health_index(log, flags):
    weighted_sum = sum(log[i] * (2 if flags[i] else 0.5) for i in range(len(log)))
    return weighted_sum / len(log)

# Real computation buried among distractions
status_weights = list(map(lambda x: 1.3 if x < 1.0 else 0.8, timing_log))

# Conditional adjustment based on paired flag-state
adjusted_metrics = []
for idx, (t, f) in enumerate(zip(timing_log, system_flags)):
    if f:
        adjusted_metrics.append(t * status_weights[idx])
    else:
        adjusted_metrics.append(t + 0.5)

# Secondary transformation with filtering
filtered_diagnostics = [val for val in adjusted_metrics if val > 1.0]

# Bit manipulation decoy (irrelevant calculation)
checksum = 0
for val in filtered_diagnostics:
    int_val = int(val * 10) % 256
    checksum ^= int_val  # Looks cryptographic but unused later

# Core logic hidden in nested conditional and enumeration
aggregate = 0.0
for index, value in enumerate(filtered_diagnostics):
    if index % 2 == 0:
        aggregate += value * (index + 1)
    else:
        aggregate -= value * 0.5

# Final computation depends only on this function
# All prior decoys are intentionally misleading
def aggregate_metrics(log_data, flag_list):
    weights = [1.3 if t < 1.0 else 0.8 for t in log_data]
    temp_vals = []
    for i, (t, f) in enumerate(zip(log_data, flag_list)):
        if f:
            temp_vals.append(t * weights[i])
        else:
            temp_vals.append(t + 0.5)
    above_threshold = [v for v in temp_vals if v > 1.0]
    result = 0.0
    for j, v in enumerate(above_threshold):
        if j % 2 == 0:
            result += v * (j + 1)
        else:
            result -= v * 0.5
    return int(result * 10)  # Deterministic integer output

# Critical execution point
final_diagnostic = aggregate_metrics(timing_log, system_flags)

# Print required result
print(f"Result: {final_diagnostic}")