def monitor_subsystem_performance(logs, threshold=75):
    performance_flags = []
    cumulative_load = 0
    peak_moment = -1
    
    for idx, load in enumerate(logs):
        cumulative_load += load
        if load > threshold and len(performance_flags) < 3:
            performance_flags.append(idx)
        if load == max(logs[:idx+1]) and load % 2 == 1:
            peak_moment = idx
    
    # Irrelevant transformation
    temp_analysis = [x * 1.05 for x in logs if x > 60]
    avg_temp = sum(temp_analysis) / len(temp_analysis) if temp_analysis else 0
    
    return cumulative_load, performance_flags, peak_moment


def calculate_stability_score(metrics, weights):
    # Dead function - never used in execution path
    score = 0
    for m, w in zip(metrics, weights):
        score += m * w
    return round(score, 3)


def decode_signal_sequence(signal):
    decoded = 0
    for bit in signal:
        decoded = (decoded << 1) | bit
    return decoded % 100


def evaluate_red_herring_conditions(state_vector):
    warnings = 0
    criticals = 0
    for i, val in enumerate(state_vector):
        if val < 0:
            warnings += 1
        elif val > 90:
            criticals += 1
    return warnings * 10 + criticals


def analyze_system_state(logs, sid):
    # Key data structures
    state_map = {i: val for i, val in enumerate(logs)}
    reverse_scan = sorted([(val, i) for i, val in state_map.items()], reverse=True)
    
    # Distractor dictionary
    diagnostics = {
        'initial': logs[0],
        'peak_index': reverse_scan[0][1],
        'entropy': 0,
        'checksum': sum(logs[i] * (i+1) for i in range(len(logs))) % 1000
    }
    
    # Real logic begins
    adjusted_logs = [logs[i] - 5 for i in range(0, len(logs), 2)]  # Only even indices
    filtered_logs = [x for x in adjusted_logs if x > 20]
    
    # Nested conditional with early exit red herring
    if len(filtered_logs) < 2:
        return -999
    
    base_value = 0
    for i, val in enumerate(filtered_logs):
        if i % 2 == 0:
            base_value += val * 3
        else:
            base_value -= val * 2
    
    # Misleading complex transformation
    shadow_process = [(i, val, val**2 % 17) for i, val in enumerate(logs) if val % 4 == 0]
    decoy_accumulator = 0
    for s in shadow_process:
        decoy_accumulator += s[2]
    
    # Actual key computation
    pivot_sum = 0
    for i, log_val in enumerate(logs):
        if i in state_map and state_map[i] % 7 == 0:
            pivot_sum += log_val // 3
    
    intermediate = (base_value + pivot_sum) % 10000
    
    # Final decision layer
    if sid ^ 13 == 10:
        final_diagnostic = intermediate + 500
    else:
        final_diagnostic = intermediate - 200
    
    return final_diagnostic

# Simulated input data
health_logs = [84, 42, 77, 56, 63, 91, 35, 48, 70, 52]
system_id = 13

# Trigger monitoring (irrelevant to final result)
monitor_subsystem_performance(health_logs, threshold=70)

# Signal processing decoy
signal_pattern = [1, 0, 1, 1, 0]
decoded_seq = decode_signal_sequence(signal_pattern)

# Real target execution
final_diagnostic = analyze_system_state(health_logs, system_id)
print(f"Target result: {final_diagnostic}")