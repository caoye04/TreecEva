def evaluate_performance(log, thresh):
    base_score = 0
    penalty_adjustment = 0
    bonus_multiplier = 1.0
    temp_accumulator = 0  # irrelevant tracking
    debug_trace = []  # dead storage

    for entry in log:
        operation_type = entry['type']
        value = entry['value']
        timestamp = entry['time']  # unused field

        if operation_type == 'compute':
            base_score += value // 2
            if value > 10:
                penalty_adjustment -= 1
        elif operation_type == 'verify':
            base_score += int(value * 0.75)
            temp_accumulator += value % 3  # semi-relevant but not used
        elif operation_type == 'calibrate':
            if value < 0:
                bonus_multiplier *= 0.9
            else:
                bonus_multiplier *= 1.1

    # Secondary loop for validation (distractor logic)
    consistency_check = 0
    for entry in log:
        if entry['type'] == 'verify' and entry['value'] > thresh:
            consistency_check += 1
    if consistency_check > 3:
        bonus_multiplier += 0.05  # minor red herring adjustment

    # Core result computation
    final_score = int((base_score + penalty_adjustment) * bonus_multiplier)
    
    # Irrelevant post-processing
    normalized_score = round(final_score / 10.0, 2)  # not used
    status_flag = 'PASS' if final_score > thresh else 'FAIL'  # unused

    return final_score

# Simulated system metrics log
dataset_integrity = [8, 12, 15]
metrics_log = [
    {'type': 'compute', 'value': 16, 'time': 1001},
    {'type': 'verify', 'value': 20, 'time': 1002},
    {'type': 'calibrate', 'value': 5, 'time': 1003},
    {'type': 'compute', 'value': 8, 'time': 1004},
    {'type': 'verify', 'value': 14, 'time': 1005},
    {'type': 'calibrate', 'value': -2, 'time': 1006},
    {'type': 'compute', 'value': 12, 'time': 1007}
]
threshold = 25

# Execution point of interest
final_score = evaluate_performance(metrics_log, threshold)
print(f"Target result: {final_score}")