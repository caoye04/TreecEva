from collections import defaultdict, Counter

# Simulated system telemetry data
timing_samples = [1.2, 0.8, 1.5, 2.3, 0.9, 1.1, 1.8, 2.1, 0.7, 1.4]
error_codes = [0, 1, 0, 3, 0, 0, 2, 3, 1, 0]
operation_types = ['read', 'write', 'read', 'delete', 'read', 'write', 'read', 'delete', 'write', 'read']

# Irrelevant accumulators (distractors)
total_reads = 0
summed_durations = 0.0
legacy_counter = 0
flag_history = []

# Misleading pre-processing (dead path)
for op in operation_types:
    if op == 'read':
        total_reads += 1

for t in timing_samples:
    summed_durations += t

# Unused transformation
inverted_timings = [round(1/t, 3) for t in timing_samples if t > 0]

# Decoy function (never called)
def legacy_diagnostic(data):
    return sum(data) / len(data) if data else 0

# Another decoy with red herring logic
def compute_reliability_index(errors):
    error_count = sum(1 for e in errors if e > 0)
    return (len(errors) - error_count) / len(errors)

# Real processing begins: filter and categorize
timing_log = defaultdict(list)
fault_severity = {1: 'warning', 2: 'critical', 3: 'critical'}
failure_flags = []

for i, (t, e) in enumerate(zip(timing_samples, error_codes)):
    if e > 0:
        flag_type = fault_severity.get(e, 'unknown')
        failure_flags.append((i, flag_type))
        
    # Categorize by timing quartile approximation
    if t < 1.0:
        timing_log['fast'].append(i)
    elif t < 1.6:
        timing_log['normal'].append(i)
    elif t < 2.0:
        timing_log['delayed'].append(i)
    else:
        timing_log['slow'].append(i)

# Dead code block: unreachable under current logic
if False:
    fallback_data = timing_log.copy()
    timing_log['reclassified'] = [x for x in fallback_data.values()]

# Auxiliary diagnostic (distractor)
phase_weights = {'fast': 1, 'normal': 2, 'delayed': 3, 'slow': 4}
score_components = []
for key, indices in timing_log.items():
    weighted_score = len(indices) * phase_weights.get(key, 0)
    score_components.append(weighted_score)

# Red herring: complex but unused calculation
aggregated_profile = dict(Counter([op[1] for op in failure_flags]))
impact_factor = 0
for sev in aggregated_profile.values():
    impact_factor += sev ** 1.5

# Key function that computes the actual answer
def aggregate_metrics(timings, flags):
    base_penalty = len(flags) * 100
    delay_bonus = 0
    
    # Additional penalty for slow operations
    if 'slow' in timings:
        delay_bonus = -len(timings['slow']) * 50
    
    # Conditional adjustment based on flag distribution
    critical_count = sum(1 for _, f in flags if f == 'critical')
    if critical_count >= 2:
        delay_bonus -= 75
    
    # Cross-check with operation types (limited relevance)
    recent_op = operation_types[-1]  # Only last op considered
    if recent_op == 'delete' and delay_bonus < 0:
        delay_bonus += 20  # Minor mitigation
    
    # Final computation
    result = base_penalty + delay_bonus
    
    # Secondary adjustment: if normal and fast are balanced
    stable_ops = len(timings.get('normal', [])) + len(timings.get('fast', []))
    if stable_ops > 5:
        result += 15
        
    return result

# Execution point of interest
final_diagnostic = aggregate_metrics(timing_log, failure_flags)

# Output required format
print(f"Target result: {final_diagnostic}")