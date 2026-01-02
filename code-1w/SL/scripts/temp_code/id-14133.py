from collections import defaultdict

# Simulate system performance logs over time
def analyze_efficiency(raw_data):
    temp_results = []
    total_entries = len(raw_data)
    outlier_count = 0

    for entry in raw_data:
        stripped = entry.strip().lower()
        if 'error' in stripped:
            outlier_count += 1
            continue
        if 'critical' in stripped:
            temp_results.append(0.1)
        elif 'warning' in stripped:
            temp_results.append(0.5)
        else:
            temp_results.append(0.9)

    # Misleading normalization (not used in final logic)
    normalized = [x / sum(temp_results) for x in temp_results] if temp_results else [0]
    return temp_results

# Process timestamped events
log_lines = [
    "System: OK - nominal operation",
    "Warning: CPU threshold exceeded",
    "Error: Disk I/O failure",
    "Critical: Memory leak detected",
    "Info: User login successful",
    "Warning: High latency observed",
    "System: OK - all checks passed"
]

efficiency_values = analyze_efficiency(log_lines)

# Bonus calculation with distractor logic
base_multiplier = 1.5
scaling_factor = 0.8  # unused red herring
bonus_weights = []
for i, val in enumerate(efficiency_values):
    weight = base_multiplier * val
    if i % 2 == 0:
        weight *= 1.1  # arbitrary adjustment
    bonus_weights.append(round(weight, 3))

# Dead code path - simulates alternate logic that isn't triggered
dummy_cache = {}
for idx in range(len(bonus_weights)):
    dummy_cache[f'key_{idx}'] = bonus_weights[idx] * 0.01  # irrelevant computation

# Real processing begins here
status_flags = [1 if w > 1.0 else 0 for w in bonus_weights]
active_bonus_count = sum(status_flags)

# Core logic hidden among distractions
def calculate_performance(weights, logs):
    cumulative = 0.0
    count = 0
    tracker = defaultdict(int)

    for w in weights:
        tracker['processed'] += 1
        if w >= 1.0:
            cumulative += w * 1.2
        else:
            cumulative += w * 0.8
        count += 1
    
    avg_log_value = sum([len(log) for log in logs]) / len(logs)  # distraction
    adjustment = tracker['processed'] * 0.05  # minor tweak
    result = cumulative + adjustment

    # Additional noise
    intermediate_checksum = 0
    for c in "performance_check":
        intermediate_checksum += ord(c)
    # Checksum not used further

    return round(result, 4)

# Key execution point
final_score = calculate_performance(bonus_weights, log_lines)
print(f"Target result: {final_score}")