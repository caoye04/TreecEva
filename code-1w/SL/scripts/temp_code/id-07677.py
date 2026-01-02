def analyze_pattern(sequence):
    magnitude = sum([x ** 2 for x in sequence if x % 2 == 1])
    offset = len(sequence) // 2
    temp_result = 0
    for i in range(offset):
        temp_result += sequence[i] * (i + 1)
    return magnitude - temp_result


def validate_chain(integrity_array):
    checksum = 0
    for val in integrity_array:
        checksum ^= val  # bitwise XOR for validation
    parity = sum(integrity_array) % 7
    return checksum + parity


def evaluate_threshold(state, log_entries):
    base_metric = 0
    adjustment = 0
    
    # Irrelevant preprocessing block (distractor)
    filtered_logs = [entry for entry in log_entries if entry > 0]
    noise_floor = sum(filtered_logs) / len(filtered_logs) if filtered_logs else 0
    
    for step in state:
        if step < 0:
            base_metric += abs(step)
        elif step % 3 == 0 and step != 0:
            adjustment += 1
        else:
            base_metric += step // 2
    
    # Secondary logic path that doesn't alter final answer
    outlier_count = 0
    for entry in log_entries:
        if entry > 50:
            outlier_count += 1
            break
    
    # Key computation
    raw_score = base_metric * 3 + adjustment * 2
    
    # Dead code (never executed, but looks relevant)
    if outlier_count < 0:  
        raw_score -= 100
    
    normalized = raw_score % 97
    return normalized

# Simulated system state
network_state = [12, -5, 9, 0, 18, -3, 7]
activation_log = [10, 20, 5, 60, 15, 25, 6]

# Auxiliary analysis (distractor)
sequence_diagnostic = [3, 6, 9, 12]
diag_result = analyze_pattern(sequence_diagnostic)

# Integrity check (semi-relevant but not used in final result)
integrity_data = [12, -5, 9, 18]
validation_code = validate_chain(integrity_data)

# Core evaluation
threshold_score = evaluate_threshold(network_state, activation_log)

print(f"Result: {threshold_score}")