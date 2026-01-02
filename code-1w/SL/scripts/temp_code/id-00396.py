def evaluate_performance(metrics):
    base_score = 0
    bonus = 10
    penalty = 3
    temp_result = 0

    # Irrelevant accumulator for distraction
    running_total = 0
    for i in range(5):
        running_total += i * 2  # Distractor loop, unused later

    # Real logic begins: analyze metric completeness
    required_fields = {'latency', 'throughput', 'accuracy', 'consistency'}
    optional_fields = {'redundancy', 'overhead', 'jitter'}
    missing_required = required_fields - metrics
    extra_data = metrics - (required_fields | optional_fields)

    if len(missing_required) == 0:
        base_score += 25
    else:
        base_score -= 5 * len(missing_required)

    # Bonus for having all optional fields (unused in final answer but looks important)
    fully_equipped = True
    for field in optional_fields:
        if field not in metrics:
            fully_equipped = False
    if fully_equipped:
        bonus += 15  # Dead code path — bonus never used

    # Penalty for invalid extra fields
    if len(extra_data) > 0:
        base_score -= 4 * len(extra_data)

    # Additional distraction: string processing that seems related
    log_entry = "perf_metrics_v2_debug"
    tokens = log_entry.split('_')
    token_count = len(tokens)
    temp_result = sum(len(t) for t in tokens)  # Looks like scoring, but isn't

    # Critical arithmetic chain with bit operations (red herring)
    debug_flag = 0b1101
    mask = 0b1010
    masked_value = debug_flag & mask
    shift_correction = (masked_value >> 1) ^ 0b0011  # Computation unrelated to output

    # Accumulate real contributions
    final_score = base_score
    final_score += len(metrics.intersection(required_fields)) * 7
    final_score -= len(metrics.intersection({'consistency'})) * 2  # Specific penalty

    # One more distraction: floating point accumulation
    sample_values = [1.1, 2.2, 3.3]
    avg_val = sum(sample_values) / len(sample_values)
    normalized = round(avg_val, 2)  # Looks important, unused

    return final_score

# Simulated input from system probe
data_keys = ['latency', 'throughput', 'accuracy', 'consistency', 'cache_hit_ratio']
metric_set = set(data_keys)

# Execution point of interest
final_score = evaluate_performance(metric_set)
print(f"Target result: {final_score}")