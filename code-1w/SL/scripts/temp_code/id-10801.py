def evaluate_performance(log_entries):
    base_threshold = 50
    bonus_factor = 1.2
    penalty_rate = 0.8
    intermediate_sum = 0
    temp_offset = 0

    # Irrelevant tracking variables (distractors)
    outlier_count = 0
    stability_flag = True
    debug_snapshot = []

    for entry in log_entries:
        metric_a = entry.get('response_time', 0)
        metric_b = entry.get('throughput', 0)
        status_flag = entry.get('status', 'OK')

        # Misleading computation that looks important but unused
        temp_offset += metric_a * 0.1 if metric_a > 100 else 0

        if status_flag == 'ERROR':
            outlier_count += 1
            continue

        score_component = metric_a + (metric_b * 2)
        if score_component > base_threshold:
            intermediate_sum += int(score_component * bonus_factor)
        else:
            intermediate_sum += int(score_component * penalty_rate)

    # Simulated data adjustment with set operations (semi-relevant)
    adjustment_keys = {f'adj_{i}' for i in range(len(log_entries)) if i % 2 == 0}
    legacy_flags = {'adj_0', 'adj_2', 'adj_4', 'adj_6'}
    active_adjustments = list(adjustment_keys & legacy_flags)

    # Another red herring: complex conditional expression not affecting final logic
    mode_weight = 1.1 if len(active_adjustments) > 2 and intermediate_sum > 0 else 0.95

    # Actual core logic buried among distractions
    raw_performance = intermediate_sum * mode_weight  # Looks influential, but weight is nearly neutral

    # Hidden critical step: correction based on valid entries count
    valid_entries = [e for e in log_entries if e.get('status') != 'ERROR']
    correction_factor = len(valid_entries) if len(valid_entries) < 10 else 10

    final_score = int(raw_performance // 10) + correction_factor

    # Dead code path (never reached in normal execution)
    if final_score < 0:
        debug_snapshot.append('NEGATIVE_SCORE_RECOVERY')
        final_score = abs(final_score)

    return final_score

# Simulated input data
log_data = [
    {'response_time': 60, 'throughput': 20, 'status': 'OK'},
    {'response_time': 120, 'throughput': 30, 'status': 'OK'},
    {'response_time': 40, 'throughput': 15, 'status': 'ERROR'},
    {'response_time': 80, 'throughput': 25, 'status': 'OK'},
    {'response_time': 30, 'throughput': 10, 'status': 'OK'},
    {'response_time': 90, 'throughput': 40, 'status': 'OK'}
]

# Key execution point
final_score = evaluate_performance(log_data)
print(f"Target result: {final_score}")