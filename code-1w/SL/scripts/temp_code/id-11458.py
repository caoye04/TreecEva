def analyze_workload(inputs):
    # Irrelevant transformation: simulates signal processing but unused
    processed = [((x >> 2) ^ 15) & 7 for x in inputs if x % 3 == 0]
    return sum(processed) * 0.5

# Misleading global variables (red herrings)
threshold_limit = 95
temp_buffer = [0] * 100
system_state = {'active': True, 'mode': 'debug'}

# Unused helper function (dead code path)
def legacy_calibrate(val):
    return (val // 7) + 2 if val > 50 else (val * 3) % 17

# Core logic disguised among distractors
def compute_entropy(data):
    total = 0
    for d in data:
        if d <= 0:
            continue
        total += int(d ** 0.5) if d % 2 == 0 else (d // 3)
    return total

def filter_anomalies(records, cutoff):
    # Uses set operations and conditional expressions
    valid_set = {r for r in records if r > 0}
    outlier_set = {r for r in records if r < -10}
    adjusted = [r if r not in outlier_set else abs(r) for r in records]
    return adjusted, len(valid_set) > cutoff

# Dictionary-based weight mapping (relevant)
baseline_metrics = {
    'weight_a': 1.2,
    'weight_b': 0.8,
    'penalty_factor': lambda x: 0.95 if x > 70 else 1.1
}

# Diagnostic input with mixed types (only integers used in computation)
diagnostic_set = [12, -5, 18, 21, 0, 24, 33, 8, -12, 6]

# Simulated preprocessing (partially irrelevant)
normalized = []
for val in diagnostic_set:
    if val > 10:
        normalized.append(val * 0.9)
    elif val > 0:
        normalized.append(val * 1.1)
    else:
        normalized.append(abs(val))

# Secondary analysis with decoy result
device_load = analyze_workload(diagnostic_set)  # This is never used later

# Actual critical path begins here
cleaned_data, meets_threshold = filter_anomalies(diagnostic_set, 5)
entropy_value = compute_entropy(cleaned_data)

# Conditional expression using dictionary value
penalty = baseline_metrics['penalty_factor'](entropy_value)

# Bit manipulation side calculation (distractor)
shadow_flag = 0
for i in range(len(diagnostic_set)):
    shadow_flag ^= i << (i % 3)

# Main scoring logic buried in complexity
raw_score = 0
for idx, val in enumerate(cleaned_data):
    if idx % 2 == 0:
        raw_score += val * baseline_metrics['weight_a']
    else:
        raw_score += val * baseline_metrics['weight_b']

# Final adjustment using multiple concepts
evaluation_log = {
    'inputs': cleaned_data,
    'entropy': entropy_value,
    'raw': raw_score,
    'adjusted': raw_score * penalty
}

# Critical statement
final_score = int(evaluation_log['adjusted']) + (entropy_value // 5)

print(f"Result: {final_score}")