def calculate_performance(data):
    base_weights = [0.8, 1.2, 0.9, 1.1]
    adjustments = []
    temp_buffer = []

    for i, entry in enumerate(data):
        raw_value = entry['metric'] * base_weights[i % 4]
        if raw_value > 100:
            adjusted = 100 + (raw_value - 100) ** 0.5
        elif raw_value < 50:
            adjusted = 50 - (50 - raw_value) * 0.3
        else:
            adjusted = raw_value

        # Irrelevant transformation (distractor)
        temp_buffer.append((adjusted * 1.05) % 97)

        if i % 2 == 0:
            adjustments.append(adjusted * 0.95)
        else:
            adjustments.append(adjusted * 1.05)

    # Dead code path (distractor)
    if len(temp_buffer) > 100:
        cleanup = [x for x in temp_buffer if x > 10]
    else:
        cleanup = []

    # Key computation
    filtered_adjustments = [val for val in adjustments if val >= 60]
    avg_performance = sum(filtered_adjustments) / len(filtered_adjustments) if filtered_adjustments else 0

    # Secondary logic with slicing distraction
    history_log = adjustments[::2] + adjustments[1::2]
    decay_factor = 0.98 ** len(history_log)

    # Final score calculation
    final_score = avg_performance * decay_factor

    # Extra dictionary operations (semi-relevant)
    stats_summary = {
        'count': len(adjustments),
        'valid': len(filtered_adjustments),
        'efficiency': filtered_adjustments[-1] / adjustments[-1] if adjustments else 0
    }

    return final_score

# Input data (real impact on result)
benchmark_data = [
    {'metric': 85, 'id': 'A1'},
    {'metric': 92, 'id': 'B2'},
    {'metric': 45, 'id': 'C3'},
    {'metric': 103, 'id': 'D4'},
    {'metric': 67, 'id': 'E5'},
    {'metric': 58, 'id': 'F6'},
    {'metric': 110, 'id': 'G7'}
]

initial_threshold = 50  # Unused parameter (distractor)
dummy_mask = [i**2 for i in range(len(benchmark_data))]  # Dead computation

final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")