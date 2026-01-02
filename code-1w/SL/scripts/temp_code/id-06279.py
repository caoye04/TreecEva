def evaluate_performance(log, thresh):
    base_score = 0
    penalty_adjustment = 0.0
    bonus_tracker = []
    temp_sum = 0

    # Irrelevant initialization (distractor)
    debug_flags = {'stage1': False, 'stage2': True, 'stage3': None}
    cycle_count = 0

    for entry in log:
        operation_type = entry['type']
        value = entry['value']
        timestamp = entry['ts']  # Unused field (misleading)

        if operation_type == 'read':
            base_score += value * 0.8
            if value > thresh * 1.2:
                bonus_tracker.append(value * 0.1)
        elif operation_type == 'write':
            base_score += value * 0.5
            penalty_adjustment -= value * 0.05
        elif operation_type == 'delete':
            # Complex but ultimately unused calculation
            temp_offset = value // 4
            temp_sum += temp_offset * 2
            if temp_offset > 5:
                debug_flags['stage3'] = True

    # Dead code path (conditional never met due to initialization)
    if debug_flags['stage1'] and debug_flags['stage3'] is None:
        cycle_count += 10
        base_score -= 5

    # Semi-relevant processing: only max bonus matters
    final_bonus = max(bonus_tracker) if bonus_tracker else 0

    # Core logic: score = base + bonus (penalty_adjustment is neutralized)
    net_penalty = penalty_adjustment if base_score < 100 else 0  # Always false
    raw_result = base_score + final_bonus + net_penalty

    # Final adjustment: truncate to integer
    final_score = int(raw_result)

    return final_score

# Main execution
metrics_data = [
    {'type': 'read', 'value': 40, 'ts': 1001},
    {'type': 'write', 'value': 20, 'ts': 1002},
    {'type': 'read', 'value': 60, 'ts': 1003},
    {'type': 'delete', 'value': 12, 'ts': 1004},
    {'type': 'read', 'value': 50, 'ts': 1005}
]

threshold = 45
final_score = evaluate_performance(metrics_data, threshold)
print(f"Result: {final_score}")