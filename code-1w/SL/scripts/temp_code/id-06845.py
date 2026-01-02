def analyze_efficiency(logs):
    total_entries = len(logs)
    valid_logs = [entry for entry in logs if 'ERROR' not in entry]
    error_count = total_entries - len(valid_logs)
    warning_count = sum(1 for log in logs if 'WARNING' in log)
    
    # Irrelevant aggregation
    char_count = sum(len(log) for log in logs)
    avg_length = char_count / total_entries if total_entries else 0
    distinct_words = set(word for log in logs for word in log.split())
    keyword_density = len([w for w in distinct_words if w.isupper()])

    return error_count, len(valid_logs), keyword_density


def calculate_metrics(data):
    processed = []
    for item in data:
        if item < 0:
            processed.append(item ** 2)
        elif item % 2 == 0:
            processed.append(item // 2)
        else:
            processed.append(item * 3 + 1)
    
    # Dead computation - not used later
    magnitude = sum(abs(x) for x in processed)
    processed_set = set(processed)
    filtered = [x for x in processed if x in processed_set and x > 10]

    return processed

# Simulated system telemetry
telemetry_data = [24, -5, 18, 31, -12, 7, 44]
log_stream = [
    "INFO: System initialized",
    "WARNING: High memory usage",
    "INFO: Data batch processed",
    "ERROR: Disk write failed",
    "WARNING: CPU threshold exceeded",
    "INFO: Restarting subsystem"
]

# Extract diagnostics
diag_errors, valid_count, _ = analyze_efficiency(log_stream)
refined_data = calculate_metrics(telemetry_data)

# Core productivity metrics
productivity = sum(refined_data[::2])  # every other element
errors = diag_errors * 2

# Distractor: complex slicing and set logic with no impact
subset_a = refined_data[1:4]
subset_b = refined_data[-3:]
overlap = set(subset_a) & set(subset_b)
redundant_flag = len(overlap) > 1 and max(overlap) > 20

# Secondary unused metric chain
temporal_weight = len(log_stream) // len(telemetry_data)
scaled_productivity = productivity + temporal_weight * 3

# Final evaluation function
def evaluate_performance(p, e):
    base = p - e * 1.5
    if p > 100:
        bonus = 10
    elif p > 50:
        bonus = 5
    else:
        bonus = 0
    
    # Extra logic that looks important but isn't triggered
    adjustment = 0
    if redundant_flag and e < 5:
        adjustment = 7
    elif 'High' in log_stream[1]:
        adjustment = -3
    
    return int(base + bonus)  # adjustment not added

final_score = evaluate_performance(productivity, errors)
print(f"Target result: {final_score}")