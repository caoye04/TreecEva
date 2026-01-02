def analyze_workload(inputs):
    # Irrelevant data processing (distractor)
    temp_results = []
    for x in inputs:
        if x % 7 == 0:
            temp_results.append(x * 2 + 1)
    normalized = [n / max(temp_results) for n in temp_results] if temp_results else [0]
    return sum(normalized) > 0.5

# Decoy function that looks important but is unused
def compute_bandwidth(latency, throughput):
    score = 0
    for i in range(1, min(latency, throughput)):
        if i % 3 == 0:
            score += i ** 2
        elif i % 5 == 0:
            score -= i
    return score if score != 0 else 100

# Another red herring: complex string analysis with no impact
log_entry = "system_boot_2024: init_complete | status=OK"
status_flag = log_entry.split('|')[1].strip().split('=')[1] if '|' in log_entry else 'UNKNOWN'
debug_mode = status_flag.lower() in ['ok', 'true'] and len(log_entry) % 2 == 0

# Real computation begins — heavily obscured
base_threshold = 42
raw_metrics = [85, 90, 78, 92, 88, 76, 95]

# Misleading transformation (not used in final result)
decoy_metrics = [x - 10 for x in raw_metrics if x > 80]
effective_weights = []
for i, val in enumerate(raw_metrics):
    weight = 1.1 if i % 2 == 0 else 0.9
    adjusted = val * weight
    effective_weights.append(round(adjusted, 2))

# Conditional expression with distractor variables
scaling_factor = 1.5 if debug_mode and sum(decoy_metrics) > 100 else 1.2

# Actual relevant logic buried here
metric_data = [x for x in raw_metrics if x >= base_threshold]

# Bit manipulation decoy
bitmask = 0b101010
masked_values = [x ^ bitmask for x in raw_metrics]

# Core logic hidden among noise
overflow_check = any(x > 100 for x in metric_data)
penalty = -5 if overflow_check else 0

# Conditional expression used meaningfully
bonus = 10 if len(metric_data) > 5 else 5

# Destructuring assignment (red herring)
first, *middle, last = raw_metrics
offset = (first + last) // 2

# The actual evaluation function
def evaluate_performance(data, threshold):
    count = len(data)
    average = sum(data) / count if count > 0 else 0
    level = 'high' if average >= threshold else 'low'
    
    # Nested logic with interdependencies
    if count >= 6:
        if average > 85:
            multiplier = 1.8
        else:
            multiplier = 1.4
    elif count >= 4:
        multiplier = 1.2
    else:
        multiplier = 0.8
    
    # Final calculation
    base_score = average * multiplier
    return int(base_score + bonus + penalty)

# Critical statement
final_score = evaluate_performance(metric_data, base_threshold)

# Print result as required
print(f"Result: {final_score}")