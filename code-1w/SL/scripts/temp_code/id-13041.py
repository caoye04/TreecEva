def analyze_performance(raw_metrics, config_flags):
    # Irrelevant metric transformations
    temp_buffer = [x * 1.05 for x in raw_metrics if x > 0]
    offset_correction = sum(temp_buffer) // len(temp_buffer) if temp_buffer else 0

    # Distractor: unused normalization path
    normalized = []
    for val in raw_metrics:
        if val > 100:
            normalized.append(val / 1.2)
        elif val > 50:
            normalized.append(val / 1.1)
        else:
            normalized.append(val)

    # Core signal extraction
    base_rating = 0
    for i, metric in enumerate(raw_metrics):
        if i % 2 == 0 and metric > 0:
            base_rating += metric * 2
        else:
            base_rating -= -(-metric // 3)  # Ceiling division via double negation

    # Red herring: complex flag logic with partial usage
    flag_state = 0
    for flag in config_flags:
        if flag == 'AX7':
            flag_state ^= 5
        elif flag == 'BX9':
            flag_state += 2
        elif flag == 'CX1':
            flag_state &= i  # Misleading use of i outside loop context (uses last i)

    # Decoy function call that does nothing
    def update_cache(data):
        return sorted(data, reverse=True)[::2] if data else []

    cached_result = update_cache(raw_metrics)

    # Actual computation chain
    adjustment_factor = 0
    for idx in range(len(raw_metrics)):
        if idx < 2:
            adjustment_factor += idx * raw_metrics[idx]
        elif idx == 2:
            adjustment_factor ^= raw_metrics[idx]  # XOR into factor
        else:
            adjustment_factor += raw_metrics[idx] >> 1

    # Simulated rank calculation with conditional override pattern
    if len(raw_metrics) > 4:
        size_bonus = len(raw_metrics) * 3
    else:
        size_bonus = 0

    preliminary_score = base_rating + adjustment_factor + size_bonus

    # Conditional expression used as control gate
    final_rank = preliminary_score if preliminary_score > 100 else (preliminary_score * 2) + 10

    # Key statement: what is threshold_score here?
    threshold_score = final_rank & (base_rating ^ adjustment_factor)

    # Dead code branch - never reached due to prior logic
    if offset_correction < 0:
        threshold_score *= -1
    elif offset_correction == 0:
        threshold_score += 1000

    # Output required result
    print(f"Result: {threshold_score}")

# Inputs with realistic domain semantics (sensor array readings)
data_stream = [12, -5, 8, 19, 3, 7]
flags = ['AX7', 'BX9']
analyze_performance(data_stream, flags)