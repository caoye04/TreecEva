def analyze_readings(data):
    adjusted = []
    offset = sum(data) / len(data)  # mean for centering
    temp_result = 0
    
    for val in data:
        shifted = val - offset
        if shifted > 0:
            adjusted.append(shifted ** 2)
        else:
            adjusted.append(abs(shifted))
    
    # Irrelevant transformation (dead-end computation)
    cumulative = 0
    for x in adjusted:
        cumulative += x * 0.5
    scaling_factor = len(adjusted) / (sum(adjusted) + 1e-8)
    fake_normalization = [a * scaling_factor for a in adjusted]

    return sum(adjusted)  # Only this matters


def validate_string_input(s):
    # Distractor function: not used in final logic
    if s.strip().lower().startswith('err'):
        return False
    return len(s) % 2 == 0


def calculate_performance(base, logs):
    base_adjusted = base * 1.5
    total_signal = 0
    noise_floor = 0.1

    # Simulate signal integration with filtering
    filtered_logs = [x for x in logs if x > noise_floor]
    
    # Multiple assignment and distractor unpacking
    n = len(filtered_logs)
    if n > 0:
        avg_log = sum(filtered_logs) / n
        max_log, min_log = max(filtered_logs), min(filtered_logs)
        range_correction = (max_log - min_log) * 0.2
    else:
        avg_log = 0
        range_correction = 0

    intermediate_score = 0
    for i in range(n):
        if i % 2 == 0:
            intermediate_score += filtered_logs[i] + range_correction
        else:
            intermediate_score -= filtered_logs[i] * 0.1

    # String-based flag check – irrelevant but looks important
    status_flag = "OK23" if intermediate_score > base else "WARN45"
    flag_length = len(status_flag)
    char_value = ord(status_flag[0])  # unused

    # Key computational chain
    raw_metric = analyze_readings(filtered_logs)
    penalty = 0
    if raw_metric > 5:
        penalty = base_adjusted * 0.3
    
    final_score = raw_metric * avg_log - penalty
    
    # Extra state tracking variables (not used)
    last_updated = '2023-11-05'
    version_tag = 'v2.1-debug'
    debug_trace = [base, n, final_score]

    return final_score

# Main execution
baseline = 10
readings = [0.5, 1.2, 0.8, 2.4, 3.1, 0.7]

# Red herring variable initialization
placeholder_data = ['temp', 'spike', 'null']
system_mode = 'ACTIVE'
buffer_size = len(placeholder_data) * 2

final_score = calculate_performance(baseline, readings)
print(f"Result: {final_score}")