import itertools

# System diagnostics simulator for distributed sensor network
sensor_ids = [101, 102, 103, 104]
base_frequency = 50
overload_threshold = 200
timing_log = [195, 188, 203, 177, 210, 165, 190, 182]
fault_flags = [False, True, False, True, False, False, True, False]

# Irrelevant auxiliary data (distractor)
diagnostic_codes = {'ERR_1': 'timeout', 'ERR_2': 'sync_fail', 'ERR_3': 'overflow'}
signal_history = {(t, id): (t * id) % 73 for t in range(3) for id in sensor_ids}

# Simulated noise buffer (dead code path)
noise_buffer = []
for i in range(10):
    noise_buffer.append((i ** 2 + 3 * i + 1) % 97)

# Misleading intermediate calculation (red herring)
effective_bandwidth = sum([(base_frequency + i) * 0.85 for i in range(len(sensor_ids))])
compression_ratio = 1.0
if effective_bandwidth > 200:
    compression_ratio = 0.75

# Decoy function (never called)
def analyze_redundancy(log):
    return [x * 1.1 for x in log if x < overload_threshold]

# Unused transformation (irrelevant computation)
normalized_load = [(x - 150) / 50 for x in timing_log if x > 0]
smoothed_signal = []
for i in range(1, len(normalized_load) - 1):
    smoothed_signal.append((normalized_load[i-1] + normalized_load[i] + normalized_load[i+1]) / 3)

# Conditional expression with distractors
status_flag = 'active' if sum(fault_flags) < 3 else 'critical'
emergency_mode = True if status_flag == 'critical' else False

# Real processing begins here — deeply nested and interwoven with noise
warning_count = 0
adjusted_timings = []

for idx, (t, f) in enumerate(itertools.zip_longest(timing_log, fault_flags, fillvalue=False)):
    if f:
        warning_count += 1
        # Apply correction only on faulty readings
        corrected = t - (t * 0.05)
    else:
        corrected = t + (5 if idx % 2 == 0 else -2)
    
    # Integer division and rounding used meaningfully
    rounded = int(round(corrected / 2.5) * 2.5)
    adjusted_timings.append(rounded)

# Secondary pass using conditional expressions and grouping
aggregated_stats = []
for group in itertools.batched(adjusted_timings, 2):  # Using itertools.batched (Python 3.12+)
    avg_group = sum(group) / len(group)
    deviation = abs(avg_group - base_frequency)
    category = 'stable' if deviation < 40 else 'volatile'
    weight = 0.9 if category == 'stable' else 1.2
    weighted_score = avg_group * weight
    aggregated_stats.append(weighted_score)

# Simulate redundant health check (distractor)
health_summary = {}
for i, score in enumerate(aggregated_stats):
    level = 'OK' if score < 200 else 'CHECK'
    health_summary[f'node_{i}'] = level

# Key logic hidden among distractions: count specific pattern
pattern_match_count = 0
for i in range(len(timing_log) - 2):
    if (timing_log[i] < timing_log[i+1] > timing_log[i+2]) and not fault_flags[i+1]:
        pattern_match_count += 1

# Core answer computation — obscured by context
primary_metric = sum(adjusted_timings) // len(adjusted_timings)  # integer division
secondary_metric = len([f for f in fault_flags if f]) * 10

timing_variance = sum((x - primary_metric) ** 2 for x in adjusted_timings) / len(adjusted_timings)

# Final aggregation function (target execution point)
def aggregate_metrics(log, flags):
    base = primary_metric
    penalty = secondary_metric
    adjustment = int(round(timing_variance / 10))
    if pattern_match_count >= 2:
        adjustment -= 5
    return base - penalty + adjustment

# Execution point of interest
final_diagnostic = aggregate_metrics(timing_log, fault_flags)

# Print result as required
print(f"Result: {final_diagnostic}")